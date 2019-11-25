"""
实现单例模式，Spider在程序中只有一个实例。
Attributes:
    _instance: 唯一实例的引用。
"""


class Singleton(object):
    _instance = None

    def __new__(cls, *args, **kw):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kw)
        return cls._instance
