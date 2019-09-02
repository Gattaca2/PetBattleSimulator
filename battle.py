from pet import *
from ability import *


class Simulator:
    """
    stages of a turn:
    select attack to use
    0. check if all pets on a team are dead
    1. pre turn buffs (here is where you would apply a move that always goes first)
    2. faster pet attacks
    3. if pet dies, it ressurects here
    4. damages back of team (pet 2 and 3 for a multi pet attack)
    5. dots on the faster pet apply
    6. slower pet attacks
    7. if pet dies, it ressurects here
    8. damages back of team (pet 2 and 3 for a multi pet attack)
    9. dots on the faster pet apply
    """

    turn = None

    team_player = None
    team_enemy = None

    def __init__(self):
        """ 
        Boneshard BB (chop, blistering cold, ice spike)
        Ikky P/S (Quills, Black Claw, Flock)
        Soul of the Forge H/P (Sulfuras Smash, Extra Plating, Reforge)
        
        Prototype Annoy-O-Tron H/H 4(Sonic Blast, Sonic Detonator, Annoying Shield)
        """
        team_player = Team()
        team_enemy = Team()
        pass

    def select_attack():
        pass

    def stage_zero():
        pass


class Battlefield:

    weather = None


class Team:
    """ A Pet team can range from 1 to 3 pets"""

    lineup = []

    def __init__(self):
        pass


class Buff:
    def __init__(self):
        pass


class Debuff:
    def __init__(self):
        pass


class Hot:
    def __init__(self):
        pass


class Dot:
    def __init__(self):
        pass


pet = Boneshard()
