def largestKeyFirstOccurance(map):
    keys=list(map.keys())
    largest=keys[0]

    for x in range(1,len(keys)):
        if(len(largest)<len(keys[x])):
            largest=keys[x]

    return largest

dict={"sno":1,"name":"Rahul","city":"Chennai","desig":"Manager","age":22}
dict2={"industry":"IT","Experience":" 9 years","Strength":"High"}
print(largestKeyFirstOccurance(dict))
print(largestKeyFirstOccurance(dict2))