def prime(num):
    valid=True
    for x in range(2,int(num/2)+1):
        if(num%x==0):
            valid=False
            break
    return valid

listx=[12,14,13,17,19,21,23,15,26,29,31]
result=filter(prime,listx)
print(list(result))