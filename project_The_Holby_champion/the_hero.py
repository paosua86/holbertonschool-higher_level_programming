#!/usr/bin/python3

FIGHTER = {"Health": 5, "attack": 8, "defense": 3,"magic": 2, "speed": 7,"weapon": sword,"defense_equip": shield, "armor": chest_armor}
CLERIC = {"Health": 5, "attack": 5, "defense": 5,"magic": 5, "speed": 2,"weapon": staff,"defense_equip": shield, "armor": chest_armor}
MAGE = {"Health": 5, "attack": 4, "defense": 6,"magic": 8, "speed": 2,"weapon": staff,"defense_equip": no_shield, "armor": gauntlets}
PALADIN = {"Health": 5, "attack": 9, "defense": 8,"magic": 2, "speed": 8,"weapon": hammer,"defense_equip": no_shield, "armor": chest_armor}
RANGER = {"Health": 5, "attack": 8, "defense": 9,"magic": 6, "speed": 9,"weapon": bow_and_arrow,"defense_equip": no_shield, "armor": chest_armor}
ROGUE = {"Health": 5, "attack": 6, "defense": 2,"magic": 3, "speed": 6,"weapon": blades ,"defense_equip": shield, "armor": chest_armor}

TYPES = {"fighter": FIGHTER, "cleric": CLERIC, "mage": MAGE, "paladin": PALADIN, "ranger": RANGER, "rogue": ROGUE}

class BaseChampion:
    __health = 0
    __attack = 0

    def __init__(self, name, race, level, gender, stats, stats_points):
        self.name = name
        self.race = race
        self.level = level
        self.gender = gender
        self.stats = stats
        self.stats_points = stats_points
        self._assing_atributes = stats

    def _assing_atributes(self):
        type_dict = TYPES[self._char_type]
        self.__health = type_dict["health"]
        self.__attack = type_dict["attack"]

    def attack(self):
        return self.__attack

    def level_up(self):
        pass

    def gain_exp(self, level):
        pass

    def death(self, exp):
        if self.__health <= 0:
            exp =




class Cleric(BaseChampion):
    pass

class experience():
    __level
    __current_level
    __total

