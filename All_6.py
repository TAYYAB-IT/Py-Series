#print(__name__)
#print("Hello ",__name__)
class computer:
    def __init__(self,cpu,ram,hd):
        self.cpu=str(cpu)+" GHz"
        self.ram=str(ram)+" GB"
        self.hd=str(hd)+ " GB"
    def show(self):
     print(f"CPU::{self.cpu} , RAM::{self.ram} ,HD={self.hd}")
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%% Computer LAB %%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
total=int(input("How many Computers are in LAB::"))
All_comp=[]
for i in range(0,total,1):
    print(f"\nCOMPUTER # {i+1}")
    comp=computer(float(input("CPU::")),int(input("RAM::")),int(input("HD::")))
    All_comp.append(comp)
print("\n\n%%%%%%%%%%%%%%%%%%%%%%%%%%%%% Computers LIST %%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n\n")
for x in All_comp:
    x.show()
