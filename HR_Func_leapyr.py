def leapYear():
    year = int(input("Enter an year:"))
    if year%4==0 or year%400==0:
        if year%100==0 and year%400!=0:
            print("Not a leap year")
        else:
            print("It is a leap year")   
    else:
        print("This is not a leap year")

if __name__ == '__main__':
    leapYear()


    