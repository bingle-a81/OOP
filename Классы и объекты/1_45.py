class Deskr:
    def __set_name__(self, owner, name):
        self.name = f'_{owner.__name__}__{name}'

    def __get__(self, instance, owner):
        return getattr(instance,self.name)

    def __set__(self, instance, value):
        if type(value) not in (int,float,):
            raise TypeError('int or float')
        setattr(instance,self.name,value)



class TrackLine:
    to_x=Deskr()
    to_y=Deskr()

    def __init__(self,to_x=0, to_y=0, max_speed=0):
        self.to_x=to_x
        self.to_y=to_y
        self.__max_speed=max_speed

    @property
    def max_speed(self):
        return self.__max_speed
    @max_speed.setter
    def max_speed(self,value):
        if type(value) in (int):
            raise TypeError('int')
        self.__max_speed = max_speed



class Track:
    start_x=Deskr()
    start_y=Deskr()

    def __init__(self,start_x=0, start_y=0):
        self.start_x=start_x
        self.start_y=start_y
        self.__path=[TrackLine(self.start_x,self.start_y)]

    def add_track(self, tr:TrackLine):
        self.__path.append(tr)

    def get_tracks(self):
        return self.__path

    def __len__(self):
        g=((self.__path[i-1],self.__path[i]) for i in range(1,len(self.__path)))
        z=sum(map(lambda t: self.formula(t[0],t[1]), g))
        return z


    @staticmethod
    def formula(line0:TrackLine,line1:TrackLine):
        a=0.5
        # a=(line1.to_x - line0.to_x)
        # a=((line1.to_x - line0.to_x)**2+(line0.to_y - line1.to_y) ** 2)**0.5
        return a

track1, track2 = Track(), Track(0, 1)
track1.add_track(TrackLine(2, 4, 100))
track1.add_track(TrackLine(5, -4, 100))
track2.add_track(TrackLine(3, 2, 90))
track2.add_track(TrackLine(10, 8, 90))

print(len(track1))