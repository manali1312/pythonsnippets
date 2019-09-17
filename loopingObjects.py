from sys import exit
class Student:
    def __init__(self):
        self.name = None
        self.rollNo = None
    
    def getDetails(self):
        self.name=input('name:')
        self.rollNo=int(input('roll no:'))
    
    def displayDetails(self):
        print("Name is:",self.name," roll no is:",self.rollNo)

studentsList=[]
count = 1
while True:
    print("Enter details for student ",count)
    student = Student()
    student.getDetails()
    studentsList.append(student)
    selection = input("select q to quit or any other key to continue: ")
    if(selection is 'q' or selection is 'Q'):
        #print all student records entered till this point
        print("Records entered till now")
        for soleStudent in studentsList:
            soleStudent.displayDetails()
        exit(0)
    count += 1
    

       