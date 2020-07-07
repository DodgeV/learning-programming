# 以下代码为提示框架
# 请在...处使用一行或多行代码替换
# 请在______处使用一行代码替换
#
...
d = {}
...
ls = list(d.items())
ls.sort(key=lambda x:x[1], reverse=True) # 该语句用于排序
...
  fo.write('{},{}\n'.format(______))
...

##################答案###################################################

##fi = open("earpa001.txt","r")
##fo = open("earpa001_count.txt","w")
##d = {}
##for line in fi:
##    t = line.strip(" \n").split(",")
##    s = t[2] + "-" + t[3]
##    d[s] = d.get(s,0) + 1  # 如果字典d中存在键s则将字典d中键为s的值+1，如果不存在，则默认值为0再+1,也对应是第一次遍历到该楼层和区域。
##ls = list(d.items())
##ls.sort(key=lambda x:x[1], reverse=True) # 该语句用于排序，当reverse=False时：为正向排序；当reverse=True时：为反向排序。
##for i in range(len(ls)):
##    a,b = ls[i]
##    fo.write('{},{}\n'.format(a,b))
##fi.close()
##fo.close()

