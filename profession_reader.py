import json
import re

file_path = 'generators/tables/professions_text.txt'

with open(file_path, 'r', encoding='utf-8') as file:
    tekst = file.read()


def parsing(_section):
    _header = _section.split('\n')[0]
    profession_name, status = _header.split(' - ')
    skills = re.search(r'Umiejętności: (.+)', _section).group(1).split(', ')
    talents = re.search(r'Talenty: (.+)', _section).group(1).split(', ')
    inventory = re.search(r'Wyposażenie: (.+)', _section).group(1).split(', ')

    return {
        "status": status.strip(),
        "umiejętności": [u.strip() for u in skills],
        "talenty": [t.strip() for t in talents],
        "wyposażenie": [w.strip() for w in inventory]
    }


sections = tekst.strip().split('\n\n')
professions = {}
for section in sections:
    profession_data = parsing(section)
    header = section.split('\n')[0]
    profession = header.split(' - ')[0]
    professions[profession] = profession_data

with open('generators/tables/professions_details.json', 'w', encoding="utf-8") as file:
    file.truncate(0)
    json.dump(professions, file, ensure_ascii=False)
