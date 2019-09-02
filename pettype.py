from enum import Enum


class PetType(Enum):
    HUMANOID = 1
    DRAGONKIN = 2
    FLYING = 3
    UNDEAD = 4
    CRITTER = 5
    MAGIC = 6
    ELEMENTAL = 7
    BEAST = 8
    AQUATIC = 9
    MECHANICAL = 10

    bonus_damage_against = {
        HUMANOID: DRAGONKIN,
        DRAGONKIN: MAGIC,
        FLYING: AQUATIC,
        UNDEAD: HUMANOID,
        CRITTER: UNDEAD,
        MAGIC: FLYING,
        ELEMENTAL: MECHANICAL,
        BEAST: CRITTER,
        AQUATIC: ELEMENTAL,
        MECHANICAL: BEAST,
    }

    weak_damage_against = {
        HUMANOID: BEAST,
        DRAGONKIN: UNDEAD,
        FLYING: DRAGONKIN,
        UNDEAD: AQUATIC,
        CRITTER: HUMANOID,
        MAGIC: MECHANICAL,
        ELEMENTAL: CRITTER,
        BEAST: FLYING,
        AQUATIC: MAGIC,
        MECHANICAL: ELEMENTAL,
    }
