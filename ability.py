from pettype import *
from aura import *
import math


class Ability:

    name = None
    level = None
    ability_type = None
    accuracy = None  # hit chance
    cooldown = None
    cooldown_remaining = None
    goes_first = False
    multiturn = False
    turns_remaining = None
    split_damage = False
    split_healing = False

    def __init__(self, level=None):
        if level != None:
            self.level = level

    def use(self, power, enemy_team_size=None, friendly_team_size=None):
        if self.get_cooldown() != None:
            self.cooldown_remaining = cooldown

        return {
            "ability_name": self.get_name(),
            "level": self.get_level(),
            "ability_type": self.get_ability_type(),
            "accuracy": self.get_accuracy(),
            "cooldown": self.get_cooldown(),
            "cooldown_remaining": self.get_cooldown_remaining(),
            "frontline_healing": self.calculate_frontline_healing(power),
            "backline_healing": self.calculate_backline_healing(power),
            "frontline_damage": self.calculate_frontline_damage(power),
            "backline_damage": self.calculate_backline_damage(power),
            "goes_first": self.get_goes_first(),
            "multiturn": self.get_multiturn(),
            "turns_remaining": self.get_turns_remaining(),
            "enemy_pet_aura": self.enemy_pet_aura(power),
            "enemy_team_aura": self.enemy_team_aura(power),
            "friendly_pet_aura": self.friendly_pet_aura(power),
            "friendly_team_aura": self.friendly_team_aura(power),
            "split_damage": self.get_split_damage(),
            "split_healing": self.get_split_healing(),
            "standby": False,
        }

    def get_name(self):
        return self.name

    def get_level(self):
        return self.level

    def get_ability_type(self):
        return self.ability_type

    def get_accuracy(self):
        return self.accuracy

    def get_cooldown(self):
        return self.cooldown

    def get_cooldown_remaining(self):
        return self.cooldown_remaining

    def decrement_cooldown_remaining(self):
        self.cooldown_remaining -= 1

    def get_goes_first(self):
        return self.goes_first

    def get_multiturn(self):
        return self.multiturn

    def get_turns_remaining(self):
        return self.turns_remaining

    def decrement_turns_remaining(self):
        self.turns_remaining -= 1

    def get_split_damage(self):
        return self.split_damage

    def get_split_healing(self):
        return self.split_healing

    def enemy_pet_aura(self, power):
        return None

    def enemy_team_aura(self, power):
        return None

    def friendly_pet_aura(self, power):
        return None

    def friendly_team_aura(self, power):
        return None

    def calculate_frontline_healing(self, power):
        return None

    def calculate_backline_healing(self, power):
        return None

    def calculate_frontline_damage(self, power):
        return None

    def calculate_backline_damage(self, power):
        return None


class Chop(Ability):

    name = "Chop"
    ability_type = PetType.MECHANICAL
    accuracy = 1.0  # hit chance

    def calculate_frontline_damage(self, power):

        return {
            "strong": round((10 + power / 2) * 1.5),
            "normal": round(10 + power / 2),
            "weak": round((10 + power / 2) * 0.66),
        }

    def enemy_pet_aura(self, power):
        # bleed = (5 + power/4) # bleed for 5 rounds
        return Bleed(round(5 + power / 4), 5)


class Blistering_Cold(Ability):
    # priority
    ability_type = PetType.ELEMENTAL
    cooldown = 2
    accuracy = 1.0
    damage = 411


class Ice_Spike(Ability):
    # priority
    ability_type = PetType.ELEMENTAL
    cooldown = 2


class Sonic_Blast(Ability):

    ability_type = PetType.ELEMENTAL
    accuracy = 1.0

    def calculate_frontline_damage(self, power):

        return {
            "strong": round((25 + power * 1.275) * 1.5),
            "normal": round(25 + power * 1.275),
            "weak": round((25 + power * 1.275) * 0.66),
        }


class Sonic_Detonator(Ability):
    # priority
    ability_type = PetType.MECHANICAL
    accuracy = 1.0
    # 247 power

    def calculate_frontline_damage(self, power):

        # 408 (strong)
        # 272 normal
        # 179 (weak)
        return {
            "strong": round((20 + power * 1.02) * 1.5),
            "normal": round(20 + power * 1.02),
            "weak": round((20 + power * 1.02) * 0.66),
        }

    def calculate_backline_damage(self, power):

        # 179 (strong)(critical)
        # 102 (strong)
        # 68 normal
        # 44 (weak)
        return {
            "strong": round((5 + power * 0.255) * 1.5),
            "normal": round(5 + power * 0.255),
            "weak": round((5 + power * 0.255) * 0.66),
        }


class Annoying_Shield(Ability):
    # priority
    ability_type = PetType.MECHANICAL


class Quills(Ability):
    # don't bother
    ability_type = PetType.MECHANICAL


class Black_Claw(Ability):
    # priority
    ability_type = PetType.MECHANICAL


class Flock(Ability):
    # priority
    ability_type = PetType.MECHANICAL


class Sulfuras_Smash(Ability):
    # don't bother
    ability_type = PetType.MECHANICAL


class Extra_Plating(Ability):
    # don't bother
    ability_type = PetType.MECHANICAL


class Reforge(Ability):
    # don't bother
    ability_type = PetType.MECHANICAL


class Bonestorm(Ability):
    # don't bother
    ability_type = PetType.MECHANICAL


# ice spike, blistering cold, chop, pass, black claw, flock, Sonic_Blast, Sonic_Detonator, Annoying_Shield
