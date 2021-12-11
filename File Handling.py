class computer:
    def __init__(self,cpu,ram,hd):
        self.cpu=str(cpu)+" GHz"
        self.ram=str(ram)+" GB"
        self.hd=str(hd)+ " GB"
com1=computer(2.3,4,200)
com2=computer(2.4,6,400)
com3=computer(2.7,8,280)
import os
if(os.path.exists("Computer_Lab.txt")):
    pass
else:
    f=open("Computer_Lab.txt","x")
    f.close()
#Write in File
f=open("Computer_Lab.txt","a")
f.write(f"({com1.cpu},{com1.ram},{com1.hd})\n")
f.write(f"({com2.cpu},{com2.ram},{com2.hd})\n")
f.write(f"({com3.cpu},{com3.ram},{com3.hd})\n")
f.close()
 #Read File
f=open("Computer_Lab.txt","r")
for i in f:
    print(i)
f.close()