class Thing:
    def __init__(self,name, weight):
        self.name=name
        self.weight=weight


class Bag:
    def __init__(self,max_weight) -> None:
        self.max_weight=max_weight
        self.things=[]
        self.__weight=0


    def __check_weight(self,new_vol,old_vol=None):
        w=self.__weight+new_vol.weight if old_vol is None else self.__weight+new_vol.weight-old_vol.weight
        if w>self.max_weight:
            raise ValueError('превышен суммарный вес предметов')


    def check(self,k):
        if type(k)!=int or not(0<=k<=len(self.things)):
            raise IndexError('неверный индекс')


    def add_thing(self,thing:Thing):
        self.__check_weight(thing)
        self.things.append(thing)
        self.__weight+=thing.weight


    def __getitem__(self,item):
        self.check(item)
        return self.things[item]

    def __setitem__(self,key,value:Thing):
        self.check(key)
        t=self.things[key]
        self.__check_weight(value,t)        
        self.things[key]=value
        self.__weight+=(value.weight-t.weight)

    def __delitem__(self,item):
        self.check(item)
        t=self.things.pop(item)
        self.__weight-=t.weight


b = Bag(700)
b.add_thing(Thing('книга', 100))
b.add_thing(Thing('носки', 200))

try:
    b.add_thing(Thing('рубашка', 500))
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

assert b[0].name == 'книга' and b[0].weight == 100, "атрибуты name и weight объекта класса Thing принимают неверные значения"

t = Thing('Python', 20)
b[1] = t
assert b[1].name == 'Python' and b[1].weight == 20, "неверные значения атрибутов name и weight, возможно, некорректно работает оператор присваивания с объектами класса Thing"

del b[0]
assert b[0].name == 'Python' and b[0].weight == 20, "некорректно отработал оператор del"

try:
    t = b[2]
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"

    
b = Bag(700)
b.add_thing(Thing('книга', 100))
b.add_thing(Thing('носки', 200))

b[0] = Thing('рубашка', 500)

try:
    b[0] = Thing('рубашка', 800)
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError при замене предмета в объекте класса Bag по индексу"






