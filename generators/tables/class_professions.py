from generators.globals import *

classes_table = {
    HUMAN: [
        (1, 8, "Uczony"),
        (9, 27, "Mieszczanin"),
        (28, 37, "Dworzaniec"),
        (38, 49, "Pospólstwo"),
        (50, 60, "Wędrowiec"),
        (61, 74, "Wodniak"),
        (75, 88, "Łotr"),
        (89, 100, "Wojownik")
    ],
    DWARF: [
        (1, 9, "Uczony"),
        (10, 34, "Mieszczanin"),
        (35, 45, "Dworzaniec"),
        (46, 55, "Pospólstwo"),
        (56, 67, "Wędrowiec"),
        (68, 78, "Wodniak"),
        (79, 84, "Łotr"),
        (85, 100, "Wojownik")
    ],
    HALFLING: [
        (1, 8, "Uczony"),
        (9, 27, "Mieszczanin"),
        (28, 46, "Dworzaniec"),
        (47, 56, "Pospólstwo"),
        (57, 68, "Wędrowiec"),
        (69, 74, "Wodniak"),
        (75, 94, "Łotr"),
        (95, 100, "Wojownik")
    ],
    HIGH_ELF: [
        (1, 16, "Uczony"),
        (17, 29, "Mieszczanin"),
        (30, 45, "Dworzaniec"),
        (46, 56, "Pospólstwo"),
        (57, 63, "Wędrowiec"),
        (64, 66, "Wodniak"),
        (67, 88, "Łotr"),
        (89, 100, "Wojownik")
    ],
    WOOD_ELF: [
        (1, 5, "Uczony"),
        (6, 10, "Mieszczanin"),
        (11, 35, "Dworzaniec"),
        (36, 57, "Pospólstwo"),
        (58, 73, "Wędrowiec"),
        (74, 79, "Wodniak"),
        (80, 96, "Łotr"),
        (97, 100, "Wojownik")
    ]
}
professions_table = {
    HUMAN: [
        (1, 1, "Aptekarka"),
        (2, 2, "Czarodziej"),
        (3, 3, "Inżynier"),
        (4, 8, "Kapłan"),
        (9, 9, "Medyczka"),
        (10, 11, "Mniszka"),
        (12, 12, "Prawniczka"),
        (13, 14, "Uczony"),
        (15, 15, "Agitator"),
        (16, 16, "Kupiec"),
        (17, 19, "Mieszczka"),
        (20, 21, "Rzemieślniczka"),
        (22, 22, "Strażnik"),
        (23, 24, "Szczurołap"),
        (25, 25, "Śledczy"),
        (26, 27, "Żebrak"),
        (28, 28, "Artystka"),
        (29, 29, "Doradca"),
        (30, 30, "Namiestnik"),
        (31, 31, "Poseł"),
        (32, 34, "Służąca"),
        (35, 35, "Szlachcic"),
        (36, 36, "Szpieg"),
        (37, 37, "Zwadźca"),
        (38, 42, "Chłopka"),
        (43, 43, "Górnik"),
        (44, 44, "Guślarz"),
        (45, 46, "Łowczyni"),
        (47, 47, "Mistyczka"),
        (48, 48, "Zarządca"),
        (49, 49, "Zielarka"),
        (50, 50, "Zwiadowca"),
        (51, 52, "Biczownik"),
        (53, 53, "Domokrążca"),
        (54, 55, "Kuglarka"),
        (56, 56, "Łowca Czarownic"),
        (57, 57, "Łowczyni Nagród"),
        (58, 58, "Posłaniec"),
        (59, 59, "Strażniczka Dróg"),
        (60, 60, "Woźnica"),
        (61, 62, "Doker"),
        (63, 65, "Flisak"),
        (66, 66, "Pilotka Rzeczna"),
        (67, 67, "Pirat Rzeczny"),
        (68, 68, "Przemytniczka"),
        (69, 70, "Przewoźnik"),
        (71, 72, "Strażnik Rzeczny"),
        (73, 74, "Żeglarz"),
        (75, 78, "Banita"),
        (79, 79, "Czarownica"),
        (80, 80, "Paser"),
        (81, 81, "Hiena Cmentarna"),
        (82, 83, "Rajfur"),
        (84, 84, "Rekietierka"),
        (85, 85, "Szarlatan"),
        (86, 88, "Złodziej"),
        (89, 89, "Gladiator"),
        (90, 90, "Kapłan Bitewny"),
        (91, 92, "Kawalerzysta"),
        (93, 94, "Ochroniarz"),
        (95, 95, "Oprych"),
        (96, 96, "Rycerz"),
        (97, 100, "Żołnierz")
    ],
    DWARF: [
        (1, 1, "Aptekarka"),
        (2, 4, "Inżynier"),
        (5, 5, "Medyczka"),
        (6, 7, "Prawniczka"),
        (8, 9, "Uczony"),
        (10, 11, "Agitator"),
        (12, 15, "Kupiec"),
        (16, 21, "Mieszczka"),
        (22, 27, "Rzemieślniczka"),
        (28, 30, "Strażnik"),
        (31, 31, "Szczurołap"),
        (32, 33, "Śledczy"),
        (34, 34, "Żebrak"),
        (35, 35, "Artystka"),
        (36, 37, "Doradca"),
        (38, 39, "Namiestnik"),
        (40, 41, "Poseł"),
        (42, 42, "Służąca"),
        (43, 43, "Szlachcic"),
        (44, 44, "Szpieg"),
        (45, 45, "Zwadźca"),
        (46, 46, "Chłopka"),
        (47, 51, "Górnik"),
        (52, 53, "Łowczyni"),
        (54, 55, "Zarządca"),
        (56, 56, "Zwiadowca"),
        (57, 58, "Domokrążca"),
        (59, 60, "Kuglarka"),
        (61, 64, "Łowczyni Nagród"),
        (65, 66, "Posłaniec"),
        (67, 67, "Woźnica"),
        (68, 69, "Doker"),
        (70, 71, "Flisak"),
        (72, 72, "Pilotka Rzeczna"),
        (73, 73, "Pirat Rzeczny"),
        (74, 75, "Przemytniczka"),
        (76, 77, "Przewoźnik"),
        (78, 78, "Żeglarz"),
        (79, 81, "Banita"),
        (82, 82, "Hiena Cmentarna"),
        (83, 83, "Rekietierka"),
        (84, 84, "Złodziej"),
        (85, 87, "Gladiator"),
        (88, 90, "Ochroniarz"),
        (91, 93, "Oprych"),
        (94, 97, "Zabójca"),
        (98, 100, "Żołnierz")
    ],
    HALFLING: [
        (1, 1, "Aptekarka"),
        (2, 2, "Inżynier"),
        (3, 4, "Medyczka"),
        (5, 6, "Prawniczka"),
        (7, 8, "Uczony"),
        (9, 10, "Agitator"),
        (11, 14, "Kupiec"),
        (15, 17, "Mieszczka"),
        (18, 22, "Rzemieślniczka"),
        (23, 24, "Strażnik"),
        (25, 27, "Szczurołap"),
        (28, 29, "Śledczy"),
        (30, 33, "Żebrak"),
        (34, 35, "Artystka"),
        (36, 36, "Doradca"),
        (37, 38, "Namiestnik"),
        (39, 39, "Poseł"),
        (40, 45, "Służąca"),
        (46, 46, "Szpieg"),
        (47, 49, "Chłopka"),
        (50, 50, "Górnik"),
        (51, 52, "Łowczyni"),
        (53, 53, "Zarządca"),
        (54, 56, "Zielarka"),
        (57, 57, "Zwiadowca"),
        (58, 59, "Domokrążca"),
        (60, 62, "Kuglarka"),
        (63, 63, "Łowczyni Nagród"),
        (64, 65, "Posłaniec"),
        (66, 66, "Strażniczka Dróg"),
        (67, 68, "Woźnica"),
        (69, 71, "Doker"),
        (72, 74, "Flisak"),
        (75, 75, "Pilotka Rzeczna"),
        (76, 79, "Przemytniczka"),
        (80, 80, "Przewoźnik"),
        (81, 81, "Strażnik Rzeczny"),
        (82, 82, "Żeglarz"),
        (83, 83, "Banita"),
        (84, 84, "Paser"),
        (85, 85, "Hiena Cmentarna"),
        (86, 88, "Rajfur"),
        (89, 89, "Rekietierka"),
        (90, 90, "Szarlatan"),
        (91, 94, "Złodziej"),
        (95, 95, "Gladiator"),
        (96, 97, "Ochroniarz"),
        (98, 100, "Żołnierz")
    ],
    HIGH_ELF: [
        (1, 2, "Aptekarka"),
        (3, 6, "Czarodziej"),
        (7, 8, "Medyczka"),
        (9, 12, "Prawniczka"),
        (13, 16, "Uczony"),
        (17, 21, "Kupiec"),
        (22, 23, "Mieszczka"),
        (24, 26, "Rzemieślniczka"),
        (27, 27, "Strażnik"),
        (28, 29, "Śledczy"),
        (30, 30, "Artystka"),
        (31, 32, "Doradca"),
        (33, 34, "Namiestnik"),
        (35, 37, "Poseł"),
        (38, 40, "Szlachcic"),
        (41, 43, "Szpieg"),
        (44, 45, "Zwadźca"),
        (46, 48, "Łowczyni"),
        (49, 50, "Zielarka"),
        (51, 56, "Zwiadowca"),
        (57, 59, "Kuglarka"),
        (60, 62, "Łowczyni Nagród"),
        (63, 63, "Posłaniec"),
        (64, 64, "Przemytniczka"),
        (65, 65, "Przewoźnik"),
        (66, 80, "Żeglarz"),
        (81, 83, "Banita"),
        (84, 85, "Rajfur"),
        (86, 88, "Szarlatan"),
        (89, 90, "Gladiator"),
        (91, 94, "Kawalerzysta"),
        (95, 96, "Ochroniarz"),
        (97, 97, "Oprych"),
        (98, 98, "Rycerz"),
        (99, 100, "Żołnierz")
    ],
    WOOD_ELF: [
        (1, 4, "Czarodziej"),
        (5, 5, "Uczony"),
        (6, 10, "Rzemieślniczka"),
        (11, 14, "Artystka"),
        (15, 18, "Doradca"),
        (19, 25, "Poseł"),
        (26, 31, "Szlachcic"),
        (32, 35, "Szpieg"),
        (36, 45, "Łowczyni"),
        (46, 50, "Mistyczka"),
        (51, 57, "Zielarka"),
        (58, 68, "Zwiadowca"),
        (69, 73, "Kuglarka"),
        (74, 75, "Łowczyni Nagród"),
        (76, 78, "Posłaniec"),
        (79, 79, "Pirat Rzeczny"),
        (80, 85, "Banita"),
        (86, 87, "Gladiator"),
        (88, 92, "Kawalerzysta"),
        (93, 94, "Ochroniarz"),
        (95, 96, "Rycerz"),
        (97, 100, "Żołnierz")
    ]
}
professions_name_converter_table = [['Uczeń Aptekarza', 'Aptekarka'], ['Uczeń Czarodzieja', 'Czarodziej'],
                                    ['Student Inżynierii', 'Inżynier'], ['Kleryk', 'Kapłan'],
                                    ['Uczeń Lekarza', 'Medyczka'], ['Nowicjuszka', 'Mniszka'],
                                    ['Student Prawa', 'Prawniczka'], ['Student', 'Uczony'], ['Pamflecista', 'Agitator'],
                                    ['Przekupka', 'Mieszczka'], ['Czeladnik', 'Rzemieślniczka'],
                                    ['Rekrut Straży', 'Strażnik'], ['Łowca Szczurów', 'Szczurołap'],
                                    ['Szpicel', 'Śledczy'], ['Biedak', 'Żebrak'], ['Uczennica Artysty', 'Artystka'],
                                    ['Asystent', 'Doradca'], ['Nadzorca', 'Namiestnik'], ['Herold', 'Poseł'],
                                    ['Posługacz', 'Służąca'], ['Dziedzic', 'Szlachcic'], ['Informator', 'Szpieg'],
                                    ['Szermierz', 'Zwadźca'], ['Parobek', 'Chłopka'], ['Poszukiwacz', 'Górnik'],
                                    ['Uczeń Guślarza', 'Guślarz'], ['Traper', 'Łowczyni'], ['Wróżbiarz', 'Mistyczka'],
                                    ['Poborca Podatków', 'Zarządca'], ['Zbieraczka Ziół', 'Zielarka'],
                                    ['Przewodnik', 'Zwiadowca'], ['Gorliwiec', 'Biczownik'],
                                    ['Handlarz', 'Kupiec'], ['Grajek Uliczny', 'Kuglarka'],
                                    ['Oprawca', 'Łowca Czarownic'], ['Pogromczyni Złodziei', 'Łowczyni Nagród'],
                                    ['Goniec', 'Posłaniec'], ['Mytnik', 'Strażniczka Dróg'], ['Foryś', 'Woźnica'],
                                    ['Pomocnik Dokera', 'Doker'], ['Rybak', 'Flisak'],
                                    ['Przewodnik Rzeczny', 'Pilotka Rzeczna'], ['Szabrownik', 'Pirat Rzeczny'],
                                    ['Szmuglerka Rzeczna', 'Przemytniczka'], ['Chłopiec Pokładowy', 'Przewoźnik'],
                                    ['Rekrut Rzeczny', 'Strażnik Rzeczny'], ['Szczur Lądowy', 'Żeglarz'],
                                    ['Zbój', 'Banita'], ['Szeptucha', 'Czarownica'],
                                    ['Porywacz Zwłok', 'Hiena Cmentarna'], ['Pośrednik', 'Paser'],
                                    ['Naganiacz', 'Rajfur'], ['Zbir', 'Rekietierka'], ['Kanciarz', 'Szarlatan'],
                                    ['Bandzior', 'Złodziej'], ['Pięściarz', 'Gladiator'],
                                    ['Nowicjusz Kapłanów-wojowników', 'Kapłan Bitewny'], ['Jeździec', 'Kawalerzysta'],
                                    ['Stróż', 'Ochroniarz'], ['Tani Drań', 'Oprych'], ['Giermek', 'Rycerz'],
                                    [' Zabójca Trolli', 'Zabójca'], ['Rekrut', 'Żołnierz'],['Włóczykij', 'Domokrążca']]
