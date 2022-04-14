def willCallYouBack(cb):
    print("Started working")
    cb("INDIA")
    print("Still in fun")
    cb("CHINA")
    print("and Still in fun")
    cb("RUSSIA")
    print("and and Still in fun")
    cb("MONGOLIA")
    print("Wrapped it")

def processIt(data):
    print("Received ",data)

willCallYouBack(processIt)

# A function which is passed as paramter to another function is called callback