class Cell:
    def __init__(self) -> None:
        self.is_free=True
        self.value=0

    def __bool__(self):
        return self.is_free

class TicTacToe:
    def __init__(self) -> None:
        self.pole=tuple(tuple(Cell() for i in range(3)) for i in range(3))

    def clear(self):
        for row in self.pole:
            for cell in row:
                cell.is_free=True
                cell.value=0

    def __check(self,v):
        if type(v)!=tuple or len(v) !=2:
            raise IndexError('неверный индекс клетки')
        if any(not(0<=x<=3) for x in v if type(x) !=slice):
            raise IndexError('неверный индекс клетки')
    
    def __setitem__(self,key,value):
        self.__check(key)
        r,c=key
        if self.pole[r][c]:
            self.pole[r][c].value=value
            self.pole[r][c].is_free=False
        else:
            raise ValueError('клетка уже занята')
    
    def __getitem__(self,item):
        self.__check(item)
        r,c=item
        if type(r)==slice:
            return tuple(self.pole[x][c].value for x in range(3))
        if type(c)==slice:
            return tuple(self.pole[r][x].value for x in range(3))
        return self.pole[r][c].value

game = TicTacToe()
game.clear()
game[0, 0] = 1
game[1, 0] = 2
# формируется поле:
# 1 0 0
# 2 0 0
# 0 0 0
game[2, 2] = 2 # генерируется исключение IndexError
if game[0, 0] == 0:
    game[0, 0] = 2
v1 = game[0, :]  # 1, 0, 0
v2 = game[:, 0]  # 1, 2, 0
