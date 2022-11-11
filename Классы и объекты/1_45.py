r,c=5,5
matrix=[[0 for x in range(c)] for y in range(r)]

dx,dy,x,y=0,1,0,0

for i in range(1,r*c+1):
    matrix[x][y]=i
    if matrix[(dx+x)%r][(dy+y)%c]:
        dx,dy=dy,-dx
    x+=dx
    y+=dy

for line in matrix:
    print(*(f'{i:<3}' for i in line), sep='')
    