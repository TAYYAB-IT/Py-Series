#Multiple inheritance
class A:
    def __init__(self):
        print("A_Constructor")
    def fun_A(self):
        print("Class A")
class B:
    def __init__(self):
        print("B_Constructor")
    def fun_B(self):
        print("Class B")
class C(B,A):
    def __init__(self):         #In multiple ,it just print first inheriated class constructor (B)
        super().__init__()      # must add to call parent class instructor
        print("C_Constructor")
    def fun_C(self):
        print("Class C")
obj=C()
