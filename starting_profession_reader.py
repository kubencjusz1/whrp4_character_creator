import json

with open('generators/tables/professions_details.json', 'r', encoding="utf-8") as file:
    all_professions = json.load(file)
professions_name_converter = []
for i, key in enumerate(all_professions):
    if i % 4 == 0:
        tmp1 = key
    elif i % 4 == 1:
        tmp2 = key
        professions_name_converter.append([tmp1, tmp2])
print(professions_name_converter)
