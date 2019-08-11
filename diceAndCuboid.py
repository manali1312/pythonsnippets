n = 6
dice = []
for i in range(1,n+1):
    for j in range(1,n+1):
        dice.append((i,j))
print("dice=",dice)
cuboid = []
for i in range(1,n+1):
    for j in range(1,n+1):
        for k in range(1,n+1):
            cuboid.append((i,j,k))
print("cuboid=",cuboid)