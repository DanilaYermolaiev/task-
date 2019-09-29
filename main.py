#!/usr/bin/python
# -*- coding: utf-8 -*-


import random 


print('Game start')

# Базовый класс для игроков 
class Player():

    # Здоровье игроков 
    hp = 100
    

    def name(self):
        return self.__class__.__name__

    # Функция вычисления урона умеренной атаки
    def attack(self, player):
        damage  = random.randint(18, 25)
        print(self.name(),' make a normal attack to a ',player.name() , ' and make ' , damage ,' damage.')
        player.hp -= damage
        if player.hp < 0:
            player.hp = 0

    # Функция вычисления урона в большом диапазоне атаки
    def powerAttack(self, player):
        powerdamage = random.randint(10,35)       
        print(self.name(),' make a power attack to a ',player.name() , ' and make ' , powerdamage ,' damage.')
        player.hp -= powerdamage
        if player.hp < 0:
            player.hp = 0

    # Функция исцеления в небольшом диапазоне 
    def heal(self):
        heal = random.randint(18, 25)
        self.hp += heal 
        print(self.name(), ' heal itself for ', heal, 'points')
        
        if self.hp >= 100:
            self.hp = 100

# Производный класс
class Human(Player):
    pass    
human = Human()

# Производный класс
class Computer(Player):

    # Функция увеличивающая шанс на исцеление 
    def boostHeal(self):
        if computer.hp < 35:    
            print('SUPER HEALING CHANCE')
            actions = random.choice(['attack', 'powerAttack'])  
            action = random.choice([actions ,'heal'])
    
computer = Computer()   

# Случайный выбор игрока
users = [computer, human]
random.shuffle(users)

# Цикл  
while True:

    firstUser = users[0]
    secondUser = users[1]

    # Случайный выбор действия 
    action = random.choice(['attack', 'powerAttack','heal'])
    
    if action == 'attack':
        firstUser.attack(secondUser)
    elif action == 'powerAttack':
        firstUser.powerAttack(secondUser)
    elif action == 'heal':
        firstUser.heal()
    
    # Вывод информации о уровне здоровья 
    print(firstUser.name(),' health: ', firstUser.hp)
    print(secondUser.name(),' health: ', secondUser.hp)
    
    # Определение конца цикла 
    if firstUser.hp <= 0:  
        loser = firstUser.name()
        break
    elif secondUser.hp <= 0:
        loser = secondUser.name()
        break
    
    # Реверс массива с игроками 
    users.reverse()

    computer.boostHeal()
    

print(loser,'lose')
