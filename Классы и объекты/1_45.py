def counter(start=0):
    def step():
        nonlocal start
        start+=1
        return start
    return step

c1=counter()
print(c1())
print(c1())


class Deco:
    def __init__(self,param):
        self.param=param

    def __call__(self,func ):
        self.func=func
        def wrapper(*args, **kwds):
            result=self.func(list(map(str,(i+self.param for i in args[0]))))
            return result
        return wrapper

@Deco(3)
def ff(x):
    print(x)

ff(range(10))

# print(a)


            

