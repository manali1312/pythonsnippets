sampleList = [1,2,2,6,7,8,8,9,0,10,2,0]
'''#using sets
sampleSet = set()
for number in sampleList:
    sampleSet.add(number)

print(sampleSet)'''
sampleList.sort()
listLen= len(sampleList) 
result = []
result.append(sampleList[0])

for index in range(1,listLen):
    if sampleList[index] != sampleList[index-1]:
        result.append(sampleList[index])
'''for index,value in enumerate(sampleList):
    print(index,value)
'''
#using sort

print(sampleList)
print(result)