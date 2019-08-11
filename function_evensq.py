import copy
seq=[1,2,3,4,5,6,7,8,9]
def isSqrEven(num):
    sqr = num**2
    return sqr%2==0

ans = filter(isSqrEven,seq)
print(list(ans))

#using list comprehension
ansListComp = [i for i in seq if isSqrEven(i)==True ]
print(ansListComp)


ans2=[]
for i in seq:
    if(isSqrEven(i)):
        ans2.append(i)


num=10
def fn():
    print(num)

fn()


a=[1,7]
b=copy.deepcopy(a)
b[0]=7



'''
a=1
b=a
b=7
'''

print(a,b)
