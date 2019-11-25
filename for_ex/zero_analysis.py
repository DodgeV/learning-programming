from pymongo import MongoClient, DESCENDING, ASCENDING
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
import sys
import traceback

# 到数据源的链接
db = MongoClient('mongodb://127.0.0.1:27017/')['my_quants']

class FactorZeroAnalysis:
	def __init__(self):
		# 单期收益的DataFrame
		self.profit_df = pd.DataFrame(columns={
			'top', 'bottom', 'portfolio'})
		# 累计收益的DataFrame
		self.cumulative_profit = pd.DataFrame(columns={
			'top', 'bottom', 'portfolio'})
		# 单期股次数的DataFrame
		self.count_df = pd.DataFrame(columns={
			'top', 'bottom'})

		# 净值
		self.last_top_net_value = 1
		self.last_bottom_net_value = 1
		self.last_portfolio_net_value = 1

	"""
	市值的零投资组合分析
	"""
	def analyze(self):
		# 每30个交易日调整一次
		_interval = 30
		# 检验时间为2016和2017年两年
		_from = '2016-01-01'
		_to = '2018-03-31'

		# 获取实际开始的的一个交易日
		first_trading_date = db.trading_dates.find_one(
			{'is_trading': True, 'date': {'$gte': _from}}, sort=[('date', ASCENDING)])['date']

		# 获取实际结束的最后一个交易日
		last_trading_date = db.trading_dates.find_one(
			{'is_trading': True, 'date': {'$lte': _to}}, sort=[('date', DESCENDING)])['date']

		end_date = datetime.strptime(last_trading_date, '%Y-%m-%d')

		# 第一个调整日从第一个交易日开始
		adjust_date_str = first_trading_date
		adjust_date = datetime.strptime(adjust_date_str, '%Y-%m-%d')

		# 首档和末档，股票代码和后复权价格的Dictionary
		top_dailies = dict()
		bottom_dailies = dict()
		# 调整日和当期收益的Dictionary
		date_profit = dict()
		# 暂存上一个调整
		last_adjust_date = None

		# 计算每日收益
		while adjust_date <= end_date:
			# 获取买入价格
			daily_cursor = db.k_day.find(
				{'time': adjust_date_str, 'code': {'$regex': '^[0|6|3]0\d{4}$'}},
				sort=[('mkt_cap', ASCENDING)],
				projection={'mkt_cap': True, 'code': True, 'close': True, 'adjfactor': True, 'trade_status': True, '_id': False})

			dailies = [x for x in daily_cursor]

			# 构建股票代码和后复权价格相对应的dictionary
			code_post_close_dict = dict()
			for daily in dailies:
				code_post_close_dict[daily['code']] = daily['close'] * daily['adjfactor']

			#计算收益
			self.compute_profit(last_adjust_date, code_post_close_dict, top_dailies, bottom_dailies, adjust_date)

			# 计算每当包含的股票数
			total_size = len(dailies)
			single_position_count = int(total_size/10)

			#调整首档组合
			self.adjust_top_position(top_dailies, dailies, single_position_count)

			#调整末档组合
			self.adjust_bottom_position(bottom_dailies, dailies, single_position_count)

			# 保存上一个调整日
			last_adjust_date = adjust_date_str
			# 到下一个调整日
			adjust_date_str = db.trade_dates.find_one(
				{'is_trading': True, 'date': {'$gte': adjust_date_str}}, 
				skip=_interval,
				sort=[('date', ASCENDING)])['date']
			adjust_date = datetime.strptime(adjust_date_str, '%Y-%m-%d')

		# 生成零投资组合的组合收益
		self.profit_df['portfolio'] = self.profit_df['top'] - self.profit_df['bottom']

		self.draw()


	"""
	调整首档组合
	1. 移除上期调入且当前非停牌股票
	2. 加入当期应跳入且当前非停牌股票
	3. 加入时，应按照排序从头逐个加入，直到满足数量要求
	"""
	def adjust_top_position(self, top_dailies, dailies, single_position_count):
		# 移除首档非停牌股票
		self.remove_stocks(top_dailies, dailies)

		# 首档股票，保留后复权的价格
		top_size = len(top_dailies.keys())
		for daily in dailies:
			# 可能已经存在股票，所以需要先判断是否已经满足了数量要求
			if top_size == single_position_count:
				break

			# 只有是交易状态的股票才被纳入组合
			code = daily['code']
			if daily['trade_status'] == 'trading':
				top_dailies[code] = daily['close'] * daily['adjfactor']
				top_size += 1

	"""
	移除当期中非停牌的股票
	"""
	def remove_stocks(self, position_dailies, dailies):
		# 首期时，还不存在股票
		if len(position_dailies.keys()) == 0:
			pass

		# 只有非停牌的股票，才会被移除
		for daily in dailies:
			code = daily['code']
			if daily['trade_status'] == 'trading' and code in position_dailies:
				del position_dailies[code]

	"""
	调整末档组合
	1. 移除上期调入且当前非停牌股票
	2. 加入当期应跳入且当前非停牌股票
	3. 加入时，应按照排序从末尾逐个加入，直到满足数量要求
	"""
	def adjust_bottom_position(self, bottom_dailies, dailies, single_position_count):
		# 移除首档非停牌股票
		self.remove_stocks(bottom_dailies, dailies)
		# 末档股票，保留后复权的价格
		bottom_size = len(bottom_dailies.keys())
		# 所有股票数
		total_size = len(dailies)
		for index in range(1, total_size):
			# 可能已经存在股票，所以需要先判断是否已经满足了数量要求
			if bottom_size == single_position_count:
				break

			# 末档要从最后一个向前回溯
			daily = dailies[-index]
			code = daily['code']
			# 只有是交易状态的股票才被纳入组合
			if daily['trade_status'] == 'trading':
				bottom_dailies[code] = daily['close'] * daily['adjfactor']
				bottom_size += 1


	"""
	计算收益
	"""
	def compute_profit(self, last_adjust_date, code_post_close_dict, top_dailies, bottom_dailies, adjust_date):
		# 只有存在上一个调整日，才计算上期的收益
			if last_adjust_date is not None:
				# 计算首档收益
				top_profit = self.compute_average_profit(code_post_close_dict, top_dailies, adjust_date)

				# 计算末档收益
				bottom_profit = self.compute_average_profit(code_post_close_dict, bottom_dailies, adjust_date)

				# 计算组合收益
				portfolio_profit = top_profit[0] - bottom_profit[0]
				# 添加结果的DataFrame中
				self.profit_df.loc[last_adjust_date] = {
					'top': top_profit[0],
					'bottom': bottom_profit[0],
					'portfolio': portfolio_profit
				}

				# 计算累积收益（复利方式）
				# 首档
				top_cumulative_profit = round((self.last_top_net_value * (1 + top_profit[0] / 100) - 1) * 100, 2)
				self.last_top_net_value *= (1 + top_profit[0] / 100)
				# 末档
				bottom_cumulative_profit = round((self.last_bottom_net_value * (1 + bottom_profit[0] / 100) - 1) * 100, 2)
				self.last_bottom_net_value *= (1 + bottom_profit[0] / 100)
				#组合
				portfolio_cumulative_profit = round((self.last_portfolio_net_value * (1 + portfolio_profit / 100) - 1) * 100, 2)
				self.last_portfolio_net_value *= (1 + portfolio_profit / 100)


				self.cumulative_profit.loc[last_adjust_date] = {
					'top': top_cumulative_profit,
					'bottom': bottom_cumulative_profit,
					'portfolio': portfolio_cumulative_profit
				}

				self.count_df.loc[last_adjust_date] = {
					'top': top_profit[1], 
					'bottom': bottom_profit[1]
				}



	"""
	绘制分析图
	"""
	def draw(self):
		print(self.profit_df)
		# 单期收益的曲线
		self.profit_df.plot(title='Single Profit', kind='line')
		# 单期收益的分布，直方图
		self.profit_df.hist(color='r', grid=False, bins=20, rwidth=0.6)
		# 单期入选股票数
		self.count_df.plot(title='Stock Count', kind='bar')
		# 累积收益曲线
		print(self.cumulative_profit)
		self.cumulative_profit.plot(title='Cumulative Profit', kind='line')
		# 显示图像
		plt.show()


	"""
	计算某一期某一个档的平均收益
	"""
	def compute_average_profit(self, code_post_close_dict, position_code_close_dict, _date):
		# 提取股票列表
		codes = list(position_code_close_dict.keys())

		# 只有存在股票时，才进行计算
		if len(codes) > 0 :
			# 所有股票的累计收益
			profit_sum = 0
			# 实际参与统计的股票数
			count = 0
			# 计算所有股票的收益
			for code in codes:
				count += 1
				buy_close = position_code_close_dict[code]
				if code in code_post_close_dict:
					profit_sum += (code_post_close_dict[code] - buy_close)/buy_close
				else:
					# 有些停牌的股票没有日线，因此向前查找停牌前的最近一个时间
					last_daily = db.k_day.find_one(
						{'code':code, 'time': {'$lte': _date}},
						projection={'close': True, 'adjfactor': True, '_id': False})
					if last_daily is not None:
						profit_sum += (last_daily['close'] * last_daily['adjfactor'] - buy_close)/buy_close

			# 计算单期平均收益
			return (round(profit_sum * 100/count, 2), count)

		# 没有数据时，返回None
		return None


FactorZeroAnalysis().analyze()


