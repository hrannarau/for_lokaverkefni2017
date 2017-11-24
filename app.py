#Hrannar Helgi Auðunsson og Magnús Dagur Jóhannesson
from random import *

def Ninja():
    lif = 1800
    def Kick():
        mime = 0
        heal = 0
        dead = 0
        sleep = 0
        shield = 0
        damage = 150
        hits = 1
        accuracy = 70
    def Ninjastar():
        mime = 0
        heal = 0
        dead = 0
        sleep = 0
        shield = 0
        damage = 60
        hits = randint(2,5)
        accuracy = 50
    def Sleep():
        mime = 0
        heal = 0
        dead = 0
        sleep = 2
        shield = 0
        damage = 0
        hits = 1
        accuracy = 60
    def Katana():
        mime = 0
        heal = 0
        dead = 0
        sleep = 0
        shield = 0
        damage = 675
        hits = 1
        accuracy = 25

def Viking():
    lif = 3600
    def Axe():
        mime = 0
        heal = 0
        dead = 0
        sleep = 0
        shield = 0
        damage = 60
        hits = 1
        accuracy = 80
    def Life():
        mime = 0
        heal = 200
        dead = 0
        sleep = 0
        shield = 0
        damage = 0
        hits = 1
        accuracy = 60
    def Shield():
        mime = 0
        heal = 0
        dead = 0
        sleep = 0
        shield = randint(1,3)
        damage = 0
        hits = 1
        accuracy = 40
    def Berzerk():
        mime = 0
        heal = 0
        dead = 0
        sleep = 0
        shield = 0
        damage = 60
        hits = randint(2,6)
        accuracy = 35

def Wizard():
    lif = 1500
    def Fireball():
        mime = 0
        heal = 0
        dead = 0
        sleep = 0
        shield = 0
        damage = 170
        hits = 1
        accuracy = 70
    def Freeze():
        mime = 0
        heal = 0
        dead = 0
        sleep = 2
        shield = 0
        damage = 0
        hits = 1
        accuracy = 50
    def Lightning():
        mime = 0
        heal = 0
        dead = 0
        sleep = 0
        shield = 0
        damage = 120
        hits = 1
        accuracy = 50
    def Heal():
        mime = 0
        heal = 600
        dead = 0
        sleep = 0
        shield = 0
        damage = 0
        hits = 1
        accuracy = 40

def Soldier():
    lif = 2400
    def Knife():
        mime = 0
        heal = 0
        dead = 0
        sleep = 0
        shield = 0
        damage = 70
        hits = 1
        accuracy = 100
    def MachineGun():
        mime = 0
        heal = 0
        dead = 0
        sleep = 0
        shield = 0
        damage = 220
        hits = 1
        accuracy = 40
    def Grenade():
        mime = 0
        heal = 0
        dead = 0
        sleep = 0
        shield = 0
        damage = 200
        hits = 1
        accuracy = 50
    def MissileStrike():
        mime = 0
        heal = 0
        dead = 0
        sleep = 0
        shield = 0
        damage = 70
        hits = randint(2,10)
        accuracy = 40

def Pirate():
    lif = 2000
    def Cutlass():
        mime = 0
        heal = 0
        dead = 0
        sleep = 0
        shield = 0
        damage = 150
        hits = 1
        accuracy = 60
    def CaptainsPlunder():
        mime = 0
        heal = 0
        dead = 0
        sleep = 2
        shield = 0
        damage = 0
        hits = 1
        accuracy = 60
    def Cannon():
        mime = 0
        heal = 0
        dead = 0
        sleep = 0
        shield = 0
        damage = 40
        hits = randint(2,7)
        accuracy = 60
    def WalkthePlank():
        mime = 0
        heal = 0
        dead = 1
        sleep = 0
        shield = 0
        damage = 0
        hits = 1
        accuracy = 60

def Ogre():
    lif = 4500
    def Jab():
        mime = 0
        heal = 0
        dead = 0
        sleep = 0
        shield = 0
        damage = 180
        hits = 1
        accuracy = 40
    def Roar():
        mime = 0
        heal = 0
        dead = 0
        sleep = 0
        shield = 0
        damage = 70
        hits = 1
        accuracy = 90
    def Slam():
        mime = 0
        heal = 0
        dead = 0
        sleep = 0
        shield = 0
        damage = 220
        hits = 1
        accuracy = 30
    def Rampage():
        mime = 0
        heal = 0
        dead = 0
        sleep = 0
        shield = 0
        damage = 180
        hits = randint(1,5)
        accuracy = 25

def Dragonborn():
    lif = 2020
    def FireBreath():
        mime = 0
        heal = 0
        dead = 0
        sleep = 0
        shield = 0
        damage = 135
        hits = 1
        accuracy = 70
    def IceBreath():
        mime = 0
        heal = 0
        dead = 0
        sleep = 2
        shield = 0
        damage = 0
        hits = 1
        accuracy = 60
    def FastAttack():
        mime = 0
        heal = 0
        dead = 0
        sleep = 0
        shield = 0
        damage = 60
        hits = randint(2,5)
        accuracy = 50
    def UnrealentingForce():
        mime = 0
        heal = 0
        dead = 0
        sleep = 0
        shield = 0
        damage = 450
        hits = 1
        accuracy = 40

def Zombie():
    lif = 1000
    def Scratch():
        mime = 0
        heal = 0
        dead = 0
        sleep = 0
        shield = 0
        damage = 60
        hits = 1
        accuracy = 80
    def Bite():
        mime = 0
        heal = 0
        dead = 0
        sleep = 0
        shield = 0
        damage = 310
        hits = 1
        accuracy = 55
    def Bloodlust():
        mime = 0
        heal = 200
        dead = 0
        sleep = 0
        shield = 0
        damage = 100
        hits = randint(1,4)
        accuracy = 40
    def Brains():
        mime = 0
        heal = 0
        dead = 1
        sleep = 0
        shield = 0
        damage = 0
        hits = 1
        accuracy = 99

def RockGolem():
    lif = 5000
    def BolderToss():
        mime = 0
        heal = -120
        dead = 0
        sleep = 0
        shield = 0
        damage = 120
        hits = 1
        accuracy = 70
    def Earthquake():
        mime = 0
        heal = 0
        dead = 0
        sleep = 2
        shield = 0
        damage = 0
        hits = 1
        accuracy = 50
    def Stomp():
        mime = 0
        heal = 0
        dead = 0
        sleep = 0
        shield = 0
        damage = 300
        hits = 1
        accuracy = 60
    def Rebuild():
        mime = 0
        heal = 800
        dead = 0
        sleep = 0
        shield = 0
        damage = 310
        hits = 1
        accuracy = 35

def Clown():
    lif = 2600
    def PieFace():
        mime = 0
        heal = 0
        dead = 0
        sleep = 0
        shield = 0
        damage = 100
        hits = 1
        accuracy = 90
    def Spook():
        mime = 0
        heal = 0
        dead = 0
        sleep = 2
        shield = 0
        damage = 0
        hits = 1
        accuracy = 50
    def Mime():
        mime = 1
        heal = 0
        dead = 0
        sleep = 0
        shield = 0
        damage = 0
        hits = 1
        accuracy = 75
    def YoullFloatToo():
        mime = 0
        heal = 0
        dead = 1
        sleep = 0
        shield = 0
        damage = 0
        hits = 1
        accuracy = 60