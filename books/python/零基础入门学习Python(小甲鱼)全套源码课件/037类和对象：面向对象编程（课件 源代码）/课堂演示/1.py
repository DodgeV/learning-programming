class Ball:
    def setName(self, name):
        self.name = name
    def kick(self):
	print("我叫%s，该死的，谁踢我..." % self.name)

a = Ball()
a.setName('球A') 
# 第一个参数self告诉Python是a对象在调用方法，因为是隐藏的并且由Python自己传入，所以我们这里不需要写进来。
b = Ball()
b.setName('球B')
c = Ball()
c.setName('土豆') # 这叫不按套路出牌

a.kick()
b.kick()
c.kick()
