"""ООП -  """
# class Car:
#   def __init__(self, wheel, motor, body):
#     self.wheel = wheel
#     self.motor = motor
#     self.body = body 

#     self.back = 20
#     self.is_start = False

#   def info(self):
#     print(f"колесо - {self.wheel}, мотор - {self.motor}, кузов - {self.body}")

#   def start(self):
#     if self.back > 0:
#       self.is_start = True
#       print(f"Машина заведена")
#     else:
#       print("У машины нет топлива")

#   def stop(self):
#     self.is_start = False
#     print("Машина заглушена")

#   def drive(self, city):
#     if self.is_start == True:
#       print(f"Машина едет в {city}")
#     else:
#       print("Машина не заведена")


# car = Car("R20", "V8", "Sedan")
# car.info()
# car.start()
# # car.stop()
# car.drive("Дубай")

# name = ("Asko", "Isko", "Sema")
# list_example = list(name)
# list_example.append("Aslan")
# name = tuple(list_example)
# print(name)

# class book:
#   def __init__( self, avtor, book_name, year,):
#      self.avtor = avtor
#      self.book_name = book_name
#      self.year = year

#   def info(self):
#     print(f"автор - {self.avtor}, название - {self.book_name}, год - {self.year}")

# book = book('Чингиз Айтматов', 'Ак-кеме','1998')
# book.info()


# class Fruit:
#   def __init__(self, name, color, weight):
#     self.name = name
#     self.color = color
#     self.weight = weight

#   def info(self):
#     print(f"название : {self.name}, цвет : {self.color}, вес : {self.weight}")

# fruit = Fruit('Гранат' , 'красный'  , '1 - гранат ,100грамов')
# fruit.info()
# fruit = Fruit('Арбуз' , 'зеленый'  , '1 - арбуз ,15кг')
# fruit.info()
# fruit = Fruit('дыня' , 'желтый'  , '1 - дыня ,10кг')
# fruit.info()

# class Book:
#     def __init__(self, title, author, pages,):
#         self.title = title
#         self.author = author
#         self.pages = pages

#     def info(self):
#         print(f"Название : {self.title}, Атор : {self.author}, Количество страниц : {self.pages}")

#     def check_pages(self):
#       if self.pages > 300:
#         print("Толстая")
#       elif 100 <= self.pages <= 300:
#         print("Средняя")
#       elif self.pages < 100:
#         print("Тонкая")
#       else:
#         print("Ошибка")
        

# book = Book('48 законов власти', 'Роберт Грина', 250)
# book.info()
# book.check_pages()