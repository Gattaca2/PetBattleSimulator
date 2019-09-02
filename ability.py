from pettype import *


class Ability:

    ability_type = None
    accuracy = None  # hit chance
    cooldown = None
    cooldown_remaining = None
    healing = None
    damage = None
    level = None
    goes_first = False
    apply_aura = False

    # damage to only the frontline pet
    # major damage to frontline pet, minor damage to backline pet
    # damage split between all pets

    def attack(power):
        pass


class Aura:

    ability_type = None
    cooldown_remaining = None


class Blistering_Cold_Aura(Aura):

    ability_type = PetType.ELEMENTAL
    cooldown_remaining = 3


class Bleed(Aura):

    ability_type = PetType.ELEMENTAL
    cooldown_remaining = 3


class Chop(Ability):

    ability_type = PetType.MECHANICAL
    accuracy = 1.0
    multiturn = False
    apply_aura = True
    aura = [Bleed]
    # damage = int(10 + power/2)
    # bleed = int(5 + power/4) # bleed for 5 rounds

    def attack(self, power):
        return {
            "ability_type": self.ability_type,
            "frontline_damage": {"strong": 0, "normal": int(10 + power / 2), "weak": 0},
            "backline_damage": {"strong": 0, "normal": int(10 + power / 2), "weak": 0},
            "multiturn": self.multiturn,
            "accuracy": self.accuracy,
            "apply_aura": self.apply_aura,
            "aura": self.aura,
        }


class Blistering_Cold(Ability):

    ability_type = PetType.ELEMENTAL
    cooldown = 2
    accuracy = 1.0
    damage = 411


class Ice_Spike(Ability):

    ability_type = PetType.ELEMENTAL
    cooldown = 2


class Sonic_Blast(Ability):

    ability_type = PetType.ELEMENTAL
    accuracy = 1.0
    damage = 411


class Sonic_Detonator(Ability):

    ability_type = PetType.MECHANICAL
    accuracy = 1.0


class Annoying_Shield(Ability):

    ability_type = PetType.MECHANICAL
