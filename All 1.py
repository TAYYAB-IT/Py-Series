#               STrings
#print("Tayyab's Laptop")
#print('Navin\'s "Laptop"')
#print("Tayyab "*4)
#print("C:\docs\\navin")
#a="Hello"
#a+=" Tayyab"
#print(a)
#print("First Character is ",a[0])
#print("Last Character is ",a[-1])
#print(a[1:4])    # CHracter from index 1 to (4-1) index
#print("Length of String 'a' is ", len(a))

#            Lists
nums=[2,1,0,3,6]
#print(nums[0])
#print(nums[:4])
#val=['9.5',True,'Tayyab',4]
#print(val,"Length::", len(val))
#x=[nums,val]
#print(x," Length::",len(x))
#nums.sort()
#print(nums)
#nums.extend([7,8,9,7])
#nums.append(90)
#print(nums)
#nums.sort()
#print(nums)
#             Tuple :we cannot change value
#tup=(2,3,14,25,3,1)
#print(tup[1])
#tup[1]=33 not possible
#print(tup.count(3))
#print(tup.index(25)) #if value is not in tuple so error will occur
#tp=("hello","qaim")
#print(tp[0])
#             Set::It does not arrange numbers in a proper sequence. It will not support duplicate values
#set={22,4,33,2,44,4}
# set[0] not allowed
#print(set)
#It support set operations
#              Dictionary
#data={1:'Ali',2:'Qasim',3:'Tayyab'}
#print(data[2])
#print(data[1])   #if key not found it cause an error
#print(data.get(4,"Not Found")) #in order if value not found so get method is better
keys=[1,2,3,4,5] #String keys also possible
values=['python','java','php','c++','Kotlin']
d=dict(zip(keys,values))
#print(d)
print(d.values())
#x=list(d.keys())
#print(x)
#d['last']='C'
#print(d)
#print(len(d))
#del d[2]  #in order to delete an entry
#print(d)
#Inside in Dictionary
#d={'JS':'ATOM','CS':'VS','Python':['Pycharm','Sublime'],'JAVA':{'JSE':'Netbeans','JEE':'Eclipse'}}
#print(d['Python'][0]) #List in Dictionary
#print(d['JAVA']['JEE']) #Dictionary in an Dictionary