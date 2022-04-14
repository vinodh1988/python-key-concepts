class Person:
    def __init__(self,sno=-1,name="noname"):
        self.sno=sno
        self.name=name

    def show(self):
        print(self.sno,"  ",self.name)

    def __repr__(self):
        return "{} and {}".format(self.sno,self.name)
  


person1=Person(12,"Rajan")
person2=Person(13,"Ramesh")
person3=Person()
person4=Person(15)
person5=Person(name="Store")

person1.show()
person2.show()
person3.show()
person4.show()
person5.show()

print(person1)
print(person2)




#functions with __ at either end are called as
# magic methods or dunder methods
# each of this methods has some special meaning that
# __init__ means constructor