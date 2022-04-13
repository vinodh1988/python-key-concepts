mylist=[1,235,34,54,356,364,43,43,356]

print(mylist)
print(mylist[1:3])
print(mylist[0:3])
print(mylist[3:])
print(mylist[::])
print(mylist[1:6:2])
print(mylist[1::2])
print(mylist[9::-1])
print(mylist[9:5:-1])

mylist.sort()
print(mylist)
mylist.sort(reverse=True)
print(mylist)

#list is mutable
mylist.insert(3,15050)
print(mylist)

mylist.remove(43)
print(mylist)

mylist.extend([43,35,64])
print(mylist)