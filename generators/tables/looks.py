from generators.globals import *

eye_colors = {HUMAN: [[2, 2, 'Dowolny wybór'], [3, 3, 'Zielony'], [4, 4, 'Błękitny'], [5, 7, 'Niebieski'],
                           [8, 11, 'Blady szary'], [12, 14, 'Szary'], [15, 17, 'Brązowy'], [18, 18, 'Orzechowy'],
                           [19, 19, 'Ciemnobrązowy'], [20, 20, 'Czarny']],
              DWARF: [[2, 2, 'Czarny jak węgiel'], [3, 3, 'Szary jak ołów'], [4, 4, 'Stalowoszary'],
                            [5, 7, 'Niebieski'], [8, 11, 'Brązowy jak ziemia'], [12, 14, 'Ciemnobrązowy'],
                            [15, 17, 'Orzechowy'], [18, 18, 'Zielony'], [19, 19, 'Ciemny miedziany'],
                            [20, 20, 'Złoty']],
              HALFLING: [[2, 2, 'Jasnoszary'], [3, 3, 'Szary'], [4, 4, 'Błękitny'], [5, 7, 'Niebieski'],
                           [8, 11, 'Zielony'], [12, 14, 'Orzechowy'], [15, 17, 'Brązowy'], [18, 18, 'Miedziany'],
                           [19, 19, 'Ciemnobrązowy'], [20, 20, 'Ciemnobrązowy']],
              HIGH_ELF: [[2, 2, 'Czarny jak smoła'], [3, 3, 'Ametystowy'], [4, 4, 'Akwamaryna'],
                             [5, 7, 'Szafirowy'], [8, 11, 'Turkusowy'], [12, 14, 'Szmaragdowy'],
                             [15, 17, 'Bursztynowy'], [18, 18, 'Miedziany'], [19, 19, 'Cytrynowożółty'],
                             [20, 20, 'Złoty']],
              WOOD_ELF: [[2, 2, 'Kolor kości słoniowej'], [3, 3, 'Antracyt'], [4, 4, 'Zielony jak bluszcz'],
                            [5, 7, 'Zielony jak mech'], [8, 11, 'Kasztanowy'], [12, 14, 'Kasztanowy'],
                            [15, 17, 'Ciemnobrązowy'], [18, 18, 'Jasnobrązowy'], [19, 19, 'Złotobrązowy'],
                            [20, 20, 'Fiołkowy']]}
hair_colors = {
    HUMAN: [[2, 2, 'Biały'], [3, 3, 'Złoty blond'], [4, 4, 'Rudoblond'], [5, 7, 'Złoty'], [8, 11, 'Jasny brąz'],
                 [12, 14, 'Ciemny brąz'], [15, 17, 'Czarny'], [18, 18, 'Kasztanowy'], [19, 19, 'Rudy'],
                 [20, 20, 'Siwy']],
    DWARF: [[2, 2, 'Blond'], [3, 3, 'Siwy'], [4, 4, 'Jasny blond'], [5, 7, 'Brązowy'], [8, 11, 'Miedziany'],
                  [12, 14, 'Brąz'], [15, 17, 'Brąz'], [18, 18, 'Ciemny brąz'], [19, 19, 'Rudy brąz'],
                  [20, 20, 'Czarny']],
    HALFLING: [[2, 2, 'Biały'], [3, 3, 'Lniany'], [4, 4, 'Rudawy'], [5, 7, 'Złoty'], [8, 11, 'Kasztanowy'],
                 [12, 14, 'Rudy'], [15, 17, 'Musztardowy'], [18, 18, 'Migdałowy'], [19, 19, 'Czekoladowy'],
                 [20, 20, 'Lukrecjowy']],
    HIGH_ELF: [[2, 2, 'Srebrnosiwy'], [3, 3, 'Popielaty'], [4, 4, 'Jasny blond'], [5, 7, 'Miodowoblond'],
                   [8, 11, 'Żółty'], [12, 14, 'Miedziany blond'], [15, 17, 'Blond'], [18, 18, 'Migdałowy'],
                   [19, 19, 'Czerwony'], [20, 20, 'Czarny']],
    WOOD_ELF: [[2, 2, 'Brzozowobiały'], [3, 3, 'Blond'], [4, 4, 'Różowe złoto'], [5, 7, 'Miodowoblond'],
                  [8, 11, 'Brązowy'], [12, 14, 'Mahoniowy'], [15, 17, 'Ciemny brąz'], [18, 18, 'Sjena'],
                  [19, 19, 'Hebanowy'], [20, 20, 'Niebiesko-czarny']]}

hight_age_table = {
    HUMAN: {"age": [15, 1], "height": [150, 4]},
    DWARF: {"age": [15, 10], "height": [130, 2]},
    HALFLING: {"age": [15, 5], "height": [95, 2]},
    HIGH_ELF: {"age": [30, 10], "height": [180, 3]},
    WOOD_ELF: {"age": [30, 10], "height": [180, 3]},
}
