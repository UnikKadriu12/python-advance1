from codecs import namereplace_errors


class Dong:
    def __init__(self,name):
        self.name=name

    def sound(self):
        print(f"{self.name} makes the sound woof")


class Cat:
    def __init__(self,name):
        self.name = name

    def sound(self):
        print(f"{self.name} make the sound mjauuu")


class Bird:
    def __init__(self,name):
        self.name = name

    def sound (self):
        print(f"{self.name} make the sound ciu ciu")


dog = dog("haski")
cat = cat("haiii")
bird = bird("twiti")

for animal in (dog,cat,bird):
    animal.sound()
