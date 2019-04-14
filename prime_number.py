import sys
def is_prime(num):
        if(num==1 or num==0):
                return False
        for i in range(2,num):
            if (num%i==0):                
                return False
                break
        else:
            return True

'''
while True:
        num=int(input("a number or for exit enter -1 :"))
        if(num==-1):
                sys.exit(0)
        print("Number is prime: "+str(is_prime(num)))
'''        



