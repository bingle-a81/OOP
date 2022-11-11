class RadiusVector:
    def __init__(self,*args) -> None:
        self.coords=list(args) if args else []

    def __getitem__(self,item):
        return tuple(self.coords[item]) if type(item)== slice else self.coords[item]

    def __setitem__(self,key,value):
        self.coords[key]=value