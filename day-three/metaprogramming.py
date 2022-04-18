def intercept(target):
    def inner(*args,**kwargs):
        print("interceptor logic is working")
        print("intercepted and have access to paramters")
        print(args,kwargs)
        x=target(*args,**kwargs)
        print("Done Interception")
        return x
        
    return inner


