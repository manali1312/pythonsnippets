a = 30
b =50
c = 20

def max(i,j):
    if (i<j):
        return j
    return i
'''       
if (a<b):
    max = b
if (max<c):
    max = c
print("max no is:",max)
    
'''
val=max(max(a,b),c)
print(val)
