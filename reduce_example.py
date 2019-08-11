a=[1,2,3,4]
'''
def add(a,b):
    return a+b

ans = reduce(add,a)

print(ans)
'''
ans = 0
for i in a:
    ans = ans + i
print(ans)

