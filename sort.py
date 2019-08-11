a=[1,2,3,4,5]
str_a=['abc','lfe','igfg']

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