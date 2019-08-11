def factorial(n):
    r = 1
    for i in range(1,n+1):
        r = i * r
    #print(r)
    return r

def recursiveFactorial(n):
    if(n==1):   
        return 1
    else:
        return n*recursiveFactorial(n-1)



n = int(input("Enter a number"))
result = recursiveFactorial(n)
print(result)