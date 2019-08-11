sampleMap={'manali':1,'mandar':0}
'''if 'mandar' in sampleMap:
    print("here")
    val=sampleMap.pop('mandar')
'''
sampleMap['manali'] += 1
sampleMap['shubham'] = 0

for key,value in sampleMap.items():
    print(key+" "+str(value))

#print(sampleMap['manali'])



