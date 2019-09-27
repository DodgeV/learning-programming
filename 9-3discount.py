def discounts(price,rate):
	final_price = price*rate
	print('这里试图打印全局变量',old_price)
	old_price= 80
	print('修改后的值为1',old_price)
	return final_price

old_price = float(input('请输入原价：'))
rate = float(input('请输入折扣率:'))
new_price = discounts(old_price,rate)
print('修改后的值是2',old_price)
print('打折后的价格是:',new_price)
print('这里试图打印局部变量',final_price)
