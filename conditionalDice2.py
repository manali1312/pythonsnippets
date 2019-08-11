n = 6
dice=[]
'''
dice = [[(i,j) for j in range(1,n+1)] for i in range(1,n+1)]
faces = []
'''

for i in range(1,n+1):
    faces = []
    for j in range(1,n+1):
            faces.append((i,j))
    dice.append(faces)
print(dice)