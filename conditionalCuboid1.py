n = 2
cuboid = [(i,j,k) for i in range(0,n+1) for j in range(0,n+1) for k in range(0,n+1) if(i+j+k!=n)]
'''
for i in range(1,n+1):
    for j in range(0,n+1):
        for k in range(0,n+1):
            if(i+j+k!=n):
                cuboid.append((i,j,k))
                '''
print("cuboid=",cuboid)