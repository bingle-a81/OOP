class SmartPhone:
    def __init__(self):
        pass


class Point:
    def __init__(self,pt):
        self.pt=pt

    @property
    def pt(self):
        return self.__pt

    @pt.setter
    def pt(self,pt):
        if type(pt)==int:
            self.__pt=pt

a=Point(10)
a.pt=100

print(a.pt)
