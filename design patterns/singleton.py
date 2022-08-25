


class Singleton(object):
    _instance = None
    def __new__(cls, *args, **kwargs):
        if cls._instance:
            # raise Exception("Cannot create another instance")
            pass
        else:
            cls._instance = super().__new__(cls)
        return cls._instance

class MyClass(Singleton):
    pass

C = MyClass()
