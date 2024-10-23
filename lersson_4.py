""" Полиморфиз"""

# num1 = 1
# num2 = 2
# print(num1 + num2)

# string1 = "Hello"
# string2 = "Geeks"
# print(string1 + string2)

# print(len("Hefafsgafgaba"))
# print(len(['phyton', 'JS', 'garry']))
# print(len({'phyton': 'Bob', 'jorj' : 'cat'}))

# class Cat:
  # def __init__(self,name, perfences):
  #   self.name = name
  #   self.perfences = perfences

  # def make_sound(self):
  #   print("Мяу!")

# class Dog:
#   def __init__(self,name, perfences):
#     self.name = name
#     self.perfences = perfences

#   def info(self):
#     print f'Я собака . Меня зовут{self.name}. Мне {self.preferences} года'

#   def make_sound(self):
#     print("Гаф!")

# cat = Cat("Васька", 2)
# dog = Dog("Мухтар", 3)

# for animal in (cat, dog):
#   animal.make_sound()
#   animal.info()

# class PaymetMethod:
#   def pay (self, amount):
#     pass

# class CreditCard(PaymetMethod):
#   def pay(self, amount):
#     return f'Сумма {amount}, оплачивается по кредитной карте'
     
# class PayPal(PaymetMethod):
#   def pay(self, amount):
#     return f'Сумма {amount}, оплачивается PayPal'

# class BankTransfer(PaymetMethod):
#   def pay(self, amount):
#     return f'Сумма {amount}, оплачивается по банковскому переводу'

# payments = [CreditCard(), PayPal(), BankTransfer()]

# for payment in payments:
#   print(payment.pay(100))

# from abc import abctractmethod

# class Vehicle:
 
#   def start_engine(self):
#     pass

#   def stop_engine(self):
#     pass

#   def drive(self):
#     pass

# class Car(Vehicle):
#   def start_engine(self):
#     return 'Двигатель автомобиля заведена'

#   def stop_engine(self):
#     return 'Двигатель автомобиля не заведен'

#   def drive(self):
#     return 'Автомобиль едет'

# class Bycycle(Vehicle):
#   def start_engine(self):
#     return 'У велосопеда нет двигателя'

#   def stop_engine(self):
#     return 'У велосипеда нет двигателя'

#   def drive(self):
#     return 'Велосипед едет'

# vehicle = [Car(), Bycycle()]

# for vehicle in vehicle:
#   print(vehicle.start_engine())
#   print(vehicle.stop_engine())
#   print(vehicle.drive())

# class Employee:
#     def __init__(self, name, amount):
#         self.name = name 
#         self.amount = amount
        
#     def display_info(self):
#         return f'Имя - {self.name}'
        
#     def calculate_salary(self):
#         return f'Имя - {self.name}  Зп - {self.amount}'
    
# class FullTimeEmployee(Employee):
#     def __init__(self, name):
#         super().__init__(name)
        
#     def calculate_salary(self):
#         return f'Имя - {self.name}  Зп - {self.amount * 1.2}'
    
# class PartTimeEmployee(Employee):
#     def __init__(self, name, amount, time):
#         super().__init__(name, amount)
#         self.time = time
        
#     def calculate_salary(self):
#         return f'Имя - {self.name}  Зп - {self.amount * 1.2} * {self.time}'
    
    
# def process_salary(employee):
#     employee.display_info()


    