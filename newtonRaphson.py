import math
Zold=1.0
Znew=Zold
x=4.0
while True:
    Znew = Zold- ((Zold**2-x)/2*Zold)
    if(abs(Zold-Znew)<0.00001):
        break
    else:
        Zold = Znew

print(Znew,math.sqrt(4))
