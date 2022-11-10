class Record:
    def __init__(self,**kwargs) -> None:
        self.__dict=kwargs
        self.__len=len(kwargs)
        self.__dict_list=[*self.__dict.keys()]

    def __getitem__(self,item):
        if type(item)!=int or not (-self.__len<=item<=self.__len):
            raise IndexError('генерируется исключение IndexError')
        return getattr(self,self.__dict_list[item])

    def __setitem__(self,key,value):
        if type(key)!=int or not (-self.__len<=key<=self.__len):
            raise IndexError('генерируется исключение IndexError')
        return setattr(self,self.__dict_list[key],value)