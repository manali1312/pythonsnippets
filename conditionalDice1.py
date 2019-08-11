n = 6
dice = [(i,j) for i in range(1,n+1) for j in range(1,n+1) if(i+j>=6)]
'''
for i in range(1,n+1):
    for j in range(1,n+1):
        if(i+j>=6):
            dice.append((i,j))
            '''
print("dice=",dice)