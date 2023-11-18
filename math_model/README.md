## Math modeling

### 方法(类比/创新)
+ 工具：matlab。不同于数学的演绎推理，数学建模的方法是归纳演绎，这决定了数学只要推理正确结果一定正确，而数学模型的演技结果必须接受实际的检验
+ 建立最简变量关系(函数关系)的方法
	- 观察法(结合初等数学)，适用于数据具有比例关系
	- 拟合。是一种数据处理的方式，不特指哪种方法拟合侧重于调整曲线的参数，使得与数据相符
		- 近似准测(拟合原理)分为
			1. 切比雪夫近似准则(偏差的最大绝对值最小，给定模型的函数关系 y=f(x) 和m个数据点(xi,yi) 的集合,对整个集合极小化最大绝对偏差|yi−f(xi)|)，对潜在的有较大偏差的单个数据点更大的权重
			2. 极小化绝对偏差之和准则，给予每个数据点相同的权重
			3. 最小二乘准则(绝对偏差平方和最小)，根据与中间某处的远近来进行加权,其与单个点具有的显著偏离有关
		- 插值(要求过已知点)可分为一维插值问题/二维插值问题，
			+ 插值函数(未知函数的近似函数)：足够简单;计算方便;足够好的性态(有足够高阶的导数)可导优于连续，连续优于分段
			+ 从多项式中找插值函数：多项式插值法。包括以下几种求法：
				+ 拉格朗日(Lagrange)插值法
					1.将复杂的问题简化为求特解，只经过点(x0,1)，其他点y值都为0
						利用该定理
							得出基函数，因为左右都已经是n次，所以A0只能是常数，并将(x0,1)带进去，解出A0
								最终得出特解多项式，然后同理得出另外n个
					2.将所有基函数连乘起来，拉格朗日插值多项式=对应节点的基函数与相应节点函数值乘积之和
					两点确定一条直线就是一次插值
					缺点：若遗漏了一个节点，则需要重算，即不具继承性
				+ 牛顿(Newton)插值法
					为简便计算，取等步长h，并引入差分，另外还有后差分，中心差分		
				+ Hermite插值法
				+ 分段线性插值法
				+ 三次样条插值法
			+ 从三角函数中找插值函数：三角插值法
			+ 分段插值法
			+ 有理插值法
		- 回归(重在研究两个变量或多个变量之间的关系)(不要求过已知点)
		- 逼近(不要求过已知点)


