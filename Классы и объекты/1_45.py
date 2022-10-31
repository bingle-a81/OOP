class Cell:
    def __init__(self) -> None:
        self.is_free=True
        self.value=0

    def __bool__(self):
        return self.is_free

    def __repr__(self) -> str:
        return f'{self.value}'



class TicTacToe:
    def __init__(self) -> None:
        self.__n=3
        self.pole=tuple(tuple(Cell() for row in range(self.__n)) for col in range(self.__n))

    def clear(self):
        for row in self.pole:
            for i in row:
                i.is_free=True
                i.value=0

    def __repr__(self) -> str:
        for i in self.pole: 
            print(' '.join(list(map(str, i))))



# p=TicTacToe()
# print(TicTacToe())

pole=tuple(tuple('0' for row in range(2)) for col in range(2))
print(len(pole))

print (list(pole[i-1][i] for i in range(1,len(pole))))

# a=(0,0,0,0,)
# print(*a)