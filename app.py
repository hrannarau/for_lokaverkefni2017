#Hrannar Helgi Auðunsson og Magnús Dagur Jóhannesson
from random import *
import time

class Ninja():
    def __init__(self,heal=0,dead=0,sleep=0,damage=0,hits=0,accuracy=0):
        self.heal = heal
        self.dead = dead
        self.sleep = sleep
        self.damage = damage
        self.hits = hits
        self.accuracy = accuracy
    def Kick(self):
        
        self.heal = 0
        self.dead = 0
        self.sleep = 0
        
        self.damage = 150
        self.hits = 1
        self.accuracy = 70
    def Ninjastar(self):
        
        self.heal = 0
        self.dead = 0
        self.sleep = 0
        
        self.damage = 60
        self.hits = randint(2,5)
        self.accuracy = 50
    def Sleep(self):
        
        self.heal = 0
        self.dead = 0
        self.sleep = 2
        
        self.damage = 0
        self.hits = 1
        self.accuracy = 40
    def Katana(self):
        
        self.heal = 0
        self.dead = 0
        self.sleep = 0
        
        self.damage = 675
        self.hits = 1
        self.accuracy = 25

class Viking():
    def __init__(self,heal=0,dead=0,sleep=0,damage=0,hits=0,accuracy=0):
        self.heal = heal
        self.dead = dead
        self.sleep = sleep
        self.damage = damage
        self.hits = hits
        self.accuracy = accuracy
    def Axe(self):
        
        self.heal = 0
        self.dead = 0
        self.sleep = 0
        
        self.damage = 60
        self.hits = 1
        self.accuracy = 80
    def Life(self):
        
        self.heal = 200
        self.dead = 0
        self.sleep = 0
        
        self.damage = 0
        self.hits = 1
        self.accuracy = 60
    def AxeThrow(self):
        self.heal = 0
        self.dead = 0
        self.sleep = 0
        self.damage = 170
        self.hits = 1
        self.accuracy = 50
        
    def Berzerk(self):
        
        self.heal = 0
        self.dead = 0
        self.sleep = 0
        
        self.damage = 60
        self.hits = randint(2,6)
        self.accuracy = 35

class Wizard():
    def __init__(self,heal=0,dead=0,sleep=0,damage=0,hits=0,accuracy=0):
        self.heal = heal
        self.dead = dead
        self.sleep = sleep
        self.damage = damage
        self.hits = hits
        self.accuracy = accuracy
    def Fireball(self):
        
        self.heal = 0
        self.dead = 0
        self.sleep = 0
        
        self.damage = 170
        self.hits = 1
        self.accuracy = 70
    def Freeze(self):
        
        self.heal = 0
        self.dead = 0
        self.sleep = 2
        
        self.damage = 0
        self.hits = 1
        self.accuracy = 50
    def Lightning(self):
        
        self.heal = 0
        self.dead = 0
        self.sleep = 0
        
        self.damage = 120
        self.hits = randint(1,4)
        self.accuracy = 50
    def Heal(self):
        
        self.heal = 600
        self.dead = 0
        self.sleep = 0
        
        self.damage = 0
        self.hits = 1
        self.accuracy = 40


print("-----------------")
print("Welcome to Ashkin")
print(" 1. Ninja")
print(" 2. Viking")
print(" 3. Wizard")
fighter1 = input("Player 1: choose your fighter: ")
fighter2 = input("Player 2: choose your fighter: ")
fighter1lif = 0
fighter2lif = 0
start = randint(1,2)
print("Player",start,"begins")

if fighter1 == "1":
    fighter1 = "Ninja"
    fighter1lif = 1800
elif fighter1 == "2":
    fighter1 = "Viking"
    fighter1lif = 3600
elif fighter1 == "3":
    fighter1 = "Wizard"
    fighter1lif = 1500
else:
    print("Wrong Selection, start again")


if fighter2 == "1":
    fighter2 = "Ninja"
    fighter2lif = 1800
elif fighter2 == "2":
    fighter2 = "Viking"
    fighter2lif = 3600
elif fighter2 == "3":
    fighter2 = "Wizard"
    fighter2lif = 1500
else:
    print("Wrong Selection, start again")

