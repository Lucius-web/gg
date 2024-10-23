""" Инкапсуляция """

# # Публичный класс
# class PublicExample: # Публичный класс
#   def __init__(self, value):
#     self.value = value # Публичный метод
    
#   def info(self):
#     return self.value # Публичный метод
  
# public = PublicExample(32)
# print(public.info()) # Вызов публичного метода
# print(public.value) # Доступ к публичному атрибуту

# class ProtectedExample:
#   def __init__(self, value):
#       self._value = value # Защищённый атрибут
      
#   def _info(self):
#     return self._value # Защищенный метод
  
# protected = ProtectedExample(32)
# print(protected._info()) # Это работает но противоречит принципам инкапсуляции
# print(protected._value) # Можно получить значение на прямую но это не рекомендуется

# class PrivateExample: # приватный класс
#   def __init__(self, value):
#     self.__value = value # приватный атрибут
    
#   def __info(self):
#     return f'Приватный класс {self.__value}' # приватный метод
  
#   def test(self):
#     return self.__info() # Публичный метод где мы получаем доступ к приватному методу или атрибуту
  
# private123 = PrivateExample(321)

# Прямой вызов приватного метода вызовет ошибку
# print(private123.__info())

# Прямой вызов приватного метода вызовет ошибку
# print(private123.__value)

# Доступ к приватному атрибуту атрибуту либо методу через name mangling 
# print(private123.test())

# import datetime

# class Car:
#   def __init__(self, marka, model, year, mileage):
#     self.marka = marka
#     self.model = model
#     self._year = year
#     self.__mileage = mileage

#   def info(self):
#     return f"Марка - {self.marka} \nМодель - {self.model}"
  
#   def _calculate_age(self):
#     current = datetime.datetime.now().year
#     return f'Возрвваст машины - {current - self._year}'
  
#   def __update_milage(self):
#     return self.__mileage

#   def set_mileage(self):
#     return self.__update_milage()

# car = Car('Mazda', 'Demio', 2008, 2345454)
# print(car.info())
# print(car._calculate_age)
# print(car.set_mileage)