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

    def __init__(this, pet_id=None, breed=None, quality=None, level=None):
        # Calculate health based on level, quality, and breed
        # the 5, 10, and 100 here are just magic numbers from WoW calculations
        temp_health = (
            (this.health_stat + (BREED["HEALTH"][this.breed] / 10))
            * 5
            * this.level
            * this.quality
        ) + 100

        # oddly, it rounds up only if its above 0.5
        if temp_health - math.trunc(temp_health) > 0.5:
            this.leveled_health = math.ceil(temp_health)
        else:
            this.leveled_health = math.floor(temp_health)

        # Calculate power based on level, quality, and breed
        temp_power = (
            (this.power_stat + (BREED["POWER"][this.breed] / 10))
            * this.level
            * this.quality
        )

        if temp_power - math.trunc(temp_power) > 0.5:
            this.leveled_power = math.ceil(temp_power)
        else:
            this.leveled_power = math.floor(temp_power)

        # Calculate speed based on level, quality, and breed
        temp_speed = (
            (this.power_stat + (BREED["SPEED"][this.breed] / 10))
            * this.level
            * this.quality
        )

        if temp_speed - math.trunc(temp_speed) > 0.5:
            this.leveled_speed = math.ceil(temp_speed)
        else:
            this.leveled_speed = math.floor(temp_speed)

        # Print the values for a sanity check
        print(
            "health: {}\npower: {}\nspeed: {}\n".format(
                this.leveled_health, this.leveled_power, this.leveled_speed
            )
        )

    def receive_attack(attack_object):
        pass


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

    health_stat = 2250
    power_stat = 247
    speed_stat = 276

    ability_1 = Sonic_Blast()
    ability_2 = Sonic_Detonator()
    ability_3 = Annoying_Shield()


class Boneshard(Pet):

    name = "Boneshard"
    pet_type = PetType.ELEMENTAL
    id = 115146
    quality = (
        1.3
    )  # 1.0 = poor, 1.1 = common, 1.2 = uncommon, 1.3 = rare, 1.4 = epic, 1.5 = legendary
    breed = "B/B"
    level = 25

    health_stat = 8
    power_stat = 8
    speed_stat = 8

    ability_1 = Chop()
    ability_2 = Blistering_Cold()
    ability_3 = Ice_Spike()
