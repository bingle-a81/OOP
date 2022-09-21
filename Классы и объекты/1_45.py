# import random
# import string
# def d(lst:list):
#     a=len(lst)-1
#     return lst[random.randint(0,a)]

# lst1=[i for i in map(int,string.digits)]
# a=len(lst1)-1
# b=[d(lst1) for i in lst1]
# b2=[lst1[random.randint(0,a)] for i in lst1]
# print(b)
# print(b2)
 
# b3=list(zip(b,b2))
# print(b3)

s2=[1, 9, 8, 1, 4, 6, 2, 9, 8, 2]
s1=[1, 4, 2, 0, 8, 9, 1, 6, 8, 8]
s3=list(zip(s2,s1))
print(s3)