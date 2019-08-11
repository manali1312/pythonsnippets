#power using for loop
def power(number,numOfPower=0):
    result = 1
    for p in range(1,numOfPower+1):
        result = result * number
    print(result)
    #print(number**numOfPower)

#find out power using while loop
def powerWhile(number,numOfPower):
    result = 1
    p = 1
    while p<= numOfPower:
        result = result * number
        p += 1
    print(result)

powerWhile(2,3)


'''
power(4)#=>1
power(4,1)#=>4
power(5,2)#=>25
power(4,2)#=>16
power(4,3)#=>64'''