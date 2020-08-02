class Ball:
    def __init__(self, name):
	self.name = name
    def kick(self):
	print("我叫%s，该死的，谁踢我..." % self.name)

b = Ball('土豆')
b.kick()
