class Person:
    __name = '小甲鱼'
    def getName(self):
	return self.__name

p = Person()
p.__name
p.getName()
