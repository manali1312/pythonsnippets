def double(n):
    return n + n

numbers = (1,2,3,4,5,6,7,8,9)
#result = map(double,numbers)
#rint(result)

doubleNums = []
for i in numbers:
    #doubleNums.append(double(i))
    r = double(i)
    doubleNums.append(r)
print(doubleNums)



