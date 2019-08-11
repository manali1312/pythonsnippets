from sys import argv
a = argv[0]
b = argv[1]
'''
temp = a
a = b
b = temp
'''
a,b = b,a

print("a: ",a)
print("b: ",b)