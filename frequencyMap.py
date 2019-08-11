fileForRead = open("assignment.txt",'r')
fileForOpen = open("result_Map_Frequency.txt",'w')

freq = {}
text = fileForRead.read()
for letter in text:
    if letter in freq:
        freq[letter] +=1
    else:
        freq[letter] = 1

for keys,values in freq.items():
    fileForOpen.write(keys+str(values)+"\n")