while fighter1lif > 0 or fighter2lif > 0:
    if start == 1:
        if fighter1 == "Ninja":
            accuracyCount = randint(1, 100)
            klasi = Ninja()
            print("----------------------------------------------")
            print("1.Kick:       (70% 150 DMG)")
            print("2.Ninja Star: (50% 60 DMG 2-5 times)")
            print("3.Sleep:      (40% Your opponent loses two turns)")
            print("4.Katana:     (25% 675 DMG)")
            print("----------------------------------------------")

            move = int(input("Choose a move Player 1: "))
            if move == 1:
                klasi.Kick()
                print("----------------------------------------------")
                print("Damage:", klasi.damage)
                print("Accuracy:", klasi.accuracy)
                print("Hits:", klasi.hits)
                print("----------------------------------------------")
                if accuracyCount < klasi.accuracy:
                    fighter2lif = fighter2lif - klasi.damage
                    print("You hit!")
                    print("You did", klasi.damage, "damage")
                else:
                    print("Darn you missed :(")

            elif move == 2:
                klasi.Ninjastar()
                print("----------------------------------------------")
                print("Damage:", klasi.damage)
                print("Accuracy:", klasi.accuracy)
                print("Hits:", klasi.hits)
                print("----------------------------------------------")
                if accuracyCount < klasi.accuracy:
                    fighter2lif = fighter2lif - klasi.damage
                    print("You hit!")
                    print("You did", klasi.damage, "damage")
                else:
                    print("Darn you missed :(")

            elif move == 3:
                klasi.Sleep()
                print("----------------------------------------------")
                print("Turns asleep:", klasi.sleep)
                print("Accuracy:", klasi.accuracy)
                print("----------------------------------------------")
                if accuracyCount < klasi.accuracy:
                    turns = 1
                    while turns < 3:
                        accuracyCount = randint(1, 100)
                        klasi = Ninja()
                        print("----------------------------------------------")
                        print("1.Kick:       (70% 150 DMG)")
                        print("2.Ninja Star: (50% 60 DMG 2-5 times)")
                        print("3.Sleep:      Not available")
                        print("4.Katana:     (25% 675 DMG)")
                        print("----------------------------------------------")

                        move = int(input("Choose a move Player 1: "))
                        if move == 1:
                            klasi.Kick()
                            print("----------------------------------------------")
                            print("Damage:", klasi.damage)
                            print("Accuracy:", klasi.accuracy)
                            print("Hits:", klasi.hits)
                            print("----------------------------------------------")
                            if accuracyCount < klasi.accuracy:
                                fighter2lif = fighter2lif - klasi.damage
                                print("You hit!")
                                print("You did", klasi.damage, "damage")
                            else:
                                print("Darn you missed :(")

                        elif move == 2:
                            klasi.Ninjastar()
                            print("----------------------------------------------")
                            print("Damage:", klasi.damage)
                            print("Accuracy:", klasi.accuracy)
                            print("Hits:", klasi.hits)
                            print("----------------------------------------------")
                            if accuracyCount < klasi.accuracy:
                                fighter2lif = fighter2lif - klasi.damage
                                print("You hit!")
                                print("You did", klasi.damage, "damage")
                            else:
                                print("Darn you missed :(")

                        elif move == 3:
                            print("----------------------------------------------")
                            print("1.Kick:       (70% 150 DMG)")
                            print("2.Ninja Star: (50% 60 DMG 2-5 times)")
                            print("3.Sleep:      Not available")
                            print("4.Katana:     (25% 675 DMG)")
                            print("----------------------------------------------")

                            move = int(input("Choose a move Player 1: "))

                        elif move == 4:
                            klasi.Katana()
                            print("----------------------------------------------")
                            print("ULTIMATE ATTACK")
                            print("----------------------------------------------")
                            print("Damage:", klasi.damage)
                            print("Accuracy:", klasi.accuracy)
                            print("----------------------------------------------")
                            if accuracyCount < klasi.accuracy:
                                fighter2lif = fighter2lif - klasi.damage
                                print("You hit!")
                                print("You call that a knife? This is a knife!")
                                print("You did", klasi.damage, "damage")
                            else:
                                print("Darn you missed :(")

                        else:
                            move = int(input("Choose a move Player 1: "))

                        turns += 1
                else:
                    print("Darn you missed :(")

            elif move == 4:
                klasi.Katana()
                print("----------------------------------------------")
                print("ULTIMATE ATTACK")
                print("----------------------------------------------")
                print("Damage:", klasi.damage)
                print("Accuracy:", klasi.accuracy)
                print("----------------------------------------------")
                if accuracyCount < klasi.accuracy:
                    fighter2lif = fighter2lif - klasi.damage
                    print("You hit!")
                    print("You call that a knife? This is a knife!")
                    print("You did", klasi.damage, "damage")
                else:
                    print("Darn you missed :(")

            else:
                move = int(input("Choose a move Player 1: "))


        elif fighter1 == "Viking":
            accuracyCount = randint(1, 100)
            klasi = Viking()
            print("----------------------------------------------")
            print("1.Axe:     (80% 60 DMG)")
            print("2.Life:    (60% 200+ health)")
            print("3.AxeThrow (50% 170 DMG)")
            print("4.Berzerk: (35% You hit your axe 2-6 times)")
            print("----------------------------------------------")

            move = int(input("Choose a move Player 1: "))

            if move == 1:
                klasi.Axe()
                print("----------------------------------------------")
                print("Damage:", klasi.damage)
                print("Accuracy:", klasi.accuracy)
                print("Hits:", klasi.hits)
                print("----------------------------------------------")
                if accuracyCount < klasi.accuracy:
                    fighter2lif = fighter2lif - klasi.damage
                    print("You hit!")
                    print("You did", klasi.damage, "damage")
                else:
                    print("Darn you missed :(")

            elif move == 2:
                klasi.Life()
                print("----------------------------------------------")
                print("Heal:", klasi.heal)
                print("Accuracy", klasi.accuracy)
                print("----------------------------------------------")
                if accuracyCount < klasi.accuracy:
                    fighter1lif = fighter1lif + klasi.heal
                    print("You hit!")
                    print("You healed", klasi.heal, "points")
                else:
                    print("Darn you missed :(")

            elif move == 3:
                klasi.AxeThrow()
                print("----------------------------------------------")
                print("Damage:", klasi.damage)
                print("Accuracy:", klasi.accuracy)
                print("Hits:", klasi.hits)
                print("----------------------------------------------")
                if accuracyCount < klasi.accuracy:
                    fighter2lif = fighter2lif - klasi.damage
                    print("You hit!")
                    print("You did", klasi.damage, "damage")
                else:
                    print("Darn you missed :(")

            elif move == 4:
                klasi.Berzerk()
                print("----------------------------------------------")
                print("ULTIMATE ATTACK")
                print("---------------")
                print("Damage:", klasi.damage)
                print("Accuracy:", klasi.accuracy)
                print("Hits:", klasi.hits)
                print("----------------------------------------------")
                if accuracyCount < klasi.accuracy:
                    fighter2lif = fighter2lif - (klasi.damage * klasi.hits)
                    print("You hit!")
                    print("Taste my steel, you foul beast!")
                    print("You did", klasi.damage * klasi.hits, "damage")
                else:
                    print("Darn you missed :(")

            else:
                move = int(input("Choose a move Player 1: "))


        elif fighter1 == "Wizard":
            accuracyCount = randint(1, 100)
            klasi = Wizard()
            print("----------------------------------------------")
            print("1.Fireball: (70% 170 DMG)")
            print("2.Freeze:   (50% Your opponent loses two turns)")
            print("3.Lightning: (50% 120 DMG 1-4 times)")
            print("4.Heal:     (40% 600+ health)")
            print("----------------------------------------------")

            move = int(input("Choose a move Player 1: "))

            if move == 1:
                klasi.Fireball()
                print("----------------------------------------------")
                print("Damage:", klasi.damage)
                print("Accuracy:", klasi.accuracy)
                print("Hits:", klasi.hits)
                print("----------------------------------------------")
                if accuracyCount < klasi.accuracy:
                    fighter2lif = fighter2lif - klasi.damage
                    print("You hit!")
                    print("You did", klasi.damage, "damage")
                else:
                    print("Darn you missed :(")

            elif move == 2:
                klasi.Freeze()
                print("Turns frozen:", klasi.sleep)
                print("Accuracy:", klasi.accuracy)
                if accuracyCount < klasi.accuracy:
                    turns = 1
                    while turns < 3:
                        accuracyCount = randint(1, 100)
                        klasi = Wizard()
                        print("----------------------------------------------")
                        print("1.Fireball: (70% 170 DMG)")
                        print("2.Freeze:   Not available")
                        print("3.Lightning: (50% 120 DMG 1-4 times)")
                        print("4.Heal:     (40% 600+ health)")
                        print("----------------------------------------------")

                        move = int(input("Choose a move Player 1: "))
                        if move == 1:
                            klasi.Fireball()
                            print("----------------------------------------------")
                            print("Damage:", klasi.damage)
                            print("Accuracy:", klasi.accuracy)
                            print("Hits:", klasi.hits)
                            print("----------------------------------------------")
                            if accuracyCount < klasi.accuracy:
                                fighter2lif = fighter2lif - klasi.damage
                                print("You hit!")
                                print("You did", klasi.damage, "damage")
                            else:
                                print("Darn you missed :(")

                        elif move == 2:
                            print("----------------------------------------------")
                            print("1.Fireball: (70% 170 DMG)")
                            print("2.Freeze:   Not available")
                            print("3.Lightning:(50% 120 DMG 1-4 times)")
                            print("4.Heal:     (40% 600+ health)")
                            print("----------------------------------------------")

                            move = int(input("Choose a move Player 1: "))

                        elif move == 3:
                            klasi.Lightning()
                            print("----------------------------------------------")
                            print("Damage:", klasi.damage)
                            print("Accuracy:", klasi.accuracy)
                            print("Hits:", klasi.hits)
                            print("----------------------------------------------")
                            if accuracyCount < klasi.accuracy:
                                fighter2lif = fighter2lif - (klasi.damage * klasi.hits)
                                print("You hit", klasi.hits, "times")
                                print("You did", klasi.damage, "damage")
                            else:
                                print("Darn you missed :(")

                        elif move == 4:
                            klasi.Heal()
                            print("----------------------------------------------")
                            print("ULTIMATE ATTACK")
                            print("----------------------------------------------")
                            print("Heal:", klasi.heal)
                            print("Accuracy:", klasi.accuracy)
                            print("----------------------------------------------")
                            if accuracyCount < klasi.accuracy:
                                fighter1lif = fighter1lif + klasi.heal
                                print("You hit!")
                                print("'That outta set you back a bit.'")
                                print("You healed",klasi.heal,"points")
                            else:
                                print("Darn you missed :(")

                        else:
                            move = int(input("Choose a move Player 1: "))

                        turns += 1
                else:
                    print("Darn you missed :(")

            elif move == 3:
                klasi.Lightning()
                print("----------------------------------------------")
                print("Damage:", klasi.damage)
                print("Accuracy:", klasi.accuracy)
                print("Hits:", klasi.hits)
                print("----------------------------------------------")
                if accuracyCount < klasi.accuracy:
                    fighter2lif = fighter2lif - (klasi.damage * klasi.hits)
                    print("You hit", klasi.hits, "times")
                    print("You did", klasi.damage, "damage")
                else:
                    print("Darn you missed :(")

            elif move == 4:
                klasi.Heal()
                print("----------------------------------------------")
                print("ULTIMATE ATTACK")
                print("----------------------------------------------")
                print("Heal:", klasi.heal)
                print("Accuracy:", klasi.accuracy)
                print("----------------------------------------------")
                if accuracyCount < klasi.accuracy:
                    fighter1lif = fighter1lif + klasi.heal
                    print("You hit!")
                    print("'That outta set you back a bit.'")
                    print("You healed", klasi.heal, "points")
                else:
                    print("Darn you missed :(")

            else:
                move = int(input("Choose a move Player 1: "))

        if fighter1lif < 0:
            break
        elif fighter2lif < 0:
            break
        ##################

        if fighter2 == "Ninja":
            accuracyCount = randint(1, 100)
            klasi = Ninja()
            print("----------------------------------------------")
            print("1.Kick:       (70% 150 DMG)")
            print("2.Ninja Star: (50% 60 DMG 2-5 times)")
            print("3.Sleep:      (40% Your opponent loses two turns)")
            print("4.Katana:     (25% 675 DMG)")
            print("----------------------------------------------")

            move = int(input("Choose a move Player 2: "))
            if move == 1:
                klasi.Kick()
                print("----------------------------------------------")
                print("Damage:", klasi.damage)
                print("Accuracy:", klasi.accuracy)
                print("Hits:", klasi.hits)
                print("----------------------------------------------")
                if accuracyCount < klasi.accuracy:
                    fighter1lif = fighter1lif - klasi.damage
                    print("You hit!")
                    print("You did", klasi.damage, "damage")
                else:
                    print("Darn you missed :(")

            elif move == 2:
                klasi.Ninjastar()
                print("----------------------------------------------")
                print("Damage:", klasi.damage)
                print("Accuracy:", klasi.accuracy)
                print("Hits:", klasi.hits)
                print("----------------------------------------------")
                if accuracyCount < klasi.accuracy:
                    fighter1lif = fighter1lif - klasi.damage
                    print("You hit!")
                    print("You did", klasi.damage, "damage")
                else:
                    print("Darn you missed :(")

            elif move == 3:
                klasi.Sleep()
                print("Turns asleep:", klasi.sleep)
                print("Accuracy:", klasi.accuracy)
                if accuracyCount < klasi.accuracy:
                    turns = 0
                    while turns < 3:
                        accuracyCount = randint(1, 100)
                        klasi = Ninja()
                        print("----------------------------------------------")
                        print("1.Kick:       (70% 150 DMG)")
                        print("2.Ninja Star: (50% 60 DMG 2-5 times)")
                        print("3.Sleep:      Not available")
                        print("4.Katana:     (25% 675 DMG)")
                        print("----------------------------------------------")

                        move = int(input("Choose a move Player 2: "))
                        if move == 1:
                            klasi.Kick()
                            print("----------------------------------------------")
                            print("Damage:", klasi.damage)
                            print("Accuracy:", klasi.accuracy)
                            print("Hits:", klasi.hits)
                            print("----------------------------------------------")
                            if accuracyCount < klasi.accuracy:
                                fighter1lif = fighter1lif - klasi.damage
                                print("You hit!")
                                print("You did", klasi.damage, "damage")
                            else:
                                print("Darn you missed :(")

                        elif move == 2:
                            klasi.Ninjastar()
                            print("----------------------------------------------")
                            print("Damage:", klasi.damage)
                            print("Accuracy:", klasi.accuracy)
                            print("Hits:", klasi.hits)
                            print("----------------------------------------------")
                            if accuracyCount < klasi.accuracy:
                                fighter1lif = fighter1lif - klasi.damage
                                print("You hit!")
                                print("You did", klasi.damage, "damage")
                            else:
                                print("Darn you missed :(")

                        elif move == 3:
                            print("----------------------------------------------")
                            print("1.Kick:       (70% 150 DMG)")
                            print("2.Ninja Star: (50% 60 DMG 2-5 times)")
                            print("3.Sleep:      Not available")
                            print("4.Katana:     (25% 675 DMG)")
                            print("----------------------------------------------")

                            move = int(input("Choose a move Player 2: "))

                        elif move == 4:
                            klasi.Katana()
                            print("----------------------------------------------")
                            print("ULTIMATE ATTACK")
                            print("---------------")
                            print("Damage:", klasi.damage)
                            print("Accuracy:", klasi.accuracy)
                            print("----------------------------------------------")
                            if accuracyCount < klasi.accuracy:
                                fighter1lif = fighter1lif - klasi.damage
                                print("You hit!")
                                print("You call that a knife? This is a knife!")
                                print("You did", klasi.damage, "damage")
                            else:
                                print("Darn you missed :(")

                        else:
                            move = int(input("Choose a move Player 2: "))

                        turns += 1
                else:
                    print("Darn you missed :(")

            elif move == 4:
                klasi.Katana()
                print("----------------------------------------------")
                print("ULTIMATE ATTACK")
                print("---------------")
                print("Damage:", klasi.damage)
                print("Accuracy:", klasi.accuracy)
                print("----------------------------------------------")
                if accuracyCount < klasi.accuracy:
                    fighter1lif = fighter1lif - klasi.damage
                    print("You hit!")
                    print("You call that a knife? This is a knife!")
                    print("You did", klasi.damage, "damage")
                else:
                    print("Darn you missed :(")

            else:
                move = int(input("Choose a move Player 2: "))


        elif fighter2 == "Viking":
            accuracyCount = randint(1, 100)
            klasi = Viking()
            print("----------------------------------------------")
            print("1.Axe:     (80% 60 DMG)")
            print("2.Life:    (60% 200+ health)")
            print("3.AxeThrow (50% 170 DMG)")
            print("4.Berzerk: (35% You hit your axe 2-6 times)")
            print("----------------------------------------------")

            move = int(input("Choose a move Player 2: "))

            if move == 1:
                klasi.Axe()
                print("----------------------------------------------")
                print("Damage:", klasi.damage)
                print("Accuracy:", klasi.accuracy)
                print("Hits:", klasi.hits)
                print("----------------------------------------------")
                if accuracyCount < klasi.accuracy:
                    fighter1lif = fighter1lif - klasi.damage
                    print("You hit!")
                    print("You did", klasi.damage, "damage")
                else:
                    print("Darn you missed :(")

            elif move == 2:
                klasi.Life()
                print("----------------------------------------------")
                print("Heal:", klasi.heal)
                print("Accuracy", klasi.accuracy)
                print("----------------------------------------------")
                if accuracyCount < klasi.accuracy:
                    fighter2lif = fighter2lif + klasi.heal
                    print("You hit!")
                    print("You healed", klasi.heal, "points")
                else:
                    print("Darn you missed :(")

            elif move == 3:
                klasi.AxeThrow()
                print("----------------------------------------------")
                print("Damage:", klasi.damage)
                print("Accuracy:", klasi.accuracy)
                print("Hits:", klasi.hits)
                print("----------------------------------------------")
                if accuracyCount < klasi.accuracy:
                    fighter1lif = fighter1lif - klasi.damage
                    print("You hit!")
                    print("You did", klasi.damage, "damage")
                else:
                    print("Darn you missed :(")

            elif move == 4:
                klasi.Berzerk()
                print("----------------------------------------------")
                print("ULTIMATE ATTACK")
                print("----------------------------------------------")
                print("Damage:", klasi.damage)
                print("Accuracy:", klasi.accuracy)
                print("Hits:", klasi.hits)
                print("----------------------------------------------")
                if accuracyCount < klasi.accuracy:
                    fighter1lif = fighter1lif - (klasi.damage * klasi.hits)
                    print("You hit!")
                    print("Taste my steel, you foul beast!")
                    print("You did", klasi.damage * klasi.hits, "damage")
                else:
                    print("Darn you missed :(")

            else:
                move = int(input("Choose a move Player 2: "))


        elif fighter2 == "Wizard":
            accuracyCount = randint(1, 100)
            klasi = Wizard()
            print("----------------------------------------------")
            print("1.Fireball: (70% 170 DMG)")
            print("2.Freeze:   (50% Your opponent loses two turns)")
            print("3.Lightning: (50% 120 DMG 1-4 times)")
            print("4.Heal:     (40% 600+ health)")
            print("----------------------------------------------")

            move = int(input("Choose a move Player 2: "))

            if move == 1:
                klasi.Fireball()
                print("----------------------------------------------")
                print("Damage:", klasi.damage)
                print("Accuracy:", klasi.accuracy)
                print("Hits:", klasi.hits)
                print("----------------------------------------------")
                if accuracyCount < klasi.accuracy:
                    fighter1lif = fighter1lif - klasi.damage
                    print("You hit!")
                    print("You did", klasi.damage, "damage")
                else:
                    print("Darn you missed :(")

            elif move == 2:
                klasi.Freeze()
                print("----------------------------------------------")
                print("Turns frozen:", klasi.sleep)
                print("Accuracy:", klasi.accuracy)
                print("----------------------------------------------")
                if accuracyCount < klasi.accuracy:
                    turns = 1
                    while turns < 3:
                        accuracyCount = randint(1, 100)
                        klasi = Wizard()
                        print("----------------------------------------------")
                        print("1.Fireball: (70% 170 DMG)")
                        print("2.Freeze:   Not available")
                        print("3.Lightning: (50% 120 DMG 1-4 times)")
                        print("4.Heal:     (40% 600+ health)")
                        print("----------------------------------------------")

                        move = int(input("Choose a move Player 2: "))
                        if move == 1:
                            klasi.Fireball()
                            print("----------------------------------------------")
                            print("Damage:", klasi.damage)
                            print("Accuracy:", klasi.accuracy)
                            print("Hits:", klasi.hits)
                            print("----------------------------------------------")
                            if accuracyCount < klasi.accuracy:
                                fighter1lif = fighter1lif - klasi.damage
                                print("You hit!")
                                print("You did", klasi.damage, "damage")
                            else:
                                print("Darn you missed :(")

                        elif move == 2:
                            print("----------------------------------------------")
                            print("1.Fireball: (70% 170 DMG)")
                            print("2.Freeze:   Not available")
                            print("3.Lightning:(50% 120 DMG 1-4 times)")
                            print("4.Heal:     (40% 600+ health)")
                            print("----------------------------------------------")

                            move = int(input("Choose a move Player 2: "))

                        elif move == 3:
                            klasi.Lightning()
                            print("----------------------------------------------")
                            print("Damage:", klasi.damage)
                            print("Accuracy:", klasi.accuracy)
                            print("Hits:", klasi.hits)
                            print("----------------------------------------------")
                            if accuracyCount < klasi.accuracy:
                                fighter1lif = fighter1lif - (klasi.damage * klasi.hits)
                                print("You hit", klasi.hits, "times")
                                print("You did", klasi.damage, "damage")
                            else:
                                print("Darn you missed :(")

                        elif move == 4:
                            klasi.Heal()
                            print("----------------------------------------------")
                            print("ULTIMATE ATTACK")
                            print("----------------------------------------------")
                            print("Heal:", klasi.heal)
                            print("Accuracy:", klasi.accuracy)
                            print("----------------------------------------------")
                            if accuracyCount < klasi.accuracy:
                                fighter2lif = fighter2lif + klasi.heal
                                print("You hit!")
                                print("'That outta set you back a bit.'")
                                print("You healed", klasi.heal, "points")
                            else:
                                print("Darn you missed :(")

                        else:
                            move = int(input("Choose a move Player 2: "))

                        turns += 1
                else:
                    print("Darn you missed :(")

            elif move == 3:
                klasi.Lightning()
                print("----------------------------------------------")
                print("Damage:", klasi.damage)
                print("Accuracy:", klasi.accuracy)
                print("Hits:", klasi.hits)
                print("----------------------------------------------")
                if accuracyCount < klasi.accuracy:
                    fighter1lif = fighter1lif - (klasi.damage * klasi.hits)
                    print("You hit", klasi.hits, "times")
                    print("You did", klasi.damage, "damage")
                else:
                    print("Darn you missed :(")

            elif move == 4:
                klasi.Heal()
                print("----------------------------------------------")
                print("ULTIMATE ATTACK")
                print("----------------------------------------------")
                print("Heal:", klasi.heal)
                print("Accuracy:", klasi.accuracy)
                print("----------------------------------------------")
                if accuracyCount < klasi.accuracy:
                    fighter2lif = fighter2lif + klasi.heal
                    print("You hit!")
                    print("'That outta set you back a bit.'")
                    print("You healed", klasi.heal, "points")
                else:
                    print("Darn you missed :(")

            else:
                move = int(input("Choose a move Player 2: "))

        print("----------------------------------------------")
        print("Player 1:", fighter1)
        print("Player 1 Health:", fighter1lif)
        print("Player 2:", fighter2)
        print("Player 2 Health:", fighter2lif)
        print("----------------------------------------------")
        if fighter1lif < 0:
            break
        elif fighter2lif < 0:
            break
        time.sleep(2)

    ############

    elif start == 2:
        if fighter2 == "Ninja":
            accuracyCount = randint(1, 100)
            klasi = Ninja()
            print("----------------------------------------------")
            print("1.Kick:       (70% 150 DMG)")
            print("2.Ninja Star: (50% 60 DMG 2-5 times)")
            print("3.Sleep:      (40% Your opponent loses two turns)")
            print("4.Katana:     (25% 675 DMG)")
            print("----------------------------------------------")

            move = int(input("Choose a move Player 2: "))
            if move == 1:
                klasi.Kick()
                print("----------------------------------------------")
                print("Damage:", klasi.damage)
                print("Accuracy:", klasi.accuracy)
                print("Hits:", klasi.hits)
                print("----------------------------------------------")
                if accuracyCount < klasi.accuracy:
                    fighter1lif = fighter1lif - klasi.damage
                    print("You hit!")
                    print("You did", klasi.damage, "damage")
                else:
                    print("Darn you missed :(")

            elif move == 2:
                klasi.Ninjastar()
                print("----------------------------------------------")
                print("Damage:", klasi.damage)
                print("Accuracy:", klasi.accuracy)
                print("Hits:", klasi.hits)
                print("----------------------------------------------")
                if accuracyCount < klasi.accuracy:
                    fighter1lif = fighter1lif - klasi.damage
                    print("You hit!")
                    print("You did", klasi.damage, "damage")
                else:
                    print("Darn you missed :(")

            elif move == 3:
                klasi.Sleep()
                print("Turns asleep:", klasi.sleep)
                print("Accuracy:", klasi.accuracy)
                if accuracyCount < klasi.accuracy:
                    turns = 1
                    while turns < 3:
                        accuracyCount = randint(1, 100)
                        klasi = Ninja()
                        print("----------------------------------------------")
                        print("1.Kick:       (70% 150 DMG)")
                        print("2.Ninja Star: (50% 60 DMG 2-5 times)")
                        print("3.Sleep:      Not available")
                        print("4.Katana:     (25% 675 DMG)")
                        print("----------------------------------------------")

                        move = int(input("Choose a move Player 2: "))
                        if move == 1:
                            klasi.Kick()
                            print("----------------------------------------------")
                            print("Damage:", klasi.damage)
                            print("Accuracy:", klasi.accuracy)
                            print("Hits:", klasi.hits)
                            print("----------------------------------------------")
                            if accuracyCount < klasi.accuracy:
                                fighter1lif = fighter1lif - klasi.damage
                                print("You hit!")
                                print("You did", klasi.damage, "damage")
                            else:
                                print("Darn you missed :(")

                        elif move == 2:
                            klasi.Ninjastar()
                            print("----------------------------------------------")
                            print("Damage:", klasi.damage)
                            print("Accuracy:", klasi.accuracy)
                            print("Hits:", klasi.hits)
                            print("----------------------------------------------")
                            if accuracyCount < klasi.accuracy:
                                fighter1lif = fighter1lif - klasi.damage
                                print("You hit!")
                                print("You did", klasi.damage, "damage")
                            else:
                                print("Darn you missed :(")

                        elif move == 3:
                            print("----------------------------------------------")
                            print("1.Kick:       (70% 150 DMG)")
                            print("2.Ninja Star: (50% 60 DMG 2-5 times)")
                            print("3.Sleep:      Not available")
                            print("4.Katana:     (25% 675 DMG)")
                            print("----------------------------------------------")

                            move = int(input("Choose a move Player 2: "))

                        elif move == 4:
                            klasi.Katana()
                            print("----------------------------------------------")
                            print("ULTIMATE ATTACK")
                            print("---------------")
                            print("Damage:", klasi.damage)
                            print("Accuracy:", klasi.accuracy)
                            print("----------------------------------------------")
                            if accuracyCount < klasi.accuracy:
                                fighter1lif = fighter1lif - klasi.damage
                                print("You hit!")
                                print("You call that a knife? This is a knife!")
                                print("You did", klasi.damage, "damage")
                            else:
                                print("Darn you missed :(")

                        else:
                            move = int(input("Choose a move Player 2: "))

                        turns += 1
                else:
                    print("Darn you missed :(")

            elif move == 4:
                klasi.Katana()
                print("----------------------------------------------")
                print("ULTIMATE ATTACK")
                print("---------------")
                print("Damage:", klasi.damage)
                print("Accuracy:", klasi.accuracy)
                print("----------------------------------------------")
                if accuracyCount < klasi.accuracy:
                    fighter1lif = fighter1lif - klasi.damage
                    print("You hit!")
                    print("You call that a knife? This is a knife!")
                    print("You did", klasi.damage, "damage")
                else:
                    print("Darn you missed :(")

            else:
                move = int(input("Choose a move Player 2: "))


        elif fighter2 == "Viking":
            accuracyCount = randint(1, 100)
            klasi = Viking()
            print("----------------------------------------------")
            print("1.Axe:     (80% 60 DMG)")
            print("2.Life:    (60% 200+ health)")
            print("3.AxeThrow (50% 170 DMG)")
            print("4.Berzerk: (35% You hit your axe 2-6 times)")
            print("----------------------------------------------")

            move = int(input("Choose a move Player 2: "))

            if move == 1:
                klasi.Axe()
                print("----------------------------------------------")
                print("Damage:", klasi.damage)
                print("Accuracy:", klasi.accuracy)
                print("Hits:", klasi.hits)
                print("----------------------------------------------")
                if accuracyCount < klasi.accuracy:
                    fighter1lif = fighter1lif - klasi.damage
                    print("You hit!")
                    print("You did", klasi.damage, "damage")
                else:
                    print("Darn you missed :(")

            elif move == 2:
                klasi.Life()
                print("----------------------------------------------")
                print("Heal:", klasi.heal)
                print("Accuracy", klasi.accuracy)
                print("----------------------------------------------")
                if accuracyCount < klasi.accuracy:
                    fighter2lif = fighter2lif + klasi.heal
                    print("You hit!")
                    print("You healed", klasi.heal, "points")
                else:
                    print("Darn you missed :(")

            elif move == 3:
                klasi.AxeThrow()
                print("----------------------------------------------")
                print("Damage:", klasi.damage)
                print("Accuracy:", klasi.accuracy)
                print("Hits:", klasi.hits)
                print("----------------------------------------------")
                if accuracyCount < klasi.accuracy:
                    fighter1lif = fighter1lif - klasi.damage
                    print("You hit!")
                    print("You did", klasi.damage, "damage")
                else:
                    print("Darn you missed :(")

            elif move == 4:
                klasi.Berzerk()
                print("----------------------------------------------")
                print("ULTIMATE ATTACK")
                print("----------------------------------------------")
                print("Damage:", klasi.damage)
                print("Accuracy:", klasi.accuracy)
                print("Hits:", klasi.hits)
                print("----------------------------------------------")
                if accuracyCount < klasi.accuracy:
                    fighter1lif = fighter1lif - (klasi.damage * klasi.hits)
                    print("You hit!")
                    print("Taste my steel, you foul beast!")
                    print("You did", klasi.damage * klasi.hits, "damage")
                else:
                    print("Darn you missed :(")

            else:
                move = int(input("Choose a move Player 2: "))


        elif fighter2 == "Wizard":
            accuracyCount = randint(1, 100)
            klasi = Wizard()
            print("----------------------------------------------")
            print("1.Fireball: (70% 170 DMG)")
            print("2.Freeze:   (50% Your opponent loses two turns)")
            print("3.Lightning: (50% 120 DMG 1-4 times)")
            print("4.Heal:     (40% 600+ health)")
            print("----------------------------------------------")

            move = int(input("Choose a move Player 2: "))

            if move == 1:
                klasi.Fireball()
                print("----------------------------------------------")
                print("Damage:", klasi.damage)
                print("Accuracy:", klasi.accuracy)
                print("Hits:", klasi.hits)
                print("----------------------------------------------")
                if accuracyCount < klasi.accuracy:
                    fighter1lif = fighter1lif - klasi.damage
                    print("You hit!")
                    print("You did", klasi.damage, "damage")
                else:
                    print("Darn you missed :(")

            elif move == 2:
                klasi.Freeze()
                print("----------------------------------------------")
                print("Turns frozen:", klasi.sleep)
                print("Accuracy:", klasi.accuracy)
                print("----------------------------------------------")
                if accuracyCount < klasi.accuracy:
                    turns = 1
                    while turns < 3:
                        accuracyCount = randint(1, 100)
                        klasi = Wizard()
                        print("----------------------------------------------")
                        print("1.Fireball: (70% 170 DMG)")
                        print("2.Freeze:   Not available")
                        print("3.Lightning: (50% 120 DMG 1-4 times)")
                        print("4.Heal:     (40% 600+ health)")
                        print("----------------------------------------------")

                        move = int(input("Choose a move Player 2: "))
                        if move == 1:
                            klasi.Fireball()
                            print("----------------------------------------------")
                            print("Damage:", klasi.damage)
                            print("Accuracy:", klasi.accuracy)
                            print("Hits:", klasi.hits)
                            print("----------------------------------------------")
                            if accuracyCount < klasi.accuracy:
                                fighter1lif = fighter1lif - klasi.damage
                                print("You hit!")
                                print("You did", klasi.damage, "damage")
                            else:
                                print("Darn you missed :(")

                        elif move == 2:
                            print("----------------------------------------------")
                            print("1.Fireball: (70% 170 DMG)")
                            print("2.Freeze:   Not available")
                            print("3.Lightning:(50% 120 DMG 1-4 times)")
                            print("4.Heal:     (40% 600+ health)")
                            print("----------------------------------------------")

                            move = int(input("Choose a move Player 2: "))

                        elif move == 3:
                            klasi.Lightning()
                            print("----------------------------------------------")
                            print("Damage:", klasi.damage)
                            print("Accuracy:", klasi.accuracy)
                            print("Hits:", klasi.hits)
                            print("----------------------------------------------")
                            if accuracyCount < klasi.accuracy:
                                fighter1lif = fighter1lif - (klasi.damage * klasi.hits)
                                print("You hit", klasi.hits, "times")
                                print("You did", klasi.damage, "damage")
                            else:
                                print("Darn you missed :(")

                        elif move == 4:
                            klasi.Heal()
                            print("----------------------------------------------")
                            print("ULTIMATE ATTACK")
                            print("----------------------------------------------")
                            print("Heal:", klasi.heal)
                            print("Accuracy:", klasi.accuracy)
                            print("----------------------------------------------")
                            if accuracyCount < klasi.accuracy:
                                fighter2lif = fighter2lif + klasi.heal
                                print("You hit!")
                                print("'That outta set you back a bit.'")
                                print("You healed", klasi.heal, "points")
                            else:
                                print("Darn you missed :(")

                        else:
                            move = int(input("Choose a move Player 2: "))

                        turns += 1
                else:
                    print("Darn you missed :(")

            elif move == 3:
                klasi.Lightning()
                print("----------------------------------------------")
                print("Damage:", klasi.damage)
                print("Accuracy:", klasi.accuracy)
                print("Hits:", klasi.hits)
                print("----------------------------------------------")
                if accuracyCount < klasi.accuracy:
                    fighter1lif = fighter1lif - (klasi.damage * klasi.hits)
                    print("You hit", klasi.hits, "times")
                    print("You did", klasi.damage, "damage")
                else:
                    print("Darn you missed :(")

            elif move == 4:
                klasi.Heal()
                print("----------------------------------------------")
                print("ULTIMATE ATTACK")
                print("----------------------------------------------")
                print("Heal:", klasi.heal)
                print("Accuracy:", klasi.accuracy)
                print("----------------------------------------------")
                if accuracyCount < klasi.accuracy:
                    fighter2lif = fighter2lif + klasi.heal
                    print("You hit!")
                    print("'That outta set you back a bit.'")
                    print("You healed", klasi.heal, "points")
                else:
                    print("Darn you missed :(")

            else:
                move = int(input("Choose a move Player 2: "))

        if fighter1lif < 0:
            break
        elif fighter2lif < 0:
            break
        ###########

        if fighter1 == "Ninja":
            accuracyCount = randint(1, 100)
            klasi = Ninja()
            print("----------------------------------------------")
            print("1.Kick:       (70% 150 DMG)")
            print("2.Ninja Star: (50% 60 DMG 2-5 times)")
            print("3.Sleep:      (40% Your opponent loses two turns)")
            print("4.Katana:     (25% 675 DMG)")
            print("----------------------------------------------")

            move = int(input("Choose a move Player 1: "))
            if move == 1:
                klasi.Kick()
                print("----------------------------------------------")
                print("Damage:", klasi.damage)
                print("Accuracy:", klasi.accuracy)
                print("Hits:", klasi.hits)
                print("----------------------------------------------")
                if accuracyCount < klasi.accuracy:
                    fighter2lif = fighter2lif - klasi.damage
                    print("You hit!")
                    print("You did", klasi.damage, "damage")
                else:
                    print("Darn you missed :(")

            elif move == 2:
                klasi.Ninjastar()
                print("----------------------------------------------")
                print("Damage:", klasi.damage)
                print("Accuracy:", klasi.accuracy)
                print("Hits:", klasi.hits)
                print("----------------------------------------------")
                if accuracyCount < klasi.accuracy:
                    fighter2lif = fighter2lif - klasi.damage
                    print("You hit!")
                    print("You did", klasi.damage, "damage")
                else:
                    print("Darn you missed :(")

            elif move == 3:
                klasi.Sleep()
                print("----------------------------------------------")
                print("Turns asleep:", klasi.sleep)
                print("Accuracy:", klasi.accuracy)
                print("----------------------------------------------")
                if accuracyCount < klasi.accuracy:
                    turns = 1
                    while turns < 3:
                        accuracyCount = randint(1, 100)
                        klasi = Ninja()
                        print("----------------------------------------------")
                        print("1.Kick:       (70% 150 DMG)")
                        print("2.Ninja Star: (50% 60 DMG 2-5 times)")
                        print("3.Sleep:      Not available")
                        print("4.Katana:     (25% 675 DMG)")
                        print("----------------------------------------------")

                        move = int(input("Choose a move Player 1: "))
                        if move == 1:
                            klasi.Kick()
                            print("----------------------------------------------")
                            print("Damage:", klasi.damage)
                            print("Accuracy:", klasi.accuracy)
                            print("Hits:", klasi.hits)
                            print("----------------------------------------------")
                            if accuracyCount < klasi.accuracy:
                                fighter2lif = fighter2lif - klasi.damage
                                print("You hit!")
                                print("You did", klasi.damage, "damage")
                            else:
                                print("Darn you missed :(")

                        elif move == 2:
                            klasi.Ninjastar()
                            print("----------------------------------------------")
                            print("Damage:", klasi.damage)
                            print("Accuracy:", klasi.accuracy)
                            print("Hits:", klasi.hits)
                            print("----------------------------------------------")
                            if accuracyCount < klasi.accuracy:
                                fighter2lif = fighter2lif - klasi.damage
                                print("You hit!")
                                print("You did", klasi.damage, "damage")
                            else:
                                print("Darn you missed :(")

                        elif move == 3:
                            print("----------------------------------------------")
                            print("1.Kick:       (70% 150 DMG)")
                            print("2.Ninja Star: (50% 60 DMG 2-5 times)")
                            print("3.Sleep:      Not available")
                            print("4.Katana:     (25% 675 DMG)")
                            print("----------------------------------------------")

                            move = int(input("Choose a move Player 1: "))

                        elif move == 4:
                            klasi.Katana()
                            print("----------------------------------------------")
                            print("ULTIMATE ATTACK")
                            print("----------------------------------------------")
                            print("Damage:", klasi.damage)
                            print("Accuracy:", klasi.accuracy)
                            print("----------------------------------------------")
                            if accuracyCount < klasi.accuracy:
                                fighter2lif = fighter2lif - klasi.damage
                                print("You hit!")
                                print("You call that a knife? This is a knife!")
                                print("You did", klasi.damage, "damage")
                            else:
                                print("Darn you missed :(")

                        else:
                            move = int(input("Choose a move Player 1: "))
                        turns += 1
                else:
                    print("Darn you missed :(")

            elif move == 4:
                klasi.Katana()
                print("----------------------------------------------")
                print("ULTIMATE ATTACK")
                print("----------------------------------------------")
                print("Damage:", klasi.damage)
                print("Accuracy:", klasi.accuracy)
                print("----------------------------------------------")
                if accuracyCount < klasi.accuracy:
                    fighter2lif = fighter2lif - klasi.damage
                    print("You hit!")
                    print("You call that a knife? This is a knife!")
                    print("You did", klasi.damage, "damage")
                else:
                    print("Darn you missed :(")

            else:
                move = int(input("Choose a move Player 1: "))


        elif fighter1 == "Viking":
            accuracyCount = randint(1, 100)
            klasi = Viking()
            print("----------------------------------------------")
            print("1.Axe:     (80% 60 DMG)")
            print("2.Life:    (60% 200+ health)")
            print("3.AxeThrow (50% 170 DMG)")
            print("4.Berzerk: (35% You hit your axe 2-6 times)")
            print("----------------------------------------------")

            move = int(input("Choose a move Player 1: "))

            if move == 1:
                klasi.Axe()
                print("----------------------------------------------")
                print("Damage:", klasi.damage)
                print("Accuracy:", klasi.accuracy)
                print("Hits:", klasi.hits)
                print("----------------------------------------------")
                if accuracyCount < klasi.accuracy:
                    fighter2lif = fighter2lif - klasi.damage
                    print("You hit!")
                    print("You did", klasi.damage, "damage")
                else:
                    print("Darn you missed :(")

            elif move == 2:
                klasi.Life()
                print("----------------------------------------------")
                print("Heal:", klasi.heal)
                print("Accuracy", klasi.accuracy)
                print("----------------------------------------------")
                if accuracyCount < klasi.accuracy:
                    fighter1lif = fighter1lif + klasi.heal
                    print("You hit!")
                    print("You healed", klasi.heal, "points")
                else:
                    print("Darn you missed :(")

            elif move == 3:
                klasi.AxeThrow()
                print("----------------------------------------------")
                print("Damage:", klasi.damage)
                print("Accuracy:", klasi.accuracy)
                print("Hits:", klasi.hits)
                print("----------------------------------------------")
                if accuracyCount < klasi.accuracy:
                    fighter2lif = fighter2lif - klasi.damage
                    print("You hit!")
                    print("You did", klasi.damage, "damage")
                else:
                    print("Darn you missed :(")

            elif move == 4:
                klasi.Berzerk()
                print("----------------------------------------------")
                print("ULTIMATE ATTACK")
                print("---------------")
                print("Damage:", klasi.damage)
                print("Accuracy:", klasi.accuracy)
                print("Hits:", klasi.hits)
                print("----------------------------------------------")
                if accuracyCount < klasi.accuracy:
                    fighter2lif = fighter2lif - (klasi.damage * klasi.hits)
                    print("You hit!")
                    print("Taste my steel, you foul beast!")
                    print("You did", klasi.damage * klasi.hits, "damage")
                else:
                    print("Darn you missed :(")

            else:
                move = int(input("Choose a move Player 1: "))


        elif fighter1 == "Wizard":
            accuracyCount = randint(1, 100)
            klasi = Wizard()
            print("----------------------------------------------")
            print("1.Fireball: (70% 170 DMG)")
            print("2.Freeze:   (50% Your opponent loses two turns)")
            print("3.Lightning: (50% 120 DMG 1-4 times)")
            print("4.Heal:     (40% 600+ health)")
            print("----------------------------------------------")

            move = int(input("Choose a move Player 1: "))

            if move == 1:
                klasi.Fireball()
                print("----------------------------------------------")
                print("Damage:", klasi.damage)
                print("Accuracy:", klasi.accuracy)
                print("Hits:", klasi.hits)
                print("----------------------------------------------")
                if accuracyCount < klasi.accuracy:
                    fighter2lif = fighter2lif - klasi.damage
                    print("You hit!")
                    print("You did", klasi.damage, "damage")
                else:
                    print("Darn you missed :(")

            elif move == 2:
                klasi.Freeze()
                print("Turns frozen:", klasi.sleep)
                print("Accuracy:", klasi.accuracy)
                if accuracyCount < klasi.accuracy:
                    turns = 1
                    while turns < 3:
                        accuracyCount = randint(1, 100)
                        klasi = Wizard()
                        print("----------------------------------------------")
                        print("1.Fireball: (70% 170 DMG)")
                        print("2.Freeze:   Not available")
                        print("3.Lightning: (50% 120 DMG 1-4 times)")
                        print("4.Heal:     (40% 600+ health)")
                        print("----------------------------------------------")

                        move = int(input("Choose a move Player 1: "))
                        if move == 1:
                            klasi.Fireball()
                            print("----------------------------------------------")
                            print("Damage:", klasi.damage)
                            print("Accuracy:", klasi.accuracy)
                            print("Hits:", klasi.hits)
                            print("----------------------------------------------")
                            if accuracyCount < klasi.accuracy:
                                fighter2lif = fighter2lif - klasi.damage
                                print("You hit!")
                                print("You did", klasi.damage, "damage")
                            else:
                                print("Darn you missed :(")

                        elif move == 2:
                            print("----------------------------------------------")
                            print("1.Fireball: (70% 170 DMG)")
                            print("2.Freeze:   Not available")
                            print("3.Lightning:(50% 120 DMG 1-4 times)")
                            print("4.Heal:     (40% 600+ health)")
                            print("----------------------------------------------")

                            move = int(input("Choose a move Player 1: "))

                        elif move == 3:
                            klasi.Lightning()
                            print("----------------------------------------------")
                            print("Damage:", klasi.damage)
                            print("Accuracy:", klasi.accuracy)
                            print("Hits:", klasi.hits)
                            print("----------------------------------------------")
                            if accuracyCount < klasi.accuracy:
                                fighter2lif = fighter2lif - (klasi.damage * klasi.hits)
                                print("You hit", klasi.hits, "times")
                                print("You did", klasi.damage, "damage")
                            else:
                                print("Darn you missed :(")

                        elif move == 4:
                            klasi.Heal()
                            print("----------------------------------------------")
                            print("ULTIMATE ATTACK")
                            print("----------------------------------------------")
                            print("Heal:", klasi.heal)
                            print("Accuracy:", klasi.accuracy)
                            print("----------------------------------------------")
                            if accuracyCount < klasi.accuracy:
                                fighter1lif = fighter1lif + klasi.heal
                                print("You hit!")
                                print("'That outta set you back a bit.'")
                                print("You healed", klasi.heal, "points")
                            else:
                                print("Darn you missed :(")

                        else:
                            move = int(input("Choose a move Player 1: "))

                        turns += 1
                else:
                    print("Darn you missed :(")

            elif move == 3:
                klasi.Lightning()
                print("----------------------------------------------")
                print("Damage:", klasi.damage)
                print("Accuracy:", klasi.accuracy)
                print("Hits:", klasi.hits)
                print("----------------------------------------------")
                if accuracyCount < klasi.accuracy:
                    fighter2lif = fighter2lif - (klasi.damage * klasi.hits)
                    print("You hit", klasi.hits, "times")
                    print("You did", klasi.damage, "damage")
                else:
                    print("Darn you missed :(")

            elif move == 4:
                klasi.Heal()
                print("----------------------------------------------")
                print("ULTIMATE ATTACK")
                print("----------------------------------------------")
                print("Heal:", klasi.heal)
                print("Accuracy:", klasi.accuracy)
                print("----------------------------------------------")
                if accuracyCount < klasi.accuracy:
                    fighter1lif = fighter1lif + klasi.heal
                    print("You hit!")
                    print("'That outta set you back a bit.'")
                    print("You healed", klasi.heal, "points")
                else:
                    print("Darn you missed :(")

            else:
                move = int(input("Choose a move Player 1: "))

        print("----------------------------------------------")
        print("Player 1:", fighter1)
        print("Player 1 Health:", fighter1lif)
        print("Player 2:", fighter2)
        print("Player 2 Health:", fighter2lif)
        print("----------------------------------------------")
        if fighter1lif < 0:
            break
        elif fighter2lif < 0:
            break
        time.sleep(2)



if fighter2lif < 1:
    print("Player 1 (",fighter1,"), you are the King of Ashkin!")
elif fighter1lif < 1:
    print("Player 2 (",fighter2,") you are the King of Ashkin!")