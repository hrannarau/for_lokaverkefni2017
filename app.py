#Hrannar Helgi Auðunsson og Magnús Dagur Jóhannesson
from random import *

class Ninja():
    lif = 1800
    def __init__(self,heal,dead,sleep,shield,damage,hits,accuracy):
        self.heal = heal
        self.dead = dead
        self.sleep = sleep
        self.shield = shield
        self.damage = damage
        self.hits = hits
        self.accuracy = accuracy
    def Kick(self):
        
        self.heal = 0
        self.dead = 0
        self.sleep = 0
        self.shield = 0
        self.damage = 150
        self.hits = 1
        self.accuracy = 70
    def Ninjastar(self):
        
        self.heal = 0
        self.dead = 0
        self.sleep = 0
        self.shield = 0
        self.damage = 60
        self.hits = randint(2,5)
        self.accuracy = 50
    def Sleep(self):
        
        self.heal = 0
        self.dead = 0
        self.sleep = 2
        self.shield = 0
        self.damage = 0
        self.hits = 1
        self.accuracy = 60
    def Katana(self):
        
        self.heal = 0
        self.dead = 0
        self.sleep = 0
        self.shield = 0
        self.damage = 675
        self.hits = 1
        self.accuracy = 25

class Viking():
    lif = 3600
    def __init__(self,heal,dead,sleep,shield,damage,hits,accuracy):
        self.heal = heal
        self.dead = dead
        self.sleep = sleep
        self.shield = shield
        self.damage = damage
        self.hits = hits
        self.accuracy = accuracy
    def Axe(self):
        
        self.heal = 0
        self.dead = 0
        self.sleep = 0
        self.shield = 0
        self.damage = 60
        self.hits = 1
        self.accuracy = 80
    def Life(self):
        
        self.heal = 200
        self.dead = 0
        self.sleep = 0
        self.shield = 0
        self.damage = 0
        self.hits = 1
        self.accuracy = 60
    def Shield(self):
        
        self.heal = 0
        self.dead = 0
        self.sleep = 0
        self.shield = randint(1,3)
        self.damage = 0
        self.hits = 1
        self.accuracy = 40
    def Berzerk(self):
        
        self.heal = 0
        self.dead = 0
        self.sleep = 0
        self.shield = 0
        self.damage = 60
        self.hits = randint(2,6)
        self.accuracy = 35

class Wizard():
    lif = 1500
    def __init__(self,heal,dead,sleep,shield,damage,hits,accuracy):
        self.heal = heal
        self.dead = dead
        self.sleep = sleep
        self.shield = shield
        self.damage = damage
        self.hits = hits
        self.accuracy = accuracy
    def Fireball(self):
        
        self.heal = 0
        self.dead = 0
        self.sleep = 0
        self.shield = 0
        self.damage = 170
        self.hits = 1
        self.accuracy = 70
    def Freeze(self):
        
        self.heal = 0
        self.dead = 0
        self.sleep = 2
        self.shield = 0
        self.damage = 0
        self.hits = 1
        self.accuracy = 50
    def Lightning(self):
        
        self.heal = 0
        self.dead = 0
        self.sleep = 0
        self.shield = 0
        self.damage = 120
        self.hits = 1
        self.accuracy = 50
    def Heal(self):
        
        self.heal = 600
        self.dead = 0
        self.sleep = 0
        self.shield = 0
        self.damage = 0
        self.hits = 1
        self.accuracy = 40

class Soldier():
    lif = 2400
    def __init__(self,heal,dead,sleep,shield,damage,hits,accuracy):
        self.heal = heal
        self.dead = dead
        self.sleep = sleep
        self.shield = shield
        self.damage = damage
        self.hits = hits
        self.accuracy = accuracy
    def Knife(self):
        
        self.heal = 0
        self.dead = 0
        self.sleep = 0
        self.shield = 0
        self.damage = 70
        self.hits = 1
        self.accuracy = 100
    def MachineGun(self):
        
        self.heal = 0
        self.dead = 0
        self.sleep = 0
        self.shield = 0
        self.damage = 220
        self.hits = 1
        self.accuracy = 40
    def Grenade(self):
        
        self.heal = 0
        self.dead = 0
        self.sleep = 0
        self.shield = 0
        self.damage = 200
        self.hits = 1
        self.accuracy = 50
    def MissileStrike(self):
        
        self.heal = 0
        self.dead = 0
        self.sleep = 0
        self.shield = 0
        self.damage = 70
        self.hits = randint(2,10)
        self.accuracy = 40

