from string import ascii_uppercase,ascii_lowercase
from random import choice

letters= ascii_lowercase+ascii_uppercase
filewrite= open('assignment.txt','w')

for i in range(0,100):
    line=''.join(choice(letters) for _ in range(0,25))
    line=line+'\n'
    filewrite.write(line)

filewrite.close()
