import random

from generators.tables.talents import random_talent


def roll_d100(n=1):
    res = 0
    for _ in range(n):
        res += random.randint(1, 100)
    return res


def roll_d10(n=1):
    res = 0
    for _ in range(n):
        res += random.randint(1, 10)
    return res


def count_bonus(character, stat):
    return int(character.attributes.get(stat) / 10)


def roll_talent(talents):
    roll = roll_d100()
    talent = [roll_on_table(roll, random_talent)[2]]

    flattened_talents = [t for sublist in talents for t in (sublist if isinstance(sublist, list) else [sublist])]

    if talent[0] in flattened_talents:
        return roll_talent(talents)
    else:
        return talent


def roll_on_table(roll, table):
    for rolled_raw in table:
        if rolled_raw[0] <= roll <= rolled_raw[1]:
            return rolled_raw
    print(roll, table)
    return ""