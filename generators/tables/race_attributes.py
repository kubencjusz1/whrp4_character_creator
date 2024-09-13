from generators.globals import *
attributes_table = {
    HUMAN: {WW: 20, US: 20, S: 20, WT: 20, I: 20, ZW: 20, ZR: 20, INT: 20, SW: 20, OGD: 20},
    DWARF: {WW: 30, US: 20, S: 20, WT: 30, I: 20, ZW: 10, ZR: 30, INT: 20, SW: 40, OGD: 10},
    HALFLING: {WW: 10, US: 30, S: 10, WT: 20, I: 20, ZW: 20, ZR: 30, INT: 20, SW: 30, OGD: 30},
    HIGH_ELF: {WW: 30, US: 30, S: 20, WT: 20, I: 40, ZW: 30, ZR: 30, INT: 30, SW: 30, OGD: 20},
    WOOD_ELF: {WW: 30, US: 30, S: 20, WT: 20, I: 40, ZW: 30, ZR: 30, INT: 30, SW: 30, OGD: 20}}
points_speed_table = {HUMAN: {DESTINY_POINTS: 2, HERO_POINTS: 1, POINTS_TO_CHOOSE: 3, SPEED: 4},
                      DWARF: {DESTINY_POINTS: 0, HERO_POINTS: 2, POINTS_TO_CHOOSE: 2, SPEED: 3},
                      HALFLING: {DESTINY_POINTS: 0, HERO_POINTS: 2, POINTS_TO_CHOOSE: 3, SPEED: 3},
                      HIGH_ELF: {DESTINY_POINTS: 0, HERO_POINTS: 0, POINTS_TO_CHOOSE: 2, SPEED: 5},
                      WOOD_ELF: {DESTINY_POINTS: 0, HERO_POINTS: 0, POINTS_TO_CHOOSE: 2, SPEED: 5}}
