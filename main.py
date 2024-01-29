#!/usr/bin/python
# -*- coding: utf-8 -*-


import random


print('Game start')

# basic class
class Player():

    # health
    hp = 100


    def name(self):
        return self.__class__.__name__

    # Moderate attack damage calculation function
    def attack(self, player):
        damage  = random.randint(18, 25)
        print(self.name(),' make a normal attack to a ',player.name() , ' and make ' , damage ,' damage.')
        player.hp -= damage
        if player.hp < 0:
            player.hp = 0

    # Function for calculating damage over a large attack range
    def powerAttack(self, player):
        powerdamage = random.randint(10,35)
        print(self.name(),' make a power attack to a ',player.name() , ' and make ' , powerdamage ,' damage.')
        player.hp -= powerdamage
        if player.hp < 0:
            player.hp = 0

    # Healing function in a small range
    def heal(self):
        heal = random.randint(18, 25)
        self.hp += heal
        print(self.name(), ' heal itself for ', heal, 'points')

        if self.hp >= 100:
            self.hp = 100

# Derived class
class Human(Player):
    pass
human = Human()

# Derived class
class Computer(Player):

    # Function that increases the chance of healing
    def boostHeal(self):
        if computer.hp < 35:
            print('SUPER HEALING CHANCE')
            actions = random.choice(['attack', 'powerAttack'])
            action = random.choice([actions ,'heal'])

computer = Computer()

# Random player selection
users = [computer, human]
random.shuffle(users)

while True:

    firstUser = users[0]
    secondUser = users[1]

    # Random action selection
    action = random.choice(['attack', 'powerAttack','heal'])

    if action == 'attack':
        firstUser.attack(secondUser)
    elif action == 'powerAttack':
        firstUser.powerAttack(secondUser)
    elif action == 'heal':
        firstUser.heal()

    # Displaying information about your health level
    print(firstUser.name(),' health: ', firstUser.hp)
    print(secondUser.name(),' health: ', secondUser.hp)

    # Determining the end of a loop
    if firstUser.hp <= 0:
        loser = firstUser.name()
        break
    elif secondUser.hp <= 0:
        loser = secondUser.name()
        break

    # Reverse array with players
    users.reverse()

    computer.boostHeal()


print(loser,'lose')
