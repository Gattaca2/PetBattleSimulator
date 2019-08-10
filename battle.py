"""
stages of a turn:
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

class Simulator:

    turn = None

    def __init__(self):
        pass
        
        
class Pet:

    breed = None

    base_health = None
    base_attack = None
    base_speed = None
    
    current_health = None
    current_attack = None
    current_speed = None    
    
    def __init__(self):
        pass
        
        
class Team:

    def __init__(self):
        pass
        
        
class Ability:

    def __init__(self):
        pass
        
        
class Buff:

    def __init__(self):
        pass
        
        
class Debuff:

    def __init__(self):
        pass
        
        
        