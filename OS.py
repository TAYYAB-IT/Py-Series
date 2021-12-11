import os
currunt_dir=os.getcwd()
print(currunt_dir)
chkfile=os.path.isfile("All 5.py")
print(chkfile)
list_file=list(os.listdir())
print(list_file)
file=open(f"{os.path.join(currunt_dir,'Computer_Lab.txt')}",'r')
change=os.path.join(currunt_dir,"New for os")
z=open(change+"/new",'w')
for i in file:
    z.write(i)
file.close()
z.close()

