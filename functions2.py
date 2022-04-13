def listprocess(list,x,y,z):
    list.extend([x,y,z])

listx=[35,353,535,34,34,534,534]
print(listx)
listprocess(listx,24,53,35) #pass by reference
print(listx)

def stringProcess(name,appender):
    name+=appender
    print("within function",name)

firstname="rajan"
print(firstname)
stringProcess(firstname,"Krishna") #pass by value
print(firstname)