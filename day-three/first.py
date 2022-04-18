class  Parent:
    def __init__(self,name="NoName"):
        self.name =  name 
    
    def show(self):
        print(self.name," is the name of the father")


class  Child(Parent):
    def __init__(self,fname ,name, toyname):
        self.cname = name
        super().__init__(fname)
        self.toyname=toyname

    def show(self):
        super().show()
        print(self.cname," is the name of the child")
        print(self.toyname," is the toyname of the child")


firstchild=Child("Ganesh","Robin","Elephant")
firstchild.show()
#firstchild.show()