class Pirate():
    lif = 2000
    def __init__(self,heal,dead,sleep,shield,damage,hits,accuracy):
        self.heal = heal
        self.dead = dead
        self.sleep = sleep
        self.shield = shield
        self.damage = damage
        self.hits = hits
        self.accuracy = accuracy
    def Cutlass(self):
        
        self.heal = 0
        self.dead = 0
        self.sleep = 0
        self.shield = 0
        self.damage = 150
        self.hits = 1
        self.accuracy = 60
    def CaptainsPlunder(self):
        
        self.heal = 0
        self.dead = 0
        self.sleep = 2
        self.shield = 0
        self.damage = 0
        self.hits = 1
        self.accuracy = 60
    def Cannon(self):
        
        self.heal = 0
        self.dead = 0
        self.sleep = 0
        self.shield = 0
        self.damage = 40
        self.hits = randint(2,7)
        self.accuracy = 60
    def WalkthePlank(self):
        
        self.heal = 0
        self.dead = 1
        self.sleep = 0
        self.shield = 0
        self.damage = 0
        self.hits = 1
        self.accuracy = 60

class Ogre():
    lif = 4500
    def __init__(self,heal,dead,sleep,shield,damage,hits,accuracy):
        self.heal = heal
        self.dead = dead
        self.sleep = sleep
        self.shield = shield
        self.damage = damage
        self.hits = hits
        self.accuracy = accuracy
    def Jab(self):
        
        self.heal = 0
        self.dead = 0
        self.sleep = 0
        self.shield = 0
        self.damage = 180
        self.hits = 1
        self.accuracy = 40
    def Roar(self):
        
        self.heal = 0
        self.dead = 0
        self.sleep = 0
        self.shield = 0
        self.damage = 70
        self.hits = 1
        self.accuracy = 90
    def Slam(self):
        
        self.heal = 0
        self.dead = 0
        self.sleep = 0
        self.shield = 0
        self.damage = 220
        self.hits = 1
        self.accuracy = 30
    def Rampage(self):
        
        self.heal = 0
        self.dead = 0
        self.sleep = 0
        self.shield = 0
        self.damage = 180
        self.hits = randint(1,5)
        self.accuracy = 25

class Dragonborn():
    lif = 2020
    def __init__(self,heal,dead,sleep,shield,damage,hits,accuracy):
        self.heal = heal
        self.dead = dead
        self.sleep = sleep
        self.shield = shield
        self.damage = damage
        self.hits = hits
        self.accuracy = accuracy
    def FireBreath(self):
        
        self.heal = 0
        self.dead = 0
        self.sleep = 0
        self.shield = 0
        self.damage = 135
        self.hits = 1
        self.accuracy = 70
    def IceBreath(self):
        
        self.heal = 0
        self.dead = 0
        self.sleep = 2
        self.shield = 0
        self.damage = 0
        self.hits = 1
        self.accuracy = 60
    def FastAttack(self):
        
        self.heal = 0
        self.dead = 0
        self.sleep = 0
        self.shield = 0
        self.damage = 60
        self.hits = randint(2,5)
        self.accuracy = 50
    def UnrealentingForce(self):
        
        self.heal = 0
        self.dead = 0
        self.sleep = 0
        self.shield = 0
        self.damage = 450
        self.hits = 1
        self.accuracy = 40

