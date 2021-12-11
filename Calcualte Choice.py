from time import sleep
while(1):
   x=float(input("1st::"))
   y=float(input("2nd::"))
   ch=int( input("1). Add\n2). Subtract\n3). Division\n4). Multiply\n Enter Choice::"))
   sleep(5)
   if(ch==1):
    print(f"Add::{x} + {y}==",x+y)
   elif(ch==2):
    print(f"Subtrat::{x} - {y}==", x - y)
   elif(ch==3):
    print(f"Division::{x} / {y}==", x / y)
   elif(ch==4):
    print(f"Multiply::{x} * {y}==", x * y)
   sleep(5)