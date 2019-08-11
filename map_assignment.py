#ip [1,2,3,4]
#op [(1,1),(2,4),(3,9),(4,16])]

ip=[1,2,3,4]

emptyListout=[]

for i in ip:
    r = i**2
    emptyListin=(i,r)
    #emptyListin.append(r)
    emptyListout.append(emptyListin)

print(emptyListout)
