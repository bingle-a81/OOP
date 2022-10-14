from functools import reduce
class Des:
    def __set_name__(self, owner, name):
        self.name= f'_{owner.__name__}__{name}'
    def __get__(self, instance, owner):
        return getattr(instance,self.name)
    def __set__(self, instance, value):
        if type(value) not in (int,float) or value<0:
            raise ValueError("длины сторон треугольника должны быть положительными числами")
        setattr(instance,self.name,value)


class Triangle:
    a=Des()
    b=Des()
    c=Des()
    def __init__(self,a, b, c):
        self.a=a
        self.b =b
        self.c =c
        if not self.__verify():
            raise ValueError("с указанными длинами нельзя\
                             образовать треугольник")

    def __verify(self):
        i=[self.a, self.b, self.c]
        return max(i) <sum(i) - max(i)

    def __len__(self):
        return int(self.a+self.b+self.c)

    def __call__(self, *args, **kwargs):
        a, b, c = self.a, self.b, self.c
        p=len(self)/2
        return (p * (p-a) * (p-b) * (p-c))**0.5

tr = Triangle(5, 4, 3)
assert tr.a == 5 and tr.b == 4 and tr.c == 3, "дескрипторы вернули неверные значения"

try:
    tr = Triangle(-5, 4, 3)
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

try:
    tr = Triangle(10, 1, 1)
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

tr = Triangle(5, 4, 3)
assert len(tr) == 12, "функция len вернула неверное значение"
assert 5.9 < tr() < 6.1, "метод __call__ вернул неверное значение"