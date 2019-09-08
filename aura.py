from pettype import *
import math


class Aura:

    ability_type = None
    accuracy = None
    turns_total = None
    turns_remaining = None
    max_stacks = None
    refresh = False
    damage = None
    healing = None

    def __init__(self, damage, duration):
        self.turns_total = duration
        self.turns_remaining = self.turns_total
        self.damage = damage

    def on_apply(self):
        pass

    def on_fade(self):
        pass

    def per_turn(self):
        pass

    def decrement_turns(self):
        self.turns_remaining -= 1
        if self.turns_remaining <= 0:
            return False
        else:
            return True

    def refresh_duration(self):
        self.turns_remaining = self.turns_total


class Blistering_Cold_Aura(Aura):

    ability_type = PetType.ELEMENTAL
    turns_total = 3


class Bleed(Aura):

    ability_type = PetType.BEAST
    accuracy = 1.0
