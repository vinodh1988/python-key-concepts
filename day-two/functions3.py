def fun():
    print("Funny function")

temp=fun

print(temp)
print(fun)
print(type(temp))
print(type(fun))
print(temp==fun)

temp()
#python is a functional language