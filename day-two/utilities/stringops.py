def reverse(data):
    result=''
    for x in reversed(range(len(data))):
        result+=data[x]
    return result