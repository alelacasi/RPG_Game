import random


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    ENDC = '\033[0m'


class Person:
    def __init__(self, name, hp, mp, atk, df, magic, items):
        self.maxHp = hp
        self.name = name
        self.hp = hp
        self.maxMp = mp
        self.mp = mp
        self.atkl = atk - 10
        self.atkh = atk + 10
        self.df = df
        self.magic = magic
        self.actions = ["Attack", "Magic", "Item"]
        self.items = items

    def generate_dmg(self):
        return random.randrange(self.atkl, self.atkh)

    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.maxHp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.maxMp

    def reduce_mp(self, cost):
        self.mp -= cost

    def heal(self, dmg):
        self.hp += dmg
        if self.hp > self.maxHp:
            self.hp = self.maxHp

    def choose_action(self):
        i = 1
        print("\n" + bcolors.BOLD + self.name + bcolors.ENDC)
        print(bcolors.OKGREEN, bcolors.BOLD, "Action:", bcolors.ENDC)
        for item in self.actions:
            print("\t" + str(i) + ":", item)
            i += 1

    def choose_magic(self):
        i = 1
        print(bcolors.OKGREEN, bcolors.BOLD, "Magic:", bcolors.ENDC)
        for spell in self.magic:
            print("\t" + str(i) + ":", spell.name, "cost:", spell.cost)
            i += 1

    def choose_items(self):
        i = 1
        print(bcolors.OKGREEN, bcolors.BOLD, "Items:", bcolors.ENDC)
        for item in self.items:
            print("\t" + str(i) + ":", item["item"].name, "cost:", item["item"].description,
                  "(x" + str(item["quantity"]) + ")")
            i += 1

    def get_stats(self):

        hp_bar = ""
        hp_ticks = (self.hp/self.maxHp) * 25

        mp_bar = ""
        mp_ticks = (self.mp/self.maxMp) * 10

        while hp_ticks > 0:
            hp_bar += "█"
            hp_ticks -= 1

        while len(hp_bar) < 25:
            hp_bar += " "

        while mp_ticks > 0:
            mp_bar += "█"
            mp_ticks -= 1

        while len(mp_bar) < 10:
            mp_bar += " "


        print("NAME              HP                                   MP ")
        print("                    _________________________           __________")
        print(str(self.name) + ":      " +
              str(self.hp) + "/" + str(self.maxHp) + " |" + bcolors.OKGREEN + hp_bar
              + bcolors.ENDC + "|   " + str(self.mp) + "/" + str(self.maxMp) + " |" +
              bcolors.OKBLUE + mp_bar + bcolors.ENDC + "|")
