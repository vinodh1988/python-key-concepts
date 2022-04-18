from metaprogramming import intercept

@intercept
def greetEveryone(name1,name2,name3):
    print("Hi ",name1)
    print("Hello ",name2)
    print("Hey ",name3)

@intercept
def add(a,b):
    return a+b

greetEveryone("Raju","Arjun","Kiran")
print("sum is ", add(345,53))