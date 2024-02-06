class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def bark(self):
        print(self.name +" bark bark")


d = Dog("Fido",3)
# print(d.get_name())
print(d.bark())

c= Dog("Spot",5)

print(c.bark())