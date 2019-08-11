i = 1
j = 1
n = int(input("Enter a number: "))
print(i)
print(j)

for _ in range(1,n):
    r = j + i
    print(r)
    i = j
    j = r
