def isEven(num):
    if num%2 == 0:
        return True
    else:
        return False
listOfNum = [2,4,7,34,68,35]
listOfOddEven = map(isEven,listOfNum)
print(listOfOddEven)

listOfNum2 = [1,2,3,4,5]
def sqrNum(n):
    result = (n,n*n)
    return result
listOfSqr = map(sqrNum,listOfNum2)
print(listOfSqr)