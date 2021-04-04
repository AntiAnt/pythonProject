import random


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    #TODO find more colors


class HeroToken:
    def __init__(self, char, color_code, description):
        self.attack_mod = 2
        self.damage_mod = 1
        self.damage_max = 8
        self.char = char
        self.color_code = color_code
        self.description = description
        self.max_health = 20
        self.health = 20
        self.ac = 15
        self.inventory = {}

    def get_char(self):
        return self.char

    def get_color_code(self):
        return self.color_code

    def damaged(self, num_damage_taken):
        self.health -= num_damage_taken

    def healed(self, num_damage_healed):
        if self.health + num_damage_healed <= self.max_health:
            self.health += num_damage_healed
        else:
            self.health = self.max_health

    def get_weapon_damage(self):
        return random.randint(1, self.damage_max) + self.damage_mod

    def takes_hit(self, attack):
        return attack >= self.ac

    def attack(self):
        return random.randint(1, 20) + self.attack_mod

    def add_to_inventory(self, item):
        self.inventory[item.name] = item


class TileToken:
    def __init__(self, char, color_code, description):
        self.char = char
        self.color_code = color_code
        self.description = description

    def get_char(self):
        return self.char

    def get_color_code(self):
        return self.color_code


class Item:

    def __init__(self, name, description, weapon):
        self.name = name
        self.description = description
        self.weapon = weapon
