# classes and objects 
# data members - class variables, member functions - class functions 
# constructor - 

class Student:
    # def __init__(self,n,r):
    # def __init__(self, n=10,r=5): # default Paramters or arguments
    def __init__(self):
        # print("Hello Constructor")
        pass
        # self.naam= n
        # self.roll=r 
        # # print(n,r)
        # # print(self)
        # print(self.naam, self.roll)
    def getValues(self):
        self.naam= input("Enter Name ")
        self.roll= input("Enter RollNo ")
        
    def printValues(self):        
        print("Name is",self.naam,"rollno is",self.roll)


stu1= Student()
stu2= Student()

stu1.getValues()
stu2.getValues()

stu2.printValues()



# print(stu1)
# stu1= Student('Nikhil',123)
# stu1= Student('Ansh',23)