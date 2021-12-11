#def add(a,b):
#    return (a+b,a-b)

#a=int(input("Enter value of 'a'::"))
#b=int(input("Enter value of 'b'::"))
#x,y=add(a,b)
#print(f"Sum ({a}+{b})={x}\nDifference({a}-{b})={y}")
#def show(name,age=18):
#    print(name,age)
#show("Tayyab")
#show("Tayyab",20)
#show(name="Ali",age=12)
#show(name="Qasim",14) # Cause error
#show(age=12,name="Haider")
#show(name="Qasim")
#show("Tayyab",age="13")# noww the type will be string of age
# *args
#def show(*b):  # Unlimited Parameters create tuple of parameters
#    print(b)
#    print(type(b))
#    for i in b:
#        print(i)
#show(2,4,"Haider",2.03)
#**Kwargs
#def person(**p): # for making dictionary actual parameter variable name as keys & variable value as its value
#    for keys,values in p.items():
#        print(keys,"=",values)
#    print(type(p))
#person(name="Umar",Age=12)
#############################
#def myFun(arg1, arg2, arg3):
#    print("arg1:", arg1)
#    print("arg2:", arg2)
#    print("arg3:", arg3)

# Now we can use *args or **kwargs to
# pass arguments to this function :
#args = ("Geeks", "for", "Geeks")
#myFun(*args)
#kwargs = {"arg1": "Geeks", "arg2": "for", "arg3": "Geeks"}
#myFun(**kwargs)
#a=4           #Global
#def fun():
#    a=3       #Local
#    print(a)   #3
#fun()
#print(a)     #4
#a=4
#def fun():
#    global a
#    a=5    #Will use Global
#fun()
#print(a)  #5 (AS value changed)
#a=4
#def fun():
#    a=3
#    globals()['a']="Hello"  # will access global variable
#    print(a)  #will print local variable
#fun()
#print(a)     #Hello
