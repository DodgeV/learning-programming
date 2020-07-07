n = eval(input("请输入数量:"))
...
print ("总额为：",cost)


######################答案#############################

n = eval(input("请输入数量:"))
if n >= 10 :
    cost = n * 160 * 0.7
elif 5 <= n <= 9 :
    cost = n * 160 * 0.8
elif 2 <= n <= 4 :
    cost = n * 160 * 0.9
else:
    cost = n * 160
cost = int(cost)   #保留整数
print ("总额为：",cost)
