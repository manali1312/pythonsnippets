strings = "AAAVSSSSHHDDDDDYYYYYYYYWWSD"
frequencyMap = {}
for l in strings:
    if l in frequencyMap:
        frequencyMap[l] += 1
    else:
        frequencyMap[l] = 1

for keys,values in frequencyMap.items():
    print(keys," ",values)
print(frequencyMap.items())

tupleList = [('A',1),('B',3)]
tupleList.append(('c',4))

for ele,val in tupleList:
    print(ele,val)