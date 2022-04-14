def outer(state):
    element=state
    print("element in outer ",element)
    def inner(data):
        inside = data
        print("element in inner", element)
        print("inside in inner", inside)
    inner("first Call")

    return inner
        
ref=outer("Strong")
ref("India")
ref("Japan")