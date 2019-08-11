fileForRead = open("Result.txt",'r')

fileForWrite = open("outout.txt",'r+')
for l in fileForRead:
    fileForWrite.writelines(l)
    print(l)
fileForWrite.write("Hi....my name is MANALI")
#print (fileForRead.read(5))
print (fileForWrite.read())

fileForRead.close()
fileForWrite.close()