max_list = ["a","cncdh","eh","fle","dlop"]
max_tuples = [(1,5),(2,4),(8,5)]
result = max_list[0]
def max(i,j):
    if (i<j):
        return j
    return i

for num in max_list:
    result = max(num,result)
print(result)

def returnLen(text):
    return len(text)
'''
#sorts by string length
max_copy= sorted(max_list,key=returnLen)
print(max_list)
print(max_copy)
'''

def returnSec(entry):
    return entry[1]
sorted_tuple = sorted(max_tuples,key=returnSec,reverse=True)
print(sorted_tuple)
