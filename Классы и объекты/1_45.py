class Fu:
    _isinctace=None
    def __new__(cls,*args,**kwargs) :
        if cls._isinctace is None:
            cls._isinctace=super().__new__(cls)
        return cls._isinctace