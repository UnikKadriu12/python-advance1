class Animal():
    def __init__(self, name):
        self.name=name

    def sound(self):
        print("")

class Dog(Animal):
    def __init__(self,name,breed):
        super().__init__(name)
        self.breed=breed

    def sound(self):
        print("Hammm hamm")

    def humanFriendly(self):
        print("this dog is freindly")

class Cat(Animal):
    def __init__(self,name,color):
        super().__init__(name)
        self.color=color
    def sound(self):
        print("maju mjauuu")


animal34= Dog("licky","pitbull")
animal34532= Cat("sia","orange")


animal34.humanFriendly()
