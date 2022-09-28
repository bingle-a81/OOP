class GentleGuy:
    def __init__(self,method):
        self.method=method

    def __call__(self, func):
        def wrapper(st:str):
            if st in self.method:
                return self.__getattribute__(st)(func)
        return wrapper

    def a(self,func):
        print(f'zzzz ')

@GentleGuy(('a','b',))
def ddd(a):
    print('cccc')

ddd('a')
