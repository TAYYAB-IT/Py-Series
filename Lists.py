#List & Tuple

lis=[2,'tayyab']
lis.append(9.0)
print(lis)
num=[2,3,4,2]
#lis.append(num)
# print(lis[3])
#num.sort()
#print(num)
#num.reverse()
#print(num)
lis.insert(0,'Ali')
for x in range(0,len(num)):
    lis.append(num[x])
print(lis)
fl=[4,34,2,34]
lis.extend(fl)
print(lis)
tup=(1,'ajs',2,1,1)
print(tup)
tx=(2)
print(tx)
t=(1,)
print(t)
print(tup.count(1))
#Swaping
a,b=2,4
print(a,b)
a,b=b,a
print(a,b)