class Zombie():
    lif = 1000
    def __init__(self,heal,dead,sleep,shield,damage,hits,accuracy):
        self.heal = heal
        self.dead = dead
        self.sleep = sleep
        self.shield = shield
        self.damage = damage
        self.hits = hits
        self.accuracy = accuracy
    def Scratch(self):
        
        self.heal = 0
        self.dead = 0
        self.sleep = 0
        self.shield = 0
        self.damage = 60
        self.hits = 1
        self.accuracy = 80
    def Bite(self):
        
        self.heal = 0
        self.dead = 0
        self.sleep = 0
        self.shield = 0
        self.damage = 310
        self.hits = 1
        self.accuracy = 55
    def Bloodlust(self):
        
        self.heal = 200
        self.dead = 0
        self.sleep = 0
        self.shield = 0
        self.damage = 100
        self.hits = randint(1,4)
        self.accuracy = 40
    def Brains(self):
        
        self.heal = 0
        self.dead = 1
        self.sleep = 0
        self.shield = 0
        self.damage = 0
        self.hits = 1
        self.accuracy = 99

class RockGolem():
    lif = 5000
    def __init__(self,heal,dead,sleep,shield,damage,hits,accuracy):
        self.heal = heal
        self.dead = dead
        self.sleep = sleep
        self.shield = shield
        self.damage = damage
        self.hits = hits
        self.accuracy = accuracy
    def BolderToss(self):
        
        self.heal = -120
        self.dead = 0
        self.sleep = 0
        self.shield = 0
        self.damage = 120
        self.hits = 1
        self.accuracy = 70
    def Earthquake(self):
        
        self.heal = 0
        self.dead = 0
        self.sleep = 2
        self.shield = 0
        self.damage = 0
        self.hits = 1
        self.accuracy = 50
    def Stomp(self):
        
        self.heal = 0
        self.dead = 0
        self.sleep = 0
        self.shield = 0
        self.damage = 300
        self.hits = 1
        self.accuracy = 60
    def Rebuild(self):
        
        self.heal = 800
        self.dead = 0
        self.sleep = 0
        self.shield = 0
        self.damage = 310
        self.hits = 1
        self.accuracy = 35

class Clown():
    lif = 2600
    def __init__(self,heal,dead,sleep,shield,damage,hits,accuracy):
        self.heal = heal
        self.dead = dead
        self.sleep = sleep
        self.shield = shield
        self.damage = damage
        self.hits = hits
        self.accuracy = accuracy
    def PieFace(self):
        
        self.heal = 0
        self.dead = 0
        self.sleep = 0
        self.shield = 0
        self.damage = 100
        self.hits = 1
        self.accuracy = 90
    def Spook(self):
        
        self.heal = 0
        self.dead = 0
        self.sleep = 2
        self.shield = 0
        self.damage = 0
        self.hits = 1
        self.accuracy = 50
    def FlowerSplash(self):
        self.heal = 0
        self.dead = 0
        self.sleep = 0
        self.shield = 0
        self.damage = 50
        self.hits = randint(2,5)
        self.accuracy = 75
        attributeList = [self.heal,self.dead,self.sleep,self.shield,self.damage,self.hits,self.accuracy]
        for i in attributeList:
            if i != 0:
                print(i)
    def YoullFloatToo(self):
        
        self.heal = 0
        self.dead = 1
        self.sleep = 0
        self.shield = 0
        self.damage = 0
        self.hits = 1
        self.accuracy = 60

'''print("-----------------")
print("Welcome to Ashkin")
print(" 1. Ninja")
print(" 2. Viking")
print(" 3. Wizard")
print(" 4. Soldier")
print(" 5. Pirate")
print(" 6. Oger")
print(" 7. Dragonborn")
print(" 8. Zombie")
print(" 9. Rock Golem")
print("10. Clown")
fighter1 = input("Player 1: choose your fighter: ")
fighter2 = input("Player 2: choose your fighter: ")
start = random.randint(1,2)
print("Player",start,"begins")'''


clown = "Clown:\n1.Pieface\n2.Spook\n3.FlowerSplash\n4.ULTIMATE - You'll Float Too"

a = Clown(0,0,0,0,0,0,0)

print(clown)
val = int(input("Choose a move: "))
if val == 1:
