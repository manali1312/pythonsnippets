fileForRead = open('sample.txt','r')
fileForWrite = open('result.txt','w')
for line in fileForRead:
    tempLine = line
    wordList = tempLine.split(" ")
    fileForWrite.writelines(wordList)
    '''for word in wordList:
        fileForWrite.write(word+"\n")'''

fileForWrite.close()
fileForRead.close()
