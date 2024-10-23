class Animal:
  def __init__(self, name, age):
    self.name = name
    self.age = age

class Lion:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def info(self):
        print(f"I am a lion. My name is {self.name}. I am {self.age} years old.")
    def make_sound(self):
        print("Meow")

class Elephant:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def info(self):
        print(f"I am a elephant. My name is {self.name}. I am {self.age} years old.")
    def make_sound(self):
        print("uuuuu")

lion = Lion("Kitty", 2.5)
lephant = Elephant("Fluffy", 4)
animal = Animal('animal',123)
# def introduce_animal(animal):
for animal in (lion, lephant):
    animal.make_sound()
    animal.info()
