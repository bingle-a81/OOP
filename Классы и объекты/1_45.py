class Cell:
    def __init__(self) -> None:
        self.is_free=True
        self.value=0

    def __bool__(self):
        return self.is_free

    def __repr__(self) -> str:
        return str(self.value)

class TicTacToe:
    def __init__(self) -> None:
        self._len=3
        self.pole=tuple(tuple(Cell() for x in range(self._len)) for y in range(self._len ))
        print(self.pole)

    def clear(self):
        for row in self.pole:
            for i in row:
                i.is_free=True
                i.value=0

    def __cheak(self,v):
        if type(v)!=tuple or len(v)!=2:
            raise IndexError('неверный индекс клетки')

        if any(not(0<=x<=self._len) for x in v if type(v)!=slice):
            raise IndexError('неверный индекс клетки')


    def __setitem__(self,key,value):
        self.__cheak(key)
        row,col=key
        if self.pole[row][col]:
            self.pole[row][col]=value
            self.pole[row][col].is_free=False
        else:
            raise ValueError('клетка уже занята')

    def __getitem__(self,item):
        self.__cheak
        row,col=item
        if type(row)==slice:
            return tuple(self.pole[x][col].value for x in range(self._len))
        if type(col)==slice:
            return tuple(self.pole[row][x].value for x in range(self._len))
        return self.pole[row][col].value





game=TicTacToe()