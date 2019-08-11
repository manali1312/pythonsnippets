fileForRead = open("assignment.txt",'r')
fileForWrite = open("assignment_result.txt",'w')
freqMap = {}
'read = fileForRead.read()'
''' #Manali's first attempt
for l in read:
    if l in freqMap:
        freqMap[l] += 1
    else:
        freqMap[l] = 1
'''
for line in fileForRead:
    for word in line:
        if word in freqMap:
            freqMap[word] += 1
        else:
            freqMap[word] = 1

#print(freqMap.items())

for keys,values in freqMap.items():
    print(keys+" "+str(values)+"\n")
    if keys == " ":
        fileForWrite.write("space"+" "+str(values)+"\n")
    elif keys == "\n":
        fileForWrite.write("new line character"+" "+str(values)+"\n")
    else:
        fileForWrite.write(keys+" "+str(values)+"\n")




fileForRead.close()
