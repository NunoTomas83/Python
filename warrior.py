""" Script to simulate a fight between warriors """


import random
import math


class Warrior:
    def __init__(self, name="warrior", health=0, attk_max=0, block_max=0):
        self.name = name
        self.health = health
        self.attk_max = attk_max
        self.block_max = block_max

    def attack(self):
        attk_amt = self.attk_max * (random.random() + 0.5)
        return attk_amt

    def block(self):
        block_amt = self.block_max * (random.random() + 0.5)
        return block_amt


class Battle:
    def start_fight(self, warrior1, warrior2):
        # Continue looping until a Warrior dies switching back and
        # forth as the Warriors attack each other
        while True:
            if self.get_attack_result(warrior1, warrior2) == "Game Over":
                print("Game Over")
                break

            if self.get_attack_result(warrior2, warrior1) == "Game Over":
                print("Game Over")
                break

    # Make this method static because we don't need to use self
    @staticmethod
    def get_attack_result(warriorA, warriorB):
        warrior_a_attk_amt = warriorA.attack()
        warrior_b_block_amt = warriorB.block()
        damage_2_warrior_b = math.ceil(warrior_a_attk_amt - warrior_b_block_amt)
        warriorB.health = warriorB.health - damage_2_warrior_b

        print("{} attacks {} and deals {} damage".format(warriorA.name, warriorB.name, damage_2_warrior_b))
        print("{} is down to {} health".format(warriorB.name, warriorB.health))

        if warriorB.health <= 0:
            print("{} has Died and {} is Victorious".format(warriorB.name, warriorA.name))
            return "Game Over"
        else:
            return "Fight Again"


def main():
    # Create 2 Warriors
    thor = Warrior("Thor", 50, 20, 10)
    loki = Warrior("Loki", 50, 20, 10)
    # Create Battle object
    battle = Battle()
    # Initiate Battle
    battle.start_fight(thor, loki)


main()
