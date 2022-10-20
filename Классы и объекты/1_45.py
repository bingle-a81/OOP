class Integer:
    def __init__(self,start_value):
        self.start_value=start_value
        self.__value=value

    @property
    def value(self):
        return self.__value
    @value.setter
    def value(self,v):
        if type(v) != int:
            raise ValueError('должно быть целое число')
        self.__value=v

class Array:
    def __init__(self,max_length, cell:Integer):
        self.max_length=max_length
        self.cell=cell
        self.ar=[]

    def __check(self,v):
        if type(v) != int or not (0<v<self.max_length):
            raise IndexError('неверный индекс для доступа к элементам массива')


    def __getitem__(self, item):
        if self.__check(item):
            return self.ar.