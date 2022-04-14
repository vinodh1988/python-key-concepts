def outer(state):
    element=state
    print("element in outer ",element)
    def inner(data):
        inside = data
        nonlocal element
        element= "Test String"
        print("element in inner", element)
        print("inside in inner", inside)
    inner("first Call")
    print("element in outer ",element)
    return inner
        
ref=outer("Strong")
