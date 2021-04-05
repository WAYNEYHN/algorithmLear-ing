class  Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            # orig = super(Singleton, cls)
            # cls._instance = orig.__new__(cls, *args, **kwargs)

            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance

class MyClass(Singleton):
    a = 1


class Borg(object):
    def __new__(cls, *args, **kwargs):
        ob = super(Borg, cls).__new__(cls, *args, **kwargs)
        ob.__dict__ = cls.state
        return ob
class MyClass2(Borg):
    a = 1



def singleton(cls):
    instaces = {}
    def getinstance(*args, **kwargs):
        if cls not in instaces:
            instaces[cls] = cls(*args, **kwargs)
        return instaces[cls]
    return getinstance

@singleton
class MyClass3:
    a  = 1

class My_Singleton(object):
    def foo(self):
        pass

My_Singleton = My_Singleton()















def Singleton(cls):
    instance = {}
    def getInstance(*args, **kwargs):
        if cls not in instance:
            instance[cls] =  cls(*args, **kwargs)
        return instance[cls]
    return getInstance

@Singleton
class A:
    def __new__(cls):
        print("a")




class B:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance
l = B()
b = B()
print(l is b)


def SingleTon(cls):
   instance = {}
   def getInstance(*args, **kwargs):
       if cls not in instance:
           instance[cls] = cls(*args, **kwargs)
        return instance[cls]
    return getInstance

@SingleTon
class C:
    pass

my = C()
my_2 = C()

print(my is my_2)