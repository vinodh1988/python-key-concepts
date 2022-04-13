def evenFilter(lista):
    listb=[]
    for x in lista:
        if x%2==0:
            listb.append(x)
    return listb

listn=[3,356,34,5,344,131,352,353,353,5623,353,622]
print(evenFilter(listn))