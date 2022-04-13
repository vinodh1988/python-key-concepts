def removeAll(list,element):
    count=0
    for x in list:
        if x==element:
            count+=1
    
    for x in range(0,count):
        list.remove(element)

list=[34,355,6,3545,645,355,355,34,535,65]
print(list)
removeAll(list,355)
print(list)