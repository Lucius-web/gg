class Computer:
  def __init__(self, cpu, memory):
      self.__cpu = cpu
      self.__memory = memory

  def __make_computations(self):
      return f"""Сложение: {self.__cpu + self.__memory},
Вычитание: {self.__cpu - self.__memory},
Умножение: {self.__cpu * self.__memory},
Деление:   {self.__cpu / self.__memory}"""

  @property
  def cpu(self):
      return self.__cpu
  @property
  def memory(self):
      return self.__memory
  
  def make_computations(self):
      return self.__make_computations()

class Laptop(Computer):
  def __init__(self, cpu, memory, memory_card):
      super().__init__(cpu, memory)
      self.__memory_card = memory_card

  @property
  def memory_card(self):
    return self.__memory_card

  def info(self):
    return f"cpu - {self.cpu}, memory - {self.memory}, laptop - {self.memory_card} "

computer = Computer(1993, 6)
print(computer.make_computations())

laptop = Laptop(2342, 8, "SD-card")
print(laptop.info())
