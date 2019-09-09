class Animals:
    def __init__(self,animalName,animalType,numOflegs):
        self.animalName = animalName
        self.animalType = animalType
        self.numOflegs = numOflegs

    def animalInfo(self):
        print(self.animalName,": Animal type is ",self.animalType," which has ",self.numOflegs,"legs") 

    def getNumOfLegs(self):
        print("Number of legs are: ",self.numOflegs)
#to overwrite animal name or set values if None
    def setAnimalName(self,animalName):
        self.animalName = animalName

animal = Animals(None,"mammal",4)
animal.animalInfo()
legs = Animals("human","mammal",2)
legs.getNumOfLegs()
animal.setAnimalName("Cat")
animal.animalInfo()