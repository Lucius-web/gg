# class Vechile:
#   def __init__(self, name_brand, model, year):
#     self.name_brand = name_brand
#     self.model = model
#     self.year = year

#   def start(self):
#     print("Вы начали ехать")

#   def stop(self):
#     print("Вы остановились")

#   def starter(self):
#     top = int(input("Если вы хотите ехать нажмите 1. Если вы хотите остановиться нажмите 2: "))
#     if top == 1:
#       self.start()
#     elif top == 2:
#       self.stop()
#     else:
#       print("Ошибка")

#   def info(self):
#     print(f"Название бренда - {self.name_brand}, Модель - {self.model}, Год выпуска - {self.year}")

# vechile = Vechile('Fix', 'Спортивный', '2019')

# vechile.info() 
# vechile.starter()

# class Car(Vechile):
#   def __init__(self, name_brand, model, year, doors):
#     super().__init__(name_brand, model, year)
#     self.doors = doors

#   def start(self):
#     print("Машина заводится")

#   def stop(self):
#     print("Машина останавливается")
  
#   def open_trunk(self):
#     print("Багажник открыт")

# class Bicycle(Vechile):
#   def __init__(self, name_brand, model, year, type_of_bicycle):
#     super().__init__(name_brand, model, year)
#     self.type_of_bicycle = type_of_bicycle

#   def start(self):
#     print("Велосипед начинает движение")

#   def stop(self):
#     print("Велосипед останавливается")

#   def ring_bell(self):
#     print("Звонок звенит")
  
# class Boat(Vechile):
#   def __init__(self, name_brand, model, year, length):
#     super().__init__(name_brand, model, year)
#     self.length = length

#   def start(self):
#     print("Лодка плывет")

#   def stop(self):
#     print("Лодка причаливет")

#   def anchor(self):
#     print("Якорь спущен")

# car = Car('Toyota', 'Sopra', 1990, 4)
# bicycle = Bicycle('Fix','sportage', 2000, 'Горный')
# boat = Boat('eshkere', 'very good', 2011, 6)

# for vechical in [car,bicycle,boat]:
#   vechical.info()
#   vechical.start()
#   vechical.stop()

# print()

# car.open_trunk()
# bicycle.ring_bell()
# boat.anchor()