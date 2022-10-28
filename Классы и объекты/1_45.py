class Bot:
    def __init__(self,*args) :
        self.coords=list(*args)

    def __getitem__(self,item):
        return self.coords[item]

    def __setitem__(self,key,value):
        self.coords[key]=value

a=list(range(10))
d=Bot(a)
d[5]=10000
print (d.coords)
