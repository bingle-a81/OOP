class Clock:
    def __init__(self,h,m,s) -> None:
        self.hour=h
        self.minute=m
        self.second=s

    def get_time(self):
        return sum(x for x in [self.hour*3600,self.minute*60,self.second])


class DeltaClock:
    def __init__(self,cl1:Clock,cl2:Clock) -> None:
        self.clock1=cl1
        self.clock2=cl2

    def __len__(self):
        res=self.clock1.get_time-self.clock2.get_time
        return res if res>0 else 0

    def __repr__(self) -> str:
        d=self.__len__()
        h=d//3600
        m=d%3600//60
        s=d%3600%60
        return f'{h:02}:{m:02}:{s:02}'


c=Clock(1,2,3)
print(c.get_time())