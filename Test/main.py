from classes.game import Person, bcolors
from classes.magic import Spell
from classes.inventory import Item

print("\n")
print("\n")


# Black Magic
fire = Spell("Fire", 10, 100, "black")
thunder = Spell("Thunder", 10, 100, "black")
blizzard = Spell("Blizzard", 10, 100, "black")
meteor = Spell("Meteor", 20, 200, "black")
quake = Spell("Quake", 14, 140, "black")

# White Magic
cure = Spell("Cure", 12, 120, "white")
kura = Spell("Kura", 18, 200, "white")

player_spells = [fire, thunder, blizzard, meteor, quake, cure, kura]

# Item Creation
potion = Item("Potion", "potion", "Heals 50 HP", 50)
hipotion = Item("Potion", "potion", "Heals 100 HP", 100)
superpotion = Item("Potion", "potion", "Heals 500 HP", 300)
elixir = Item("Elixir", "elixir", "Fully restores HP/MP of one party member", 9999)
hielixir = Item("MegaElixir", "elixir", "Fully restores HP/MP of party", 9999)
grenade = Item("Grenade", "attack", "Deals 500 Damage", 500)

player_items = [{"item": potion, "quantity": 5},
                {"item": elixir, "quantity": 2},
                {"item": grenade, "quantity": 1}]

# Instantiation of People
player1 = Person("Tim ", 460, 65, 60, 34, player_spells, player_items)
player2 = Person("Tom ", 460, 65, 60, 34, player_spells, player_items)
player3 = Person("John", 460, 65, 60, 34, player_spells, player_items)
enemy = Person("Enemy", 2200, 65, 45, 25, [], [])

players = [player1, player2, player3]
running = True

print(bcolors.FAIL + bcolors.BOLD + "An Enemy Attacks!" + bcolors.ENDC)

while running:
    print("================")
    print("\n")

    for player in players:
        player.get_stats()
        print()



    for player in players:


        player.choose_action()
        choice = input("Choose Action: ")
        index = int(choice) - 1

        if index == 0:
            dmg = player.generate_dmg()
            enemy.take_damage(dmg)
            print("You attacked for", dmg, "damage points")
            # print ("Enemy HP is reduced to", enemy.get_hp())
        elif index == 1:
            player.choose_magic()
            magic_choice = int(input("Choose magic:")) - 1

            if magic_choice == -1:
                # print("Invalid Entry")
                continue

            spell = player.magic[magic_choice]
            magic_dmg = spell.generate_dmg()

            current_mp = player.get_mp()

            if spell.cost > current_mp:
                print(bcolors.FAIL, "Not enough MP", bcolors.ENDC)
                continue

            if spell.type == "white":
                player.heal(magic_dmg)
                print(bcolors.OKBLUE, spell.name, "heals for", str(magic_dmg), "HP.", bcolors.ENDC)
            elif spell.type == "black":
                enemy.take_damage(magic_dmg)
                print(bcolors.OKBLUE, spell.name, "deals", str(magic_dmg), "points of damage", bcolors.ENDC)

            player.reduce_mp(spell.cost)

        elif index == 2:
            player.choose_items()
            item_choice = int(input("Choose item:")) - 1

            if item_choice == -1:
                # print("Invalid Entry")
                continue

            item = player.items[item_choice]["item"]

            if player.items[item_choice]["quantity"] == 0:
                print(bcolors.FAIL, "None left..", bcolors.ENDC)
                continue

            player.items[item_choice]["quantity"] -= 1

            if item.type == "potion":
                player.heal(item.prop)
                print(bcolors.OKBLUE, item.name, "heals for", str(item.prop), "HP.", bcolors.ENDC)
            elif item.type == "elixir":
                player.hp = player.maxHp
                player.mp = player.maxMp
                print(bcolors.OKBLUE, item.name, "Fully Restored HP & MP", bcolors.ENDC)
            elif item.type == "attack":
                enemy.take_damage(item.prop)
                print(bcolors.OKBLUE, item.name, "deals", str(item.prop), "points of damage", bcolors.ENDC)




        enemy_choice = 1

        enemy_dmg = enemy.generate_dmg()
        player.take_damage(enemy_dmg)
        print("Enemy attacked for", enemy_dmg, "damage points")
        # print("Your HP is reduced to", player.get_hp())

        print("----------------------")
        print("Enemy HP:", bcolors.FAIL, str(enemy.get_hp()), "/", str(enemy.get_max_hp()), bcolors.ENDC)

        if enemy.get_hp() == 0:
            print(bcolors.OKGREEN + "You win!" + bcolors.ENDC)
            running = False
        elif player.get_hp() == 0:
            print(bcolors.FAIL + "You have been defeated!" + bcolors.ENDC)
            running = False
