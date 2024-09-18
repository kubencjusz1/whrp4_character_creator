import json
from generators.roller import *
from generators.tables.race_attributes import *
from generators.tables.class_professions import *
from generators.tables.equpment import *
from generators.tables.looks import *
from generators.tables.names import *
from generators.tables.skills import race_skills_table
from generators.tables.talents import talent_table

with open('generators/tables/professions_details.json', 'r', encoding="utf-8") as file:
    all_professions_details = json.load(file)


class Character:

    def __init__(self):
        self.race = ""
        self.profession = ""
        self.true_profession = ""
        self.status = ""
        self.character_class = ""
        self.attributes = {WW: 0, US: 0, S: 0, WT: 0, I: 0, ZW: 0, ZR: 0, INT: 0, SW: 0, OGD: 0}
        self.hp = 0
        self.destiny_points = 0
        self.hero_points = 0
        self.points_to_choose = 0
        self.speed = 0
        self.skills = {RACE_SKILLS: {}, PROFESSION_SKILLS: {}}
        self.talents = {RACE_TALENTS: [], PROFESSION_TALENTS: []}
        self.equipment = []
        self.money = {"Z": 0, "S": 0, "B": 0}
        self.name = ""
        self.age = ""
        self.eye_color = ""
        self.hair_color = ""
        self.height = ""

    def print_info(self):
        for attribute, value in vars(self).items():
            print(f"{attribute}: {value}")

    def get_race(self):
        roll = roll_d100()
        if 1 <= roll <= 90:
            self.race = HUMAN
        if 91 <= roll <= 94:
            self.race = HALFLING
        if 95 <= roll <= 98:
            self.race = DWARF
        if roll == 99:
            self.race = WOOD_ELF
        if roll == 100:
            self.race = HIGH_ELF

    def get_profession_and_class(self):
        roll = roll_d100()

        professions = professions_table.get(self.race)
        self.profession = roll_on_table(roll, professions)[2]

        for conversion in professions_name_converter_table:
            if self.profession in conversion:
                self.true_profession = conversion[0]
                break

        self.status = all_professions_details.get(self.true_profession).get("status")

        classes = classes_table.get(self.race)
        self.character_class = roll_on_table(roll, classes)[2]

    def get_attributes(self):
        attributes = attributes_table.get(self.race)
        for attribute in self.attributes:
            self.attributes[attribute] = attributes[attribute] + roll_d10(2)

        table = points_speed_table.get(self.race)
        self.destiny_points = table.get(DESTINY_POINTS)
        self.hero_points = table.get(HERO_POINTS)
        self.points_to_choose = table.get(POINTS_TO_CHOOSE)
        self.speed = table.get(SPEED)

    def get_hp(self):
        self.hp = count_bonus(self, S) + count_bonus(self, WT) + count_bonus(self, SW)

    def get_talents(self):
        self.talents[RACE_TALENTS] = talent_table.get(self.race)
        for i, t in enumerate(self.talents[RACE_TALENTS]):
            if t == ["Losowy talent"]:
                self.talents[RACE_TALENTS][i] = roll_talent(self.talents[RACE_TALENTS])
        self.talents[PROFESSION_TALENTS] = [all_professions_details.get(self.true_profession).get("talenty")]

    def get_skills(self):
        self.skills[RACE_SKILLS] = race_skills_table.get(self.race)
        self.skills[PROFESSION_SKILLS] = [all_professions_details.get(self.true_profession).get("umiejętności")]

    def get_equipemnt(self):
        self.equipment.append(equipment_table.get(self.character_class))
        coin, number = self.status.split()
        if coin == "Brąz":
            for n in range(int(number)):
                self.money["B"] += roll_d10(2)
        elif coin == "Srebro":
            for n in range(int(number)):
                self.money["S"] += roll_d10()
        elif coin == "Złoto":
            self.money["Z"] += int(number)

    def get_name_and_look(self):
        self.eye_color = roll_on_table(roll_d10(2), eye_colors.get(self.race))[2]
        self.hair_color = roll_on_table(roll_d10(2), hair_colors.get(self.race))[2]
        self.age = height_age_table.get(self.race).get("age")[0] + roll_d10(height_age_table.get(self.race).get("age")[1])
        self.height = height_age_table.get(self.race).get("height")[0] + roll_d10(
            height_age_table.get(self.race).get("height")[1])

        if self.race == HUMAN:
            self.name = f"{random.choice(human_names_table)} {random.choice(human_second_names_table)} von {random.choice(imperium_cities_table)}"

        elif self.race == DWARF:
            self.name = f"{random.choice(dwarves_names_table)} '{random.choice(dwarves_nicknames_table)}' {random.choice(dwarves_second_names_table)} klanu {random.choice(dwarves_clans_table)}"

        elif self.race == HALFLING:
            self.name = f"{random.choice(halfling_names_with_nicknames_table)} z klanu {random.choice(halfling_clans_table)}"

        elif self.race == HIGH_ELF:
            self.name = f"{random.choice(elves_name_table)[0]}{random.choice(elves_name_table)[1]}{random.choice(elves_name_table)[2]} zwany {random.choice(high_elf_nicknames_table)}"

        elif self.race == WOOD_ELF:
            self.name = f"{random.choice(elves_name_table)[0]}{random.choice(elves_name_table)[1]}{random.choice(elves_name_table)[3]} zwany {random.choice(wood_elf_nicknames_table)}"
