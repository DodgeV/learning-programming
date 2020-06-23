* sysuse "D:\stata\auto.dta"
* use auto.dta
* describe,short #只显示头部
* describe [variable] #全部显示或显示变量名
* count 
* count if price > 10000
* count if missing
* isid mpg #是否每一个都不一样
* isid price make
* ssc install unique
* help -search
* unique mpg weight
* codebook [var] [if] [in] [,option] #提供变量的一些信息,各种分位
* codebook price if price > 5000
* codebook price in 10/20   #/#
* codebook price in             10 #
* codebook price in 10/l       #/l  10分位到末尾
* codebook price in f/10       f/#  开头到10分位
* summarize [var] [if] [in] [weight] [,option]  #sum/summ
* summarize price,detail  #提供额外的统计量
* summarize price,clear  
