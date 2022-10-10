class Deco:
    def __set_name__(self,owner,name):
        self.name=f'_{owner.__name__}__{name}'

    def __get__(self,owner,objtype):
        return getattr(owner,self.name)
    
    def __set__(self,instance,value):
        setattr(instance,self.name,value)


class Don:
    start=Deco()
    end=Deco()
    def __init__(self,start=None,end=None) :
        self.start=start
        self.end=end


class Lst:
    def __init__(self):
        self.obj_nachalo=None
        self.obj_konec=None

    def add(self,obj:Don):
        if self.obj_konec:
            self.obj_konec=obj.start
        obj.end=self.obj_konec
        self.obj_konec=obj
        if not self.obj_nachalo:
            self.obj_nachalo=obj
        

a1=Don()
a2=Don()
a3=Don()
a4=Don()
l=Lst()
l.add(a1)
print(l.n,l.f)
l.add(a2)
print(l.n,l.f)
l.add(a3)
print(l.n,l.f)
l.add(a4)
print(l.n,l.f)