class C:
    def __getattribute__(self, name):
        print('getattribute')
        # 使用 super() 调用 object 基类的 __getattribute__ 方法
	return super().__getattribute__(name)  

    def __setattr__(self, name, value):
	print('setattr')
	super().__setattr__(name, value)

    def __delattr__(self, name):
        print('delattr')
	super().__delattr__(name)

    def __getattr__(self, name):
        print('getattr')
