from pet import *
from ability import *
import sys


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

    max_turns = 30

    # team_player = None
    # team_enemy = None

    def __init__(self):
        """ 
        Boneshard BB (chop, blistering cold, ice spike)
        Ikky P/S (Quills, Black Claw, Flock)
        Soul of the Forge H/P (Sulfuras Smash, Extra Plating, Reforge)
        
        Prototype Annoy-O-Tron H/H 4(Sonic Blast, Sonic Detonator, Annoying Shield)
        """

        # Pet(breed, quality, level, health_percentage)
        team_player = Player_Team(
            Boneshard("B/B", 1.3, 25),
            Ikky("P/S", 1.3, 25),
            Soul_of_the_Forge("H/P", 1.3, 25),
        )
        team_enemy = NPC_Team(Prototype_Annoy_O_Tron("B/B", 1.3, 25))

        self.simulate(team_player, team_enemy)

    def simulate(self, team_player, team_enemy):

        turn = 0

        """
        INT_MAX = sys.maxsize + 1

        INT_MIN = -sys.maxsize-1


        print(INT_MAX,INT_MIN)
        """

        while (
            team_player.is_team_dead() == False
            and team_enemy.is_team_dead() == False
            and turn < self.max_turns
        ):

            player_ability = team_player.select_ability()
            enemy_ability = team_enemy.select_ability()

            # Whoever has the higher speed goes first. If the speeds are matched,
            # then the npc goes first. A trainer switching a pet always goes first
            # if (
            #    player_attack_object["goes_first"] == True
            #    and enemy_attack_object["goes_first"] == True
            # ):
            #    # This case can be discounted since if the enemy has a "goes first"
            #    # ability, then they will go first, regardless if you do aswell
            #    pass
            if enemy_ability["goes_first"] == True or player_ability["standby"] == True:
                self.use_ability(
                    (team_enemy, enemy_ability), (team_player, player_ability)
                )
                self.use_ability(
                    (team_player, player_ability), (team_enemy, enemy_ability)
                )

            elif player_ability["goes_first"] == True:
                self.use_ability(
                    (team_player, player_ability), (team_enemy, enemy_ability)
                )
                self.use_ability(
                    (team_enemy, enemy_ability), (team_player, player_ability)
                )

            else:
                player_speed = team_player.get_speed()
                enemy_speed = team_enemy.get_speed()

                if enemy_speed >= player_speed:
                    self.use_ability(
                        (team_enemy, enemy_ability), (team_player, player_ability)
                    )
                    self.use_ability(
                        (team_player, player_ability), (team_enemy, enemy_ability)
                    )
                else:
                    self.use_ability(
                        (team_player, player_ability), (team_enemy, enemy_ability)
                    )
                    self.use_ability(
                        (team_enemy, enemy_ability), (team_player, player_ability)
                    )

            if turn == 1:
                print(player_ability["frontline_damage"]["normal"])

            turn += 1
        else:
            print("reached max turns")

    def use_ability(self, offensive_object, defensive_object):

        offensive_team, offensive_ability = offensive_object
        defensive_team, _ = defensive_object

        # No need to do anything on a pass
        if offensive_ability["standby"] == True:
            return

        if offensive_ability["frontline_damage"] == True:
            defensive_team.receive_attack(offensive_ability)

        if offensive_ability["backline_damage"] == True:
            pass
        if offensive_ability["enemy_pet_aura"] == True:
            pass
        if offensive_ability["enemy_team_aura"] == True:
            pass

        if offensive_ability["frontline_healing"] == True:
            pass
        if offensive_ability["backline_healing"] == True:
            pass
        if offensive_ability["friendly_pet_aura"] == True:
            pass
        if offensive_ability["friendly_team_aura"] == True:
            pass

        """
        return {
            "standby":False,
            "ability_type": self.get_ability_type(),
            "accuracy": self.get_accuracy(),
            "frontline_healing": self.calculate_frontline_healing(power),
            "backline_healing": self.calculate_backline_healing(power),
            "friendly_pet_aura": self.friendly_pet_aura(power),
            "friendly_team_aura": self.friendly_team_aura(power),
            "split_healing": self.get_split_healing(),
            "frontline_damage": self.calculate_frontline_damage(power),
            "backline_damage": self.calculate_backline_damage(power),
            "enemy_pet_aura": self.enemy_pet_aura(power),
            "enemy_team_aura": self.enemy_team_aura(power),
            "split_damage": self.get_split_damage(),
        }
        """

    def stage_zero(self):
        pass


class Battlefield:

    weather = None


class Team:
    """ A Pet team can range from 1 to 3 pets"""

    lineup = []
    active_pet = None

    def __init__(self, pet_one, pet_two=None, pet_three=None):

        if pet_two != None and pet_three != None:
            self.lineup = [pet_one, pet_two, pet_three]
        elif pet_two != None:
            self.lineup = [pet_one, pet_two]
        elif pet_three != None:
            self.lineup = [pet_one, pet_three]
        else:
            self.lineup = [pet_one]

        self.activate_pet(0)

    def select_ability(self):
        # This will probably need some other function parameters like the turn,
        # the weather, ect.
        pass

    def receive_attack(self):
        pass

    def is_team_dead(self):
        all_dead = True

        for pet in self.lineup:
            if pet.is_alive() == True:
                all_dead = False
                break

        return all_dead

    def activate_pet(self, lineup_position):
        self.active_pet = self.lineup[lineup_position]
        self.active_pet.set_played()

    def get_speed(self):
        return self.active_pet.get_speed()

    def standby(self):
        return {"standby": True, "goes_first": False}


class Player_Team(Team):
    def select_ability(self):
        """ The action priority list should be loaded in and interpreted here 
        ability(Blistering Cold:786) [ round>3 ]
        standby [ round~1,2,6 ]
        ability(Chop:943) [ round>4 ]
        ability(Ice Spike:625)
        change(#2)
        ability(Black Claw:919) [ !enemy.aura(Black Claw:918).exists ]
        ability(Flock:581)
        """
        return self.active_pet.use_ability("#1")


class NPC_Team(Team):
    def select_ability(self):
        return self.standby()


"""
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
"""

game = Simulator()
