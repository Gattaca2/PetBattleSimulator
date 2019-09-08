from pettype import *
from ability import *
import math

"""
BREED     LETTERS     H/P/S
 3/13   →   B/B   =   5/5/5
 4/14   →   P/P   =   0/20/0
 5/15   →   S/S   =   0/0/20
 6/16   →   H/H   =   20/0/0
 7/17   →   H/P   =   9/9/0
 8/18   →   P/S   =   0/9/9
 9/19   →   H/S   =   9/0/9
10/20   →   P/B   =   4/9/4
11/21   →   S/B   =   4/4/9
12/22   →   H/B   =   9/4/4
"""
BREED = {
    "HEALTH": {
        "B/B": 5,
        "3": 5,
        "13": 5,
        "P/P": 0,
        "4": 0,
        "14": 0,
        "S/S": 0,
        "5": 0,
        "15": 0,
        "H/H": 20,
        "6": 20,
        "16": 20,
        "H/P": 9,
        "7": 9,
        "17": 9,
        "P/S": 0,
        "8": 0,
        "18": 0,
        "H/S": 9,
        "9": 9,
        "19": 9,
        "P/B": 4,
        "10": 4,
        "20": 4,
        "S/B": 4,
        "11": 4,
        "21": 4,
        "H/B": 9,
        "12": 9,
        "22": 9,
    },
    "POWER": {
        "B/B": 5,
        "3": 5,
        "13": 5,
        "P/P": 20,
        "4": 20,
        "14": 20,
        "S/S": 0,
        "5": 0,
        "15": 0,
        "H/H": 0,
        "6": 0,
        "16": 0,
        "H/P": 9,
        "7": 9,
        "17": 9,
        "P/S": 9,
        "8": 9,
        "18": 9,
        "H/S": 0,
        "9": 0,
        "19": 0,
        "P/B": 9,
        "10": 9,
        "20": 9,
        "S/B": 4,
        "11": 4,
        "21": 4,
        "H/B": 4,
        "12": 4,
        "22": 4,
    },
    "SPEED": {
        "B/B": 5,
        "3": 5,
        "13": 5,
        "P/P": 0,
        "4": 0,
        "14": 0,
        "S/S": 20,
        "5": 20,
        "15": 20,
        "H/H": 0,
        "6": 0,
        "16": 0,
        "H/P": 0,
        "7": 0,
        "17": 0,
        "P/S": 9,
        "8": 9,
        "18": 9,
        "H/S": 9,
        "9": 9,
        "19": 9,
        "P/B": 4,
        "10": 4,
        "20": 4,
        "S/B": 9,
        "11": 9,
        "21": 9,
        "H/B": 4,
        "12": 4,
        "22": 4,
    },
}


