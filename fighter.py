# Create a function that returns the name of the winner in a fight between two fighters.

# Each fighter takes turns attacking the other and whoever kills the other first is victorious. Death is defined as having health <= 0.

# Each fighter will be a Fighter object/instance. See the Fighter class below in your chosen language.

# Both health and damagePerAttack (damage_per_attack for python) will be integers larger than 0. You can mutate the Fighter objects.

# Example:


class Fighter(object):
    def __init__(self, name, health, damage_per_attack):
        self.name = name
        self.health = health
        self.damage_per_attack = damage_per_attack

    def __str__(self): return "Fighter({}, {}, {})".format(
        self.name, self.health, self.damage_per_attack)
    __repr__ = __str__


def declare_winner(fighter1, fighter2, first_attacker):
    if fighter1.name == first_attacker:
        first = fighter1
        second = fighter2
    else:
        first = fighter2
        second = fighter1

    while not is_dead(fighter1) or not is_dead(fighter2):
        second.health = second.health - first.damage_per_attack
        first.health = first.health - second.damage_per_attack

    if is_dead(fighter1):
        return fighter2.name
    else:
        return fighter1.name


def is_dead(fighter):
    if fighter.health >= 0:
        return True
    else:
        return False

# tests


print(declare_winner(Fighter("Lew", 10, 2),
                     Fighter("Harry", 5, 4), "Lew") == "Lew")

print(declare_winner(Fighter("Lew", 10, 2),
                     Fighter("Harry", 5, 4), "Harry") == "Harry")

print(declare_winner(Fighter("Harold", 20, 5),
                     Fighter("Harry", 5, 4), "Harry") == "Harold")

print(declare_winner(Fighter("Harold", 20, 5),
                     Fighter("Harry", 5, 4), "Harold") == "Harold")

print(declare_winner(Fighter("Jerry", 30, 3),
                     Fighter("Harold", 20, 5), "Jerry") == "Harold")

print(declare_winner(Fighter("Jerry", 30, 3),
                     Fighter("Harold", 20, 5), "Harold") == "Harold")
