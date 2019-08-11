seq=[1,2,3,4,5,6,7,8,9]
even = []
for i in seq:
    if i%2==0:
        even.append(i)
    else:
        print("Number is odd: ",i)
print(even)

def isEven(num):
    return num%2==0

result= filter(isEven,seq)
print(list(result))
