import datetime as dt
x=dt.datetime.now()
y=dt.datetime(x.year,x.month,x.day)
print(y)
#x=str(x.day)+"-"+str(x.month)+"-"+str(x.year)
#print(x)
#print(y.strftime("%A"))     #Weekday Full name
#print(y.strftime("%a"))     #Weekday short name
#print(y.strftime("%B"))     #Month Full name
#print(y.strftime("%b"))     #Month Short name
#print(y.strftime("%Y"))     #Year Full(2021)
#print(y.strftime("%y"))     #Year just (21)
#print(y.strftime("%p"))     #Pm/Am
#################JSON#################################
#import json
#Student={
#    "Name":"Tayyab Aman",
#    "Batch":"19th",
#    "Roll#":"19014156-018",
#    "Marks":(24,22,19,20)
#}
#x=json.dumps(Student)    #Convert to JSON
#print("JSON Encoded = ",x)
#y=json.loads(x)          #Convert from JSON to noraml
#print("After JSON Decoded = ",y)
#from exception import exception
#########Exceptation Handling###########
#try:
#    print(9/0)
#except:
#    print("Division By 0")
