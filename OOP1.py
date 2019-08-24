age = 10

class Student:
    def __init__(self,name,age=None,address=None):
        self.name = name
        self.age = age
        self.address = address
    
    def getDescription(self):
        if (self.age==None and self.address==None):
            print("Name is",self.name)
        else:
            print(self.name+" is "+str(self.age)+" years old and stays at "+self.address)

    def getAddress(self,addr):
        #print("Address is : Mumbai")
        #print(addr)
        pass
    
    def setAge(self,age):
        self.age= age

    def setAddress(self,address):
        self.address=address


student1 = Student("Manali",25,"Alibag")
print(student1.age)
#print(student1.getAddress("thane"))
student2 = Student("Mandar",25,"Thane")
student2.getDescription()

student3=Student("Pakya")
student3.getDescription()
student3.setAge(5)
student3.setAddress("Powai")
student3.getDescription()

student3.setAge(25)
student3.getDescription()
