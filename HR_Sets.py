FirstSet = set([3,1])
SecondSet = set([5,1])
ArrayForSearch = [1,5,2]
count = 0

for num in ArrayForSearch:
    print(num)
    if num in FirstSet:
        count +=1
        print(count)
    if num in SecondSet:
        count -=1
        print(count)
print("Final count: ",count)

