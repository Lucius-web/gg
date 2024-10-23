# class Game:
#   def __init__(self, game_name, graphics, game_year, company):
#     self.game_name = game_name
#     self.graphics = graphics  
#     self.game_year = game_year  
#     self.company = company
    
#   def info(self):
#     print(f"Game - {self.game_name}, - {self.graphics}, - {self.game_year}, - {self.company}")
    
# game = Game('MobileLegends', 'Full HD', "2017", "Tencent")
# game.info()

# class Roblox(Game):
#   def __init__(self, game_name, graphics, game_year, company):
#     Game.__init__(self, game_name,graphics, game_year, company)
#     self.multiplayer = 'multiplayer'
#     self.name = 'Iskhak'
#     self.gender = 'man'
#     self.skin = 'naruto'
#     self.hp = '100'
    
#   def info(self):
#     print(f"Game - {self.game_name}, - {self.graphics}, - {self.game_year}, - {self.company}, - {self.multiplayer}")
    
#   def info_player(self):
#     print(f'Player - {self.name}, Gender - {self.gender}, Skin - {self.skin}, Health point - {self.hp}')
    
#   def edit_player(self):
#     name = input('Введите тмя игрока: ')
#     gender = input("Введите пол игрока: ")
#     skin = input("Введите облик:")
#     self.name = name
#     self.gender = gender
#     self.skin = skin
  
# roblox = Roblox("Roblox", "ULTRA", "2006", "Roblox_corparatyon")
# roblox.info()
# roblox.edit_player()



""" Наследование """

# class Game:
#     def __init__(self, game_name, graphics, game_year, company):
#         self.game_name = game_name
#         self.graphics = graphics
#         self.game_year = game_year
#         self.company = company
        
#     def info(self):
#         print(f"Game - {self.game_name} - {self.graphics} - {self.game_year} - {self.company} - {self.multiplayer}")
        
# game = Game('MobileLegends', 'FULL HD', 2017, 'Tencent')
# game.info()

# class Roblox(Game):
#     def __init__(self, game_name, graphics, game_year, company, multiplayer):
#         # super().__init__(game_name, graphics, game_year, company)
#         Game.__init__(self, game_name, graphics, game_year, company)
#         self.multiplayer = multiplayer
#         self.name = 'Iskhak'
#         self.gender = 'man'
#         self.skin = 'naruto'
#         self.hp = '100'
        
#     def info(self):
#         print(f"Game - {self.game_name} - {self.graphics} - {self.game_year} - {self.company} - {self.multiplayer}")
        
#     def info_player(self):
#         print(f'Игрок - {self.name} - {self.gender} - {self.skin} - {self.hp}')
        
#     def edit_player(self):
#         name = input("Введите имя игрока: ")
#         gender = input("Введите пол игрока: ")
#         skin = input("Введите облик для игрока: ")
#         self.name = name
#         self.gender = gender
#         self.skin = skin
    
# roblox = Roblox("Roblox", "ULTRA", 2006, 'Roblox Corporation', 'ДА')
# roblox.info()
# roblox.edit_player()
# roblox.info_player()


