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
        self.team_player = Boneshard()
        self.team_enemy = Prototype_Annoy_O_Tron()
        self.select_attack()

    def select_attack(self):
        """ The action priority list should be loaded in and interpreted here 
        ability(Blistering Cold:786) [ round>3 ]
        standby [ round~1,2,6 ]
        ability(Chop:943) [ round>4 ]
        ability(Ice Spike:625)
        change(#2)
        ability(Black Claw:919) [ !enemy.aura(Black Claw:918).exists ]
        ability(Flock:581)
        """
        
        player_attack_object = self.team_player.use_ability("#1")
        enemy_attack_object = self.team_enemy.use_ability("#1")
        print(attack_object["frontline_damage"]["normal"])

    def stage_zero(self):
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

game = Simulator()
#pet = Boneshard()
