# 以下代码为提示框架
# 请在...处使用一行或多行代码替换
# 请在______处使用一行代码替换

import _______________
txt = input("请输入一段中文文本：")
________________
print('{:.1f}'.format(len(txt)/len(ls)))



######################答案#####################################
import jieba
txt = input("请输入一段中文文本：")
ls = jieba.lcut(txt)
print('{:.1f}'.format(len(txt)/len(ls))) 
