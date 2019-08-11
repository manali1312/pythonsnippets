numTopReverse = 12345
result = 0
while numTopReverse != 0:
    lastNum = numTopReverse % 10
    result = (result * 10) + lastNum
    numTopReverse = int(numTopReverse / 10)

print(result)