class Pet:

    name = None
    pet_type = None
    id = None
    breed = None
    quality = None
    elite = None
    level = None
    played = False
    alive = True

    # This is the basic stat allotment each pet has. For the majority of player
    # aquirable pets, this will sum to 24. Generally will be a multiple of 0.25
    # Zoom and Elekk Plushie are notable exceptions, as well as nearly all NPC
    # pets
    health_stat = None
    power_stat = None
    speed_stat = None

    # These are the actual numbers you see when you level a pet. For example,
    # Boneshard at lvl 25 and rare quality has 1481 health, 276 power, 276
    # health. Some attacks and auras will modify these values.
    leveled_health = None
    leveled_power = None
    leveled_speed = None

    # These are the values used in a battle. They can be modified by attacks
    # and auras.
    current_health = None
    current_power = None
    current_speed = None

    ability_1_choices = [None]
    ability_2_choices = [None]
    ability_3_choices = [None]

    ability_1 = None
    ability_1_name = None
    ability_1_id = None
    ability_2 = None
    ability_2_name = None
    ability_2_id = None
    ability_3 = None
    ability_3_name = None
    ability_3_id = None

    def __init__(self, breed="B/B", quality=1.0, level=1, health=None):

        # Calculate how much health/power/speed pet has at this level/breed/quality
        # These will be static and unchanging throughout the fight
        self.leveled_health = self.calculate_health(breed, quality, level)
        self.leveled_power = self.calculate_power(breed, quality, level)
        self.leveled_speed = self.calculate_speed(breed, quality, level)

        # Mutable values. health will change as damaged, speed can be boosted / retarded
        self.current_health = self.leveled_health
        self.current_power = self.leveled_power
        self.current_speed = self.leveled_speed

        # Print the values for a sanity check
        print(
            "name: {}\nhealth: {}\npower: {}\nspeed: {}\n".format(
                self.name, self.leveled_health, self.leveled_power, self.leveled_speed
            )
        )

    def calculate_health(self, breed, quality, level):
        # Calculate health based on level, quality, and breed
        # the 5, 10, and 100 here are just magic numbers from WoW calculations
        temp_health = (
            (self.health_stat + (BREED["HEALTH"][breed] / 10)) * 5 * level * quality
        ) + 100

        # oddly, it rounds up only if its above 0.5
        if temp_health - math.trunc(temp_health) > 0.5:
            temp_health = math.ceil(temp_health)
        else:
            temp_health = math.floor(temp_health)

        return temp_health

    def calculate_power(self, breed, quality, level):
        # Calculate power based on level, quality, and breed
        temp_power = (self.power_stat + (BREED["POWER"][breed] / 10)) * level * quality

        if temp_power - math.trunc(temp_power) > 0.5:
            temp_power = math.ceil(temp_power)
        else:
            temp_power = math.floor(temp_power)

        return temp_power

    def calculate_speed(self, breed, quality, level):
        # Calculate speed based on level, quality, and breed
        temp_speed = (self.speed_stat + (BREED["SPEED"][breed] / 10)) * level * quality

        if temp_speed - math.trunc(temp_speed) > 0.5:
            temp_speed = math.ceil(temp_speed)
        else:
            temp_speed = math.floor(temp_speed)

        return temp_speed

    def use_ability(self, ability):
        power = self.get_power()

        if (
            ability == self.ability_1_name
            or ability == self.ability_1_id
            or ability == "#1"
        ):
            return self.ability_1.use(power)
        elif (
            ability == self.ability_2_name
            or ability == self.ability_2_id
            or ability == "#2"
        ):
            return self.ability_2.use(power)
        elif (
            ability == self.ability_3_name
            or ability == self.ability_3_id
            or ability == "#3"
        ):
            return self.ability_3.use(power)
        else:
            print("error in use_ability")

    def receive_attack(self, attack_object):
        pass

    def get_name(self):
        return self.name

    def get_health(self):
        return self.current_health

    def get_power(self):
        return self.current_power

    def get_speed(self):
        return self.current_speed

    def is_alive(self):
        return self.alive

    def is_played(self):
        return self.played

    def set_played(self):
        self.played = True


class Prototype_Annoy_O_Tron(Pet):
    """ 
    1. annoying shield
    2. sonic detonator
    3. sonic blast
    4. sonic blast
    5. sonic blast
    6. annoying shield
    7. sonic detonator
    8. sonic blast
    9. sonic blast
    10. sonic blast
    11. annoying shield
    """

    name = "Prototype Annoy-O-Tron"
    pet_type = PetType.MECHANICAL
    id = 146001
    elite = True

    health_stat = 12.73
    power_stat = 7.1
    speed_stat = 8

    ability_1 = Sonic_Blast()
    ability_2 = Sonic_Detonator()
    ability_3 = Annoying_Shield()


class Boneshard(Pet):

    name = "Boneshard"
    pet_type = PetType.UNDEAD
    id = 115146

    # 1.0 = poor, 1.1 = common, 1.2 = uncommon, 1.3 = rare, 1.4 = epic, 1.5 = legendary

    health_stat = 8
    power_stat = 8
    speed_stat = 8

    ability_1_choices = [Chop(1), Bonestorm(10)]
    ability_2_choices = [Blistering_Cold(2), Bonestorm(15)]
    ability_3_choices = [Ice_Spike(4), Bonestorm(20)]

    ability_1 = ability_1_choices[0]
    ability_2 = ability_2_choices[0]
    ability_3 = ability_3_choices[0]


class Ikky(Pet):

    name = "Ikky"
    pet_type = PetType.FLYING
    id = 86447
    quality = 1.3
    breed = "P/S"
    level = 25

    health_stat = 7.5
    power_stat = 9
    speed_stat = 7.5

    ability_1 = Quills()
    ability_2 = Black_Claw()
    ability_3 = Flock()


class Soul_of_the_Forge(Pet):

    name = "Soul of the Forge"
    pet_type = PetType.ELEMENTAL
    id = 84853
    quality = 1.3
    breed = "H/P"
    level = 25

    health_stat = 9.75
    power_stat = 7.25
    speed_stat = 7

    ability_1 = Sulfuras_Smash()
    ability_2 = Extra_Plating()
    ability_3 = Reforge()
