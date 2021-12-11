class student:
    school="UOG"          #class variable
    def __init__(self,m1,m2,m3):
        self.m1=m1            #instance variable
        self.m2=m2            #instance variable
        self.m3=m3            #instance variable
    def avg(self):
        return (self.m1+self.m2+self.m3)/3
    @classmethod                   #decorator
    def info(self):                #class method can access only class variables
        return self.school
    @staticmethod                  #decorator
    def show():
        print("I am Student") #staticmethod cannot access any class attribute
std1=student(30,20,10)
print(std1.avg())
print(std1.info())
std1.show()
