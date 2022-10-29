from operator import add

class Thing:
    def __init__(self,name, weight):
        self.name=name
        self.weight=weight


class Bag:
    def __init__(self,max_weight) -> None:
        self.max_weight=max_weight
        self.things=[]


    def add_thing(self,thing:Thing):
        a=sum(x.weight for x in self.things)
        if add(a,thing.weight)>self.max_weight:
            raise ValueError('превышен суммарный вес предметов')
        return self.things.append(thing)


    def check(self,k):
        if type(k)!=int or not(0<=k<=len(self.things)):
            raise IndexError('hj')


    def __getitem__(self,item):
        self.check(item)
        return self.things[item]

    def __setitem__(self,key,value):
        self.check(key)
        self.


bag = Bag(1000)
bag.add_thing(Thing('книга', 100))
# print(bag.things)
bag.add_thing(Thing('носки', 200))
bag.add_thing(Thing('рубашка', 500))
# bag.add_thing(Thing('ножницы', 300)) # генерируется исключение ValueError
print(bag[2].name) # рубашка
        






