class HH:
    id=0
    def __init__(self):
        self.__class__.id+=1
        self.id=self.__class__.id