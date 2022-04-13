def extendList(lista,index,listb):
    current=index
    for x in range(0,len(listb)):
        lista.insert(current,listb[x])
        current+=1

listx=[1,2,3,4,5]
listy=[20,30,40,34,53]

print(listx)
extendList(listx,4,listy)

print(listx)