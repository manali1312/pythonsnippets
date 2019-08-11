import math
a = int(input("a="))
b = int(input("b="))

#in python 3, 10/3 is 3.33333333333 and in python 2, 10/3 is 3
# that is why we have used // here in python 3 for complete number
# and for float value we have used fload function.
 
d = a//b
fd = float(a/b)

print("division = ",d)
print("float division =",fd)