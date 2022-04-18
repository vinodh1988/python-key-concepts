from metaprogramming import interceptor

@interceptor(name="India",type="function")
def simplefun(x,y):
    print("x: {}, y: {}".format(x,y))

simplefun("Ram","Rahim")