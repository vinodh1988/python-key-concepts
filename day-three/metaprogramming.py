from functools import wraps

def intercept(target):
    def inner(*args,**kwargs):
        print("interceptor logic is working")
        print("intercepted and have access to paramters")
        print(args,kwargs)
        x=target(*args,**kwargs)
        print("Done Interception")
        return x
        
    return inner

def interceptor(name,type):
    def wrapper(fun):
        @wraps(fun)
        def inner(*args,**kwargs):
            print("Intercepting")
            print("parameters passed for interceptor name: {} type:{}".format(name,type))
            fun(*args,**kwargs)
            print("interception complete")
        return inner
    return wrapper

