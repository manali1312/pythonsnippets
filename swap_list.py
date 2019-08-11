a = [1,2,3,4,5,6,7,8,9]

b = a[8]
a[8] = a[0]
a[0] = b
'''
i = a[0]
j = a[8]
print(i,j)
temp = i
i = j
j = temp
print(i,j)
'''
print(a)