### 论文提交（MD5使用方法）
*MD5文件校验和使用说明：* [**MD5文件校验和使用说明**](https://github.com/zhanwen/MathModel/blob/master/MD5%E6%96%87%E4%BB%B6%E6%A0%A1%E9%AA%8C%E5%92%8C%E4%BD%BF%E7%94%A8%E8%AF%B4%E6%98%8E/%E4%BD%BF%E7%94%A8%E8%AF%B4%E6%98%8E.md)
### 论文模版更新
*LaTex 论文模版：* [**LaTex 论文模版**](https://github.com/zhanwen/MathModel/blob/master/2019%E5%B9%B4%E8%AE%BA%E6%96%87%E6%A8%A1%E7%89%88/2019%E5%B9%B4Latex%E6%A8%A1%E7%89%88.zip)  
*Word 论文模版：* [**Word 论文模版（已更新最新）**](https://github.com/zhanwen/MathModel/blob/master/2019%E5%B9%B4%E8%AE%BA%E6%96%87%E6%A8%A1%E7%89%88/%E2%80%9C%E5%8D%8E%E4%B8%BA%E6%9D%AF%E2%80%9D%E7%AC%AC%E5%8D%81%E5%85%AD%E5%B1%8A%E4%B8%AD%E5%9B%BD%E7%A0%94%E7%A9%B6%E7%94%9F%E6%95%B0%E5%AD%A6%E5%BB%BA%E6%A8%A1%E7%AB%9E%E8%B5%9B%E8%AE%BA%E6%96%87%E6%A0%BC%E5%BC%8F%E8%A7%84%E8%8C%83.doc)  
*LaTex 论文模版使用方式：* [**如何编译 Latex 文件**](https://github.com/zhanwen/MathModel/tree/master/2019%E5%B9%B4%E8%AE%BA%E6%96%87%E6%A8%A1%E7%89%88/latex_note.md)

### 更新/添加比赛官网地址[戳这里](https://cpipc.chinadegrees.cn/)
* [**“华为杯”中国研究生数学建模竞赛**](https://cpipc.chinadegrees.cn/cw/hp/4)
* [数学建模竞赛](https://cpipc.chinadegrees.cn/cw/hp/4)     
* [电子设计竞赛](https://cpipc.chinadegrees.cn/cw/hp/6)     
* [人工智能创新大赛](https://cpipc.chinadegrees.cn/cw/hp/2c9088a5696cbf370169a3f8101510bd)     
* [机器人创新设计大赛](https://cpipc.chinadegrees.cn/cw/hp/2c9088a5696cbf370169a3f8934810be)

### 国赛试题
* 研究生数学建模竞赛试题：[2019](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AF%95%E9%A2%98/2019%E5%B9%B4%E7%A0%94%E7%A9%B6%E7%94%9F%E6%95%B0%E5%AD%A6%E5%BB%BA%E6%A8%A1%E7%AB%9E%E8%B5%9B%E8%AF%95%E9%A2%98)、[2018](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AF%95%E9%A2%98/2018%E5%B9%B4%E7%A0%94%E7%A9%B6%E7%94%9F%E6%95%B0%E5%AD%A6%E5%BB%BA%E6%A8%A1%E7%AB%9E%E8%B5%9B%E8%AF%95%E9%A2%98)、[2017](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AF%95%E9%A2%98/2017%E5%B9%B4%E7%A0%94%E7%A9%B6%E7%94%9F%E6%95%B0%E5%AD%A6%E5%BB%BA%E6%A8%A1%E7%AB%9E%E8%B5%9B%E8%AF%95%E9%A2%98)、[2016](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AF%95%E9%A2%98/2016%E5%B9%B4%E7%A0%94%E7%A9%B6%E7%94%9F%E6%95%B0%E5%AD%A6%E5%BB%BA%E6%A8%A1%E7%AB%9E%E8%B5%9B%E8%AF%95%E9%A2%98)、[2015](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AF%95%E9%A2%98/2015%E5%B9%B4%E7%A0%94%E7%A9%B6%E7%94%9F%E6%95%B0%E5%AD%A6%E5%BB%BA%E6%A8%A1%E7%AB%9E%E8%B5%9B%E8%AF%95%E9%A2%98)、[2014](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AF%95%E9%A2%98/2014%E5%B9%B4%E7%A0%94%E7%A9%B6%E7%94%9F%E6%95%B0%E5%AD%A6%E5%BB%BA%E6%A8%A1%E7%AB%9E%E8%B5%9B%E8%AF%95%E9%A2%98)、[2013](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AF%95%E9%A2%98/2013%E5%B9%B4%E7%A0%94%E7%A9%B6%E7%94%9F%E6%95%B0%E5%AD%A6%E5%BB%BA%E6%A8%A1%E7%AB%9E%E8%B5%9B%E8%AF%95%E9%A2%98)、[2012](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AF%95%E9%A2%98/2012%E5%B9%B4%E7%A0%94%E7%A9%B6%E7%94%9F%E6%95%B0%E5%AD%A6%E5%BB%BA%E6%A8%A1%E7%AB%9E%E8%B5%9B%E8%AF%95%E9%A2%98)、[2011](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AF%95%E9%A2%98/2011%E5%B9%B4%E7%A0%94%E7%A9%B6%E7%94%9F%E6%95%B0%E5%AD%A6%E5%BB%BA%E6%A8%A1%E7%AB%9E%E8%B5%9B%E8%AF%95%E9%A2%98)、[2010](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AF%95%E9%A2%98/2010%E5%B9%B4%E7%A0%94%E7%A9%B6%E7%94%9F%E6%95%B0%E5%AD%A6%E5%BB%BA%E6%A8%A1%E7%AB%9E%E8%B5%9B%E8%AF%95%E9%A2%98)、[2009](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AF%95%E9%A2%98/2009%E5%B9%B4%E7%A0%94%E7%A9%B6%E7%94%9F%E6%95%B0%E5%AD%A6%E5%BB%BA%E6%A8%A1%E7%AB%9E%E8%B5%9B%E8%AF%95%E9%A2%98)、[2008](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AF%95%E9%A2%98/2008%E5%B9%B4%E7%A0%94%E7%A9%B6%E7%94%9F%E6%95%B0%E5%AD%A6%E5%BB%BA%E6%A8%A1%E7%AB%9E%E8%B5%9B%E8%AF%95%E9%A2%98)、[2007](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AF%95%E9%A2%98/2007%E5%B9%B4%E7%A0%94%E7%A9%B6%E7%94%9F%E6%95%B0%E5%AD%A6%E5%BB%BA%E6%A8%A1%E7%AB%9E%E8%B5%9B%E8%AF%95%E9%A2%98)、[2006](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AF%95%E9%A2%98/2006%E5%B9%B4%E7%A0%94%E7%A9%B6%E7%94%9F%E6%95%B0%E5%AD%A6%E5%BB%BA%E6%A8%A1%E7%AB%9E%E8%B5%9B%E8%AF%95%E9%A2%98)、[2005](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AF%95%E9%A2%98/2005%E5%B9%B4%E7%A0%94%E7%A9%B6%E7%94%9F%E6%95%B0%E5%AD%A6%E5%BB%BA%E6%A8%A1%E7%AB%9E%E8%B5%9B%E8%AF%95%E9%A2%98)、[2004](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AF%95%E9%A2%98/2004%E5%B9%B4%E7%A0%94%E7%A9%B6%E7%94%9F%E6%95%B0%E5%AD%A6%E5%BB%BA%E6%A8%A1%E7%AB%9E%E8%B5%9B%E8%AF%95%E9%A2%98)


### 国赛论文
* [2018年优秀论文](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2018%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87)
* [A题：关于跳台跳水体型系数设置的建模分析](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2018%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87/A)
* [B题：光传送网建模与价值评估](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2018%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87/B)
* [C题：对恐怖袭击事件记录数据的量化分析](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2018%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87/C)
* [D题：基于卫星高度计海面高度异常资料获取潮汐调和常数方法及应用](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2018%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87/D)
* [E题：多无人机对组网雷达的协同干扰](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2018%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87/E)
* [F题：航站楼扩增评估](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2018%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87/F)

* [2017年优秀论文](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2017%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87)
* [A题：无人机在抢险救灾中的优化运用](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2017%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87/A)
* [B题：面向下一代光通信的 VCSEL 激光器仿真模型](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2017%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87/B)
* [C题：航班恢复问题](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2017%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87/C)
* [D题：基于监控视频的前景目标提取](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2017%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87/D)
* [E题：多波次导弹发射中的规划问题](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2017%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87/E)
* [F题：地下物流系统网络](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2017%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87/F)

* [2016年优秀论文](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2016%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87)
* [A题：多无人机协同任务规划](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2016%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87/A) 
* [B题：具有遗传性疾病和性状的遗传位点分析](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2016%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87/B)
* [C题：基于无线通信基站的室内三维定位问题](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2016%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87/C)
* [D题：军事行动避空侦察的时机和路线选择](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2016%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87/D)
* [E题：粮食最低收购价政策问题研究](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2016%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87/E)

* [2015年优秀论文](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2015%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87)
* [A题：水面舰艇编队防空和信息化战争评估模型](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2015%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87/A)
* [B题：数据的多流形结构分析](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2015%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87/B)
* [C题：移动通信中的无线信道“指纹”特征建模](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2015%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87/C)
* [D题：面向节能的单/多列车优化决策问题](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2015%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87/D)
* [E题：数控加工刀具运动的优化控制](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2015%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87/E)
* [F题：旅游路线规划问题](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2015%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87/F)

* [2014年优秀论文](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2014%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87)
* [A题：小鼠视觉感受区电位信号(LFP)与视觉刺激之间的关系研究](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2014%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87/A)
* [B题：机动目标的跟踪与反跟踪](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2014%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87/B)
* [C题：无线通信中的快时变信道建模](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2014%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87/C)
* [D题：人体营养健康角度的中国果蔬发展战略研究](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2014%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87/D)
* [E题：乘用车物流运输计划问题](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2014%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87/E)

* [2013年优秀论文](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2013%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87)
* [A题：变循环发动机部件法建模及优化](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2013%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87/A)
* [B题：功率放大器非线性特性及预失真模型](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2013%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87/B)
* [C题：微蜂窝环境中无线接收信号的特性分析](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2013%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87/C)
* [D题：空气中PM2.5问题的研究 attachment](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2013%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87/D)
* [E题：中等收入定位与人口度量模型研究](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2013%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87/E)
* [F题：可持续的中国城乡居民养老保险体系的数学模型研究](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2013%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87/F) 

* [2012年优秀论文](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2012%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87)
* [A题：基因识别问题及其算法实现](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2012%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87/A)
* [B题：基于卫星无源探测的空间飞行器主动段轨道估计与误差分析](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2012%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87/B)
* [C题：有杆抽油系统的数学建模及诊断](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2012%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87/C)
* [D题：基于卫星云图的风失场(云导风)度量模型与算法探讨](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2012%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87/D) 

* [2011年优秀论文](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2011%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87)
* [A题：基于光的波粒二象性一种猜想的数学仿真](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2011%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87/A)
* [B题：吸波材料与微波暗室问题的数学建模](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2011%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87/B)
* [C题：小麦发育后期茎杆抗倒性的数学模型](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2011%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87/C)
* [D题：房地产行业的数学建模](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2011%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87/D) 

* [2010年优秀论文](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2010%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87)
* [A题：确定肿瘤的重要基因信息](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2010%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87/A)
* [B题：与封堵渍口有关的重物落水后运动过程的数学建模](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2010%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87/B)
* [C题：神经元的形态分类和识别](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2010%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87/C)
* [D题：特殊工件磨削加工的数学建模](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2010%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87/D) 

* [2009年优秀论文](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2009%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87)
* [A题：我国就业人数或城镇登记失业率的数学建模](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2009%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87/A)
* [B题：枪弹头痕迹，自动比对方法的研究](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2009%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87/B)
* [C题：多传感器数据融合与航迹预测](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2009%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87/C)
* [D题：110 警车配置及巡逻方案](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2009%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87/D) 

* [2008年优秀论文](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2008%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87)
* [A题：汶川地震中唐家山堪塞湖泄洪问题](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2008%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87/A)
* [B题：城市道路交通信号实时控制问题](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2008%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87/B)
* [C题：货运列车的编组调度问题]()
* [D题：中央空调系统节能设计问题]() 

* [2007年优秀论文](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2007%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87)
* [A题：建立食品卫生安全保障体系数学模型及改进模型的若干理论问题](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2007%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87/A)
* [B题：械臂运动路径设计问题](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2007%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87/B)
* [C题：探讨提高高速公路路面质量的改进方案](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2007%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87/C)
* [D题：邮政运输网络中的邮路规划和邮车调运](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2007%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87/D) 

* [2006年优秀论文](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2006%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87)
* [A题：Ad Hoc 网络中的区域划分和资源分配问题](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2006%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87/A)
* [B题：确定高精度参数问题](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2006%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87/B)
* [C题：维修线性流量阀时的内筒设计问题](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2006%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87/C)
* [D题：学生面试问题](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2006%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87/D) 
	
* [2005年优秀论文](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2005%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87)
* [A题：Highway Traveling time Estimate and Optimal Routing](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2005%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87/A)
* [B题：空中加油](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2005%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87/B)
* [C题：城市交通管理中的出租车规划](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2005%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87/C)
* [D题：仓库容量有限条件下的随机存贮管理](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2005%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87/D) 
	
* [2004年优秀论文](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2004%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87)
* [A题：发现黄球并定位](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2004%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87/A)
* [B题：使用下料问题](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2004%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87/B)
* [C题：售后服务数据的运用](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2004%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87/C)
* [D题：研究生录取问题](https://github.com/zhanwen/MathModel/tree/master/%E5%9B%BD%E8%B5%9B%E8%AE%BA%E6%96%87/2004%E5%B9%B4%E4%BC%98%E7%A7%80%E8%AE%BA%E6%96%87/D) 

### 美赛论文
* 特等奖论文：[2017](https://github.com/zhanwen/MathModel/tree/master/%E7%BE%8E%E8%B5%9B%E8%AE%BA%E6%96%87/2017%E7%BE%8E%E8%B5%9B%E7%89%B9%E7%AD%89%E5%A5%96%E5%8E%9F%E7%89%88%E8%AE%BA%E6%96%87%E9%9B%86)、[2016](https://github.com/zhanwen/MathModel/tree/master/%E7%BE%8E%E8%B5%9B%E8%AE%BA%E6%96%87/2016%E7%BE%8E%E8%B5%9B%E7%89%B9%E7%AD%89%E5%A5%96%E5%8E%9F%E7%89%88%E8%AE%BA%E6%96%87%E9%9B%86)、 [2015](https://github.com/zhanwen/MathModel/tree/master/%E7%BE%8E%E8%B5%9B%E8%AE%BA%E6%96%87/2015%E7%BE%8E%E8%B5%9B%E7%89%B9%E7%AD%89%E5%A5%96%E5%8E%9F%E7%89%88%E8%AE%BA%E6%96%87%E9%9B%86)、[2014](https://github.com/zhanwen/MathModel/tree/master/%E7%BE%8E%E8%B5%9B%E8%AE%BA%E6%96%87/2014%E7%BE%8E%E8%B5%9B%E7%89%B9%E7%AD%89%E5%A5%96%E5%8E%9F%E7%89%88%E8%AE%BA%E6%96%87%E9%9B%86)、 [2013](https://github.com/zhanwen/MathModel/tree/master/%E7%BE%8E%E8%B5%9B%E8%AE%BA%E6%96%87/2013%E7%BE%8E%E8%B5%9B%E7%89%B9%E7%AD%89%E5%A5%96%E5%8E%9F%E7%89%88%E8%AE%BA%E6%96%87%E9%9B%86)、[2012](https://github.com/zhanwen/MathModel/tree/master/%E7%BE%8E%E8%B5%9B%E8%AE%BA%E6%96%87/2012%E7%BE%8E%E8%B5%9B%E7%89%B9%E7%AD%89%E5%A5%96%E5%8E%9F%E7%89%88%E8%AE%BA%E6%96%87%E9%9B%86)、 [2011](https://github.com/zhanwen/MathModel/tree/master/%E7%BE%8E%E8%B5%9B%E8%AE%BA%E6%96%87/2011%E7%BE%8E%E8%B5%9B%E7%89%B9%E7%AD%89%E5%A5%96%E5%8E%9F%E7%89%88%E8%AE%BA%E6%96%87%E9%9B%86)、[2010](https://github.com/zhanwen/MathModel/tree/master/%E7%BE%8E%E8%B5%9B%E8%AE%BA%E6%96%87/2010%E7%BE%8E%E8%B5%9B%E7%89%B9%E7%AD%89%E5%A5%96%E5%8E%9F%E7%89%88%E8%AE%BA%E6%96%87%E9%9B%86)、 [2009](https://github.com/zhanwen/MathModel/tree/master/%E7%BE%8E%E8%B5%9B%E8%AE%BA%E6%96%87/2009%E7%BE%8E%E8%B5%9B%E7%89%B9%E7%AD%89%E5%A5%96%E5%8E%9F%E7%89%88%E8%AE%BA%E6%96%87%E9%9B%86)、[2008](https://github.com/zhanwen/MathModel/tree/master/%E7%BE%8E%E8%B5%9B%E8%AE%BA%E6%96%87/2008%E7%BE%8E%E8%B5%9B%E7%89%B9%E7%AD%89%E5%A5%96%E5%8E%9F%E7%89%88%E8%AE%BA%E6%96%87%E9%9B%86)、 [2007](https://github.com/zhanwen/MathModel/tree/master/%E7%BE%8E%E8%B5%9B%E8%AE%BA%E6%96%87/2007%E7%BE%8E%E8%B5%9B%E7%89%B9%E7%AD%89%E5%A5%96%E5%8E%9F%E7%89%88%E8%AE%BA%E6%96%87%E9%9B%86)、[2006](https://github.com/zhanwen/MathModel/tree/master/%E7%BE%8E%E8%B5%9B%E8%AE%BA%E6%96%87/2006%E7%BE%8E%E8%B5%9B%E7%89%B9%E7%AD%89%E5%A5%96%E5%8E%9F%E7%89%88%E8%AE%BA%E6%96%87%E9%9B%86)、 [2005](https://github.com/zhanwen/MathModel/tree/master/%E7%BE%8E%E8%B5%9B%E8%AE%BA%E6%96%87/2005%E7%BE%8E%E8%B5%9B%E7%89%B9%E7%AD%89%E5%A5%96%E5%8E%9F%E7%89%88%E8%AE%BA%E6%96%87%E9%9B%86)、[2004](https://github.com/zhanwen/MathModel/tree/master/%E7%BE%8E%E8%B5%9B%E8%AE%BA%E6%96%87/2004%E7%BE%8E%E8%B5%9B%E7%89%B9%E7%AD%89%E5%A5%96%E5%8E%9F%E7%89%88%E8%AE%BA%E6%96%87%E9%9B%86)

### 数学建模算法
* [数学建模相关算法MATLAB实现](https://github.com/HuangCongQing/Algorithms_MathModels)
* [经典算法](https://github.com/zhanwen/MathModel/tree/master/%E6%95%B0%E5%AD%A6%E5%BB%BA%E6%A8%A1%E7%AE%97%E6%B3%95)
* [现代算法](https://github.com/zhanwen/MathModel/tree/master/%E7%8E%B0%E4%BB%A3%E7%AE%97%E6%B3%95)
* [计算机仿真](https://github.com/zhanwen/MathModel/tree/master/%E7%8E%B0%E4%BB%A3%E7%AE%97%E6%B3%95/%E8%AE%A1%E7%AE%97%E6%9C%BA%E4%BB%BF%E7%9C%9F) 
* [粒子群算法](https://github.com/zhanwen/MathModel/tree/master/%E7%8E%B0%E4%BB%A3%E7%AE%97%E6%B3%95/%E7%B2%92%E5%AD%90%E7%BE%A4%E7%AE%97%E6%B3%95)
* [马尔可夫链](https://github.com/zhanwen/MathModel/tree/master/%E7%8E%B0%E4%BB%A3%E7%AE%97%E6%B3%95/%E9%A9%AC%E5%B0%94%E5%8F%AF%E5%A4%AB%E9%93%BE)
* [蒙特卡洛法](https://github.com/zhanwen/MathModel/tree/master/%E7%8E%B0%E4%BB%A3%E7%AE%97%E6%B3%95/%E8%92%99%E7%89%B9%E5%8D%A1%E6%B4%9B%E6%B3%95)
* [模拟退火法](https://github.com/zhanwen/MathModel/tree/master/%E7%8E%B0%E4%BB%A3%E7%AE%97%E6%B3%95/%E6%A8%A1%E6%8B%9F%E9%80%80%E7%81%AB%E6%B3%95)
* [神经网络](https://github.com/zhanwen/MathModel/tree/master/%E7%8E%B0%E4%BB%A3%E7%AE%97%E6%B3%95/%E7%A5%9E%E7%BB%8F%E7%BD%91%E7%BB%9C)
* [小波分析](https://github.com/zhanwen/MathModel/tree/master/%E7%8E%B0%E4%BB%A3%E7%AE%97%E6%B3%95/%E5%B0%8F%E6%B3%A2%E5%88%86%E6%9E%90)
* [遗传算法](https://github.com/zhanwen/MathModel/tree/master/%E7%8E%B0%E4%BB%A3%E7%AE%97%E6%B3%95/%E9%81%97%E4%BC%A0%E7%AE%97%E6%B3%95)

### 数模网站
* [MATLAB技术论坛](http://www.matlabsky.com/)
* [MATLAB中文论坛](https://www.ilovematlab.cn/)
* [数学中国](http://www.madio.net/portal.php)
* [全国大学生数学建模竞赛](http://www.mcm.edu.cn/)
* [数学建模网](https://www.shumo.com/home/)
* [toolbox大全](https://www.mathworks.com/matlabcentral/fileexchange/)

### 教材及课件及思维导图
* [国防科技术大学](https://github.com/zhanwen/MathModel/tree/master/%E6%95%99%E6%9D%90%E5%8F%8A%E8%AF%BE%E4%BB%B6/%E5%9B%BD%E9%98%B2%E7%A7%91%E6%8A%80%E6%9C%AF%E5%A4%A7%E5%AD%A6)
* [浙江大学课件](https://github.com/zhanwen/MathModel/tree/master/%E6%95%99%E6%9D%90%E5%8F%8A%E8%AF%BE%E4%BB%B6/%E6%B5%99%E6%B1%9F%E5%A4%A7%E5%AD%A6%E8%AF%BE%E4%BB%B6/PPT%E8%AF%BE%E4%BB%B6)
* [数学建模算法思维导图](https://github.com/zhanwen/MathModel/tree/master/Mind)

### Matlab video & notebook
+ [笔记本](https://github.com/DodgeV/learning-programming/blob/master/MATLAB_NOTE.md)
+ [机器学习及其MATLAB实现—从基础到实践[13节全]](https://www.bilibili.com/video/BV12W411q7Se)&[对应资料](https://github.com/DodgeV/learning-programming/tree/master/books/MATLAB/%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0%E5%8F%8A%E5%85%B6MATLAB%E5%AE%9E%E7%8E%B0)
+ [Matlab入门和在线性代数中的应用](https://github.com/zhanwen/MathModel/tree/master/Matlab%E5%85%A5%E9%97%A8%E6%95%99%E7%A8%8B)
+ [数学建模比赛MATLAB教学[23P]](https://www.bilibili.com/video/BV1db411Y7uQ)
+ [数学建模培训视频-小石老师[14讲]](https://www.bilibili.com/video/BV1by4y1B7dk)&[对应资料](https://github.com/DodgeV/learning-programming/tree/master/books/MATLAB/%E6%95%B0%E5%AD%A6%E5%BB%BA%E6%A8%A1%E5%9F%B9%E8%AE%AD%E8%A7%86%E9%A2%91-%E5%B0%8F%E7%9F%B3%E8%80%81%E5%B8%88-14%E8%AE%B2)
+ [《MATLAB函数查询及应用案例》](https://www.bilibili.com/video/BV1ry4y1C7fN)&[对应例子](https://github.com/DodgeV/learning-programming/blob/master/books/MATLAB/%E3%80%8AMATLAB%E5%87%BD%E6%95%B0%E6%9F%A5%E8%AF%A2%E5%8F%8A%E5%BA%94%E7%94%A8%E6%A1%88%E4%BE%8B%E3%80%8B.7z)
+ [MATLAB数据挖掘技术系列培训视频[6P]](https://www.bilibili.com/video/bv1Tp4y1y7G7)ds&[备用](https://www.bilibili.com/video/BV1NV411n7G7?p=66)&[对应资料](https://github.com/DodgeV/learning-programming/tree/master/books/MATLAB/MATLAB%E6%95%B0%E6%8D%AE%E6%8C%96%E6%8E%98%E6%8A%80%E6%9C%AF%E7%B3%BB%E5%88%97%E5%9F%B9%E8%AE%AD%E8%AF%BE%E4%BB%B6_PDF%E7%89%88)
+ [Matlab基础教程](https://www.bilibili.com/video/BV1VJ411p7M6)
+ [Matlab最基础纯手写教程--Taylim](https://www.bilibili.com/video/BV1q7411g7Dh)
+ [Matlab基础入门与算法实践--老教练](https://www.bilibili.com/video/BV1FD4y1m78C)&[对应资料](https://github.com/DodgeV/learning-programming/tree/master/books/MATLAB/Matlab%E5%9F%BA%E7%A1%80%E5%85%A5%E9%97%A8%E4%B8%8E%E7%AE%97%E6%B3%95%E5%AE%9E%E8%B7%B5)
+ [走进数学之数学建模（中国大学mooc）](https://www.bilibili.com/video/BV1ux411G7k3)
+ [数学建模--北航牛薇](https://www.bilibili.com/video/BV1d7411T7BK)
+ [数学建模--厦门大学](http://www.icourse163.org/learn/XMU-1001556009)
+ [科学计算与数学建模--中南大学](http://www.icourse163.org/learn/CSU-1001985002)
+ [数学建模--华中农业大学](http://www.icourse163.org/learn/HZAU-1001658002)
+ [数学模型--姜启源](https://www.bilibili.com/video/BV1VJ411w7r3/)
+ [数学建模--清风](https://www.bilibili.com/video/BV1DW411s7wi)
+ [数学模型--清华大学](https://www.bilibili.com/video/BV1Zx411y7Ah)&[对应资料](https://github.com/DodgeV/learning-programming/tree/master/books/MATLAB/%E6%95%B0%E5%AD%A6%E5%BB%BA%E6%A8%A1_%E6%B8%85%E5%8D%8E%E5%A4%A7%E5%AD%A683%E8%AE%B2)
+ [数学建模美赛/国赛 算法顶级培训(完)--老教练](https://www.bilibili.com/video/BV14b411v7dT)&[备用](https://www.bilibili.com/video/BV1e54y1e7cU)&[对应资料](https://github.com/DodgeV/learning-programming/tree/master/books/MATLAB/%E6%95%B0%E5%AD%A6%E5%BB%BA%E6%A8%A1%E9%AB%98%E9%98%B631%E5%A0%82%E8%AF%BE%E7%A8%8B%E8%B5%84%E6%96%99)
+ [【数学建模/零基础/教程】数学建模零基础快速入门教程(附代码)](https://www.bilibili.com/video/BV1Kb41167QZ)
+ [数学建模清风第一次直播：传染病模型和微分方程拟合](https://www.bilibili.com/video/BV1Hi4y1t7uu)

