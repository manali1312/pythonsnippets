n = 6
def sqr(n):
    r = n * n
    return r
listOfSqrs = [sqr(i) for i in range(1,n)]#using functions
print(listOfSqrs)

f = lambda x: x*x
lambdaList = [f(x) for x in range(1,n)]#using lambda function
print(lambdaList)