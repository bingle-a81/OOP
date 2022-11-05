lst_1 = [1, 2, 3]
lst_2 = [4, 5, 6]
# Упаковка двух списков вместе
zipped = list(zip(lst_1, lst_2))
print(zipped)
# [(1, 4), (2, 5), (3, 6)]
# Обратная распаковка списков
lst_1_new, lst_2_new = zip(*zipped)
print(list(lst_1_new))
print(list(lst_2_new))

f=[(1,2,3,4),(1,2,3,4),(1,2,3,4)]
a,b,c,d=zip(*f)

print(a,b,c,d)