stringToReverse = "MANALI"
length = len(stringToReverse)
stringList = []
#reverse using for loop
for i in range(1,length+1):
    print(stringToReverse[-i])

#reverse using swap
'''for letter in stringToReverse:
    stringList.append(letter)
print(stringList)'''
#stringList = list(stringToReverse)
stringList = [letter for letter in stringToReverse]
print(stringList)
for index in range(0,int(length/2)):
    result = stringList[index] 
    stringList[index] = stringList[length - index -1]
    stringList[length - index -1] = result

result = ("".join(stringList))    
print(result)