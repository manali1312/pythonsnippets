def student(name):
    marks = {"manali":(88,78,89),"utkarsha":(98,72,91),"devang":(71,72,94),"sohini":(89,82,78)}
    if name in marks:

        markes_new = marks.get(name)
        print(markes_new)
        result = 0
        for num in markes_new:
            result += num
        print(result)
        average = result / 3
        print(name,"'s average marks are: ",average)
    else:
        print(name+" :student name is not present in the list")
    
student("manali")
student("mandar")