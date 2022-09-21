from functools import reduce

items = [10, 20, 30, 40, 50]
print(reduce(lambda x,y: x + y, items))