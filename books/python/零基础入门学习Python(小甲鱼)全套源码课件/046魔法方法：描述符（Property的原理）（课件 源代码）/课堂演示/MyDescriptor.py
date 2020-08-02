class MyDescriptor:
	def __get__(self, instance, owner):
		print("getting...", self, instance, owner)
		
	def __set__(self, instance, value):
		print("setting...", self, instance, value)
		
	def __delete__(self, instance):
		print("deleting...", self, instance)

class Test:
	x = MyDescriptor()
