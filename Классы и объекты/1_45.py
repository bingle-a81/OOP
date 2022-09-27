class Decorator:
    def __init__(self, func):
        self.__func = func

    def __call__(self, x, y=1):
        return self.__func(x) + y


@Decorator
def my_func(x):
    return x

print(type(my_func))
a = my_func(10,11)  # Попробуйте добавить второй аргумент
print(a)