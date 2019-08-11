a = ['a','b','c','d']
def concatStr(l1,l2):
    return l1 + " " + l2 

ans = reduce(concatStr,a)
print(ans)