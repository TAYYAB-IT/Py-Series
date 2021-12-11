#add=lambda x,y:x+y
#square=lambda x:x**2
#print(f"sum={add(2,4)}")
#print(f"Square={square(3)}")
# Filter
#def fun(n):
#    return n%2==0
#nums=[2,3,4,5,6,88,89]
#result=tuple(filter(fun,nums))
#print(result)
#Filter -Lambda
#nums=[2,3,4,5,6,88,89]
#result=tuple(filter(lambda n:n%2==0,nums))
#print(result)
#Map-Lambda
#nums=[2,3,4,5,6,88,89]
#result=tuple(map(lambda n:n*2,nums))
#print(result)
#Reduce-Lambda
#from functools import reduce
#nums=range(1,10,1)
#result=int(reduce(lambda a,b:a+b,nums))
#print(result)

##########Decoratores###########
#def diff(x,y):
#    print(x,y)
#    print(x-y)
#def smart_diff(func):
#    def inner(a,b):
#        if(a<b):
#            a,b=b,a
#        return func(a,b)
#    return inner
#diff=smart_diff(diff)
#diff(6,9)