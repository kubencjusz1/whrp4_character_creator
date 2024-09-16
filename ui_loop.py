import tkinter as tk
from generators.character import Character
from generators.globals import *
from generators.tables.race_attributes import attributes_table
from generators.ui import *
from tkinter import messagebox


class CharacterApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.initialise_character()

        self.configure(bg="#f0f0f0")
        self.title("Character sheet creator for WHRP 4ed by Kubencjusz")
        self.main_frame = tk.Frame(self)
        self.main_frame.grid(row=0, column=0, padx=10, pady=10)

        self.race_class_profession_frame()

        self.switch_frame()

        self.other_attributes()

        self.attributes_spinbox_map = {}
        self.talents_combobox_map = {}
        self.race_skills_combobox_map = {}
        self.profession_skills_spinbox_map = {}

        self.skills_talents_frame()

        self.aesthetics_and_name()

    def initialise_character(self):
        self.new_character = Character()
        self.new_character.get_race()
        self.new_character.get_profession_and_class()

        self.var_race = tk.StringVar(value=self.new_character.race)
        self.var_profession = tk.StringVar(value=self.new_character.profession)
        self.var_status = tk.StringVar(value=self.new_character.status)
        self.var_character_class = tk.StringVar(value=self.new_character.character_class)

        self.var_point_buy_skills = tk.IntVar(value=40)
        self.initialise_character_attributes()
        self.initialize_skills_and_talents()
        self.initialize_aesthetics()

    def initialise_character_attributes(self):
        # attributes = {"WW": 0, "US": 0, "S": 0, "Wt": 0, "I": 0, "Zw": 0, "Zr": 0, "Int": 0, "SW": 0, "Ogd": 0}
        self.att_race_table = attributes_table.get(self.new_character.race)
        self.new_character.get_attributes()
        self.var_att_points = tk.IntVar(self, 100)
        self.max_bonus = 18
        self.var_ww = tk.IntVar(value=self.new_character.attributes.get(WW))
        self.var_us = tk.IntVar(value=self.new_character.attributes.get(US))
        self.var_s = tk.IntVar(value=self.new_character.attributes.get(S))
        self.var_wt = tk.IntVar(value=self.new_character.attributes.get(WT))
        self.var_i = tk.IntVar(value=self.new_character.attributes.get(I))
        self.var_zw = tk.IntVar(value=self.new_character.attributes.get(ZW))
        self.var_zr = tk.IntVar(value=self.new_character.attributes.get(ZR))
        self.var_int = tk.IntVar(value=self.new_character.attributes.get(INT))
        self.var_sw = tk.IntVar(value=self.new_character.attributes.get(SW))
        self.var_ogd = tk.IntVar(value=self.new_character.attributes.get(OGD))
        self.var_ww_bonus = tk.IntVar(value=0)
        self.var_us_bonus = tk.IntVar(value=0)
        self.var_s_bonus = tk.IntVar(value=0)
        self.var_wt_bonus = tk.IntVar(value=0)
        self.var_i_bonus = tk.IntVar(value=0)
        self.var_zw_bonus = tk.IntVar(value=0)
        self.var_zr_bonus = tk.IntVar(value=0)
        self.var_int_bonus = tk.IntVar(value=0)
        self.var_sw_bonus = tk.IntVar(value=0)
        self.var_ogd_bonus = tk.IntVar(value=0)
        self.labels_text = [WW, US, S, WT, I, ZW, ZR, INT, SW, OGD]
        self.var_attributes_list = [self.var_ww, self.var_us, self.var_s, self.var_wt, self.var_i,
                                    self.var_zw, self.var_zr, self.var_int, self.var_sw, self.var_ogd]
        self.var_attributes_bonus_list = [self.var_ww_bonus, self.var_us_bonus, self.var_s_bonus, self.var_wt_bonus,
                                          self.var_i_bonus,
                                          self.var_zw_bonus, self.var_zr_bonus, self.var_int_bonus, self.var_sw_bonus,
                                          self.var_ogd_bonus]
        self.var_speed = tk.IntVar(value=self.new_character.speed)
        self.var_hp = tk.IntVar(value=self.new_character.hp)
        self.var_points_to_choose = tk.IntVar(value=self.new_character.points_to_choose)
        self.var_hero_points = tk.IntVar(value=self.new_character.hero_points)
        self.var_destiny_points = tk.IntVar(value=self.new_character.destiny_points)

    def initialize_skills_and_talents(self):

        self.new_character.get_talents()
        self.new_character.get_skills()
        if (len(self.new_character.skills.get(PROFESSION_SKILLS)[0])) != 8:
            print("Błąd plików", self.new_character.true_profession)

    def initialize_aesthetics(self):
        self.new_character.get_name_and_look()
        self.var_name = tk.StringVar(value=self.new_character.name)
        self.var_name.trace("w", self.adjust_width)
        self.var_hight = tk.StringVar(value=self.new_character.height)
        self.var_age = tk.StringVar(value=self.new_character.age)
        self.var_hair_color = tk.StringVar(value=self.new_character.hair_color)
        self.var_eye_color = tk.StringVar(value=self.new_character.eye_color)

    def reset_stats(self):
        self.var_ww.set(self.new_character.attributes.get(WW))
        self.var_us.set(self.new_character.attributes.get(US))
        self.var_s.set(self.new_character.attributes.get(S))
        self.var_wt.set(self.new_character.attributes.get(WT))
        self.var_i.set(self.new_character.attributes.get(I))
        self.var_zw.set(self.new_character.attributes.get(ZW))
        self.var_zr.set(self.new_character.attributes.get(ZR))
        self.var_int.set(self.new_character.attributes.get(INT))
        self.var_sw.set(self.new_character.attributes.get(SW))
        self.var_ogd.set(self.new_character.attributes.get(OGD))

    def race_class_profession_frame(self):
        frame = tk.LabelFrame(self.main_frame, text="Rasa Klasa i Profesja")
        frame.grid(row=0, column=0, padx=10, pady=10)

        entry_with_label(frame, "Rasa", var=self.var_race, row=0, column=0)

        profession_label = tk.Label(frame, text="Profesja")
        profession_label.grid(row=0, column=1)
        status_label = tk.Label(frame, text="Status")
        status_label.grid(row=0, column=2)
        class_label = tk.Label(frame, text="Klasa")
        class_label.grid(row=0, column=3)

        profession_entry = tk.Entry(frame, textvariable=self.var_profession)
        profession_entry.grid(row=1, column=1)
        status_entry = tk.Entry(frame, textvariable=self.var_status)
        status_entry.grid(row=1, column=2)
        class_entry = tk.Entry(frame, textvariable=self.var_character_class)
        class_entry.grid(row=1, column=3)

        reroll_profession_button = tk.Button(frame, text="Przerzuć profesję", command=self.reroll_profession)
        reroll_profession_button.grid(row=2, column=1)

        for widget in frame.winfo_children():
            widget.grid_configure(padx=5, pady=5)

    def reroll_profession(self):
        self.new_character.get_profession_and_class()
        self.initialize_skills_and_talents()
        self.var_race.set(self.new_character.race)
        self.var_profession.set(self.new_character.true_profession)
        self.var_status.set(self.new_character.status)
        self.var_character_class.set(self.new_character.character_class)

        self.profession_talent_combobox.destroy()
        self.profession_talent_combobox = ttk.Combobox(self.sub_frame1,
                                                       values=self.new_character.talents.get(PROFESSION_TALENTS)[0])
        self.profession_talent_combobox.grid(row=1, column=len(self.new_character.talents.get(RACE_TALENTS)), padx=5,
                                             pady=5)
        for widget in self.sub_frame4.winfo_children():
            widget.destroy()
        length_profession_skills = len(self.new_character.skills.get(PROFESSION_SKILLS)[0])
        for i in range(length_profession_skills):
            spinbox = spinbox_with_label(self.sub_frame4, text=self.new_character.skills.get(PROFESSION_SKILLS)[0][i],
                                         var=None, from_=0, to=10, column=i, row=0)
            self.profession_skills_spinbox_map[spinbox] = f"{self.new_character.skills.get(PROFESSION_SKILLS)[0][i]}"
            spinbox.bind("<<Increment>>", self.skills_spinbox_plus)
            spinbox.bind("<<Decrement>>", self.skills_spinbox_minus)
            spinbox.set(0)
        label_with_label(self.sub_frame4, text="Punkty do wydania", var=self.var_point_buy_skills,
                         column=length_profession_skills + 1)

    def switch_frame(self):
        self.mode = tk.StringVar(value="Losowo")
        radio_button_frame = ttk.Frame(self.main_frame)
        radio_button_frame.grid(row=1, column=0, padx=10, pady=10)
        # self.attributes = {"WW": 0, "US": 0, "S": 0, "Wt": 0, "I": 0, "Zw": 0, "Zr": 0, "Int": 0, "SW": 0, "Ogd": 0}

        ttk.Radiobutton(radio_button_frame, text="Losowo", variable=self.mode, value="Losowo",
                        command=self.switch_state).grid(row=0, column=0, padx=10, pady=10)
        ttk.Radiobutton(radio_button_frame, text="Zmienianie", variable=self.mode, value="Zmienianie",
                        command=self.switch_state).grid(row=0, column=1, padx=10, pady=10)
        ttk.Radiobutton(radio_button_frame, text="Point buy", variable=self.mode, value="Point buy",
                        command=self.switch_state).grid(row=0, column=2, padx=10, pady=10)

        self.state_frame = ttk.LabelFrame(self.main_frame, text="Lista attrybutów")
        self.state_frame.grid(row=2, column=0, padx=10, pady=10)

        self.switch_state()
        self.bonus_attributes()

    def switch_state(self):
        # Clear the frame
        for widget in self.state_frame.winfo_children():
            widget.destroy()

        state = self.mode.get()

        if state == "Losowo":
            self.reset_stats()
            self.create_state1()
            self.bonus_attributes()
        elif state == "Zmienianie":
            self.reset_stats()
            self.create_state1()
            self.bonus_attributes()
            self.mode.set("Losowo")
            messagebox.showinfo(title="Uwaga", message="Prace trwają, na razie nie działa")
        elif state == "Point buy":
            if messagebox.askyesno(title="Ostrzeżenie!",
                                   message="Czy chcesz zrezygnować z wylosowanych wartości?"):
                self.create_state3()
                self.bonus_attributes()
            else:
                self.mode.set("Losowo")
                self.create_state1()
                self.bonus_attributes()

    def create_state1(self):
        for i in range(len(self.var_attributes_list)):
            frame = ttk.Frame(self.state_frame)
            frame.grid(row=0, column=i, padx=5, pady=5)
            label_with_label(frame, text=self.labels_text[i], var=self.var_attributes_list[i], column=i, row=0)

    def create_state2(self):
        # In state 2, we can swap labels and entries
        for i in range(len(self.var_attributes_list)):
            frame = ttk.Frame(self.state_frame)
            frame.grid(row=0, column=i, padx=5, pady=5)

            entry = DraggableLabel(self.state_frame, textvariable=self.var_attributes_list[i])
            entry.grid(row=0, column=i, padx=5, pady=5)

            label = ttk.Label(self.state_frame, text=self.labels_text[i])
            label.grid(row=1, column=i, padx=15, pady=5)

    def create_state3(self):
        for i in range(len(self.var_attributes_list)):
            self.var_attributes_list[i].set(self.att_race_table.get(self.labels_text[i]))
            frame = ttk.Frame(self.state_frame)
            frame.grid(row=0, column=i, padx=5, pady=5)

            spinbox = spinbox_with_label(frame, text=self.labels_text[i], var=self.var_attributes_list[i], column=i,
                                         row=0, from_=self.att_race_table.get(self.labels_text[i]),
                                         to=self.att_race_table.get(self.labels_text[i]) + self.max_bonus)
            # ,lambda event: self.on_spinbox_plus(event, self.var_attributes_list[i].get()))
            spinbox.bind("<<Increment>>", self.attributes_spinbox_plus)
            spinbox.bind("<<Decrement>>", self.attributes_spinbox_minus)
            self.attributes_spinbox_map[spinbox] = f"{self.labels_text[i]}"

        label_with_label(self.state_frame, var=self.var_att_points, text="Ilość puntków do wydania", row=0,
                         column=len(self.var_attributes_list) + 1)

    def attributes_spinbox_plus(self, event):
        spinbox = event.widget  # ._name
        spinbox_id = self.attributes_spinbox_map.get(spinbox, "Unknown Spinbox")
        if int(spinbox.get()) < self.att_race_table.get(spinbox_id) + self.max_bonus:
            self.var_att_points.set(self.var_att_points.get() - 1)

    def attributes_spinbox_minus(self, event):
        if self.var_att_points.get() < 100:
            self.var_att_points.set(self.var_att_points.get() + 1)

    def bonus_attributes(self):
        for i in range(len(self.var_attributes_bonus_list)):
            frame = ttk.Frame(self.state_frame)
            frame.grid(row=3, column=i, padx=5, pady=5)
            spinbox = ttk.Spinbox(frame,
                                  textvariable=self.var_attributes_bonus_list[i],
                                  from_=0,
                                  to=5,
                                  width=5)
            spinbox.grid(row=3, column=i, padx=5, pady=5)

    def other_attributes(self):
        frame = tk.LabelFrame(self.main_frame, text="Pozostałe atrybuty")
        frame.grid(row=3, column=0, padx=10, pady=10)

        label_with_label(frame, text="Prędfkość", var=self.var_speed, column=0, row=0)
        label_with_label(frame, text="Punkty trafień", var=self.var_hp, column=1, row=0)
        label_with_label(frame, text="Ilość puntków do wydania", var=self.var_points_to_choose, column=2, row=0)
        spinbox_with_label(frame, text="Punkty przeznaczenia", var=self.var_destiny_points, column=3, row=0,
                           from_=self.var_destiny_points.get(),
                           to=self.var_points_to_choose.get() + self.var_destiny_points.get())
        spinbox_with_label(frame, text="Punkty bohatera", var=self.var_hero_points, column=4, row=0,
                           from_=self.var_hero_points.get(),
                           to=self.var_points_to_choose.get() + self.var_hero_points.get())

    def skills_talents_frame(self):
        skill_talent_frame = tk.LabelFrame(self.main_frame, text="Umiejętności i Talenty")
        skill_talent_frame.grid(row=4, column=0, padx=5, pady=5)
        length_talents = len(self.new_character.talents.get(RACE_TALENTS))
        length_profession_skills = len(self.new_character.skills.get(PROFESSION_SKILLS)[0])

        self.sub_frame1 = tk.LabelFrame(skill_talent_frame, text="Talenty")
        self.sub_frame1.grid(row=0, column=0, padx=5, pady=5)

        for i in range(length_talents):
            combobox = ttk.Combobox(self.sub_frame1, values=self.new_character.talents.get(RACE_TALENTS)[i])
            combobox.grid(row=1, column=i, padx=5, pady=5)
            if len(self.new_character.talents.get(RACE_TALENTS)[i]) == 1:
                combobox.set(self.new_character.talents.get(RACE_TALENTS)[i][0])
            self.talents_combobox_map[combobox] = f"{self.new_character.talents.get(RACE_TALENTS)[i][0]}"

        label = ttk.Label(self.sub_frame1, text="Talent z Profesji")
        label.grid(row=0, column=length_talents, padx=5, pady=5)
        self.profession_talent_combobox = ttk.Combobox(self.sub_frame1,
                                                       values=self.new_character.talents.get(PROFESSION_TALENTS)[0])
        self.profession_talent_combobox.grid(row=1, column=length_talents, padx=5, pady=5)

        sub_frame2 = tk.LabelFrame(skill_talent_frame, text="Umiejętności rasowe +5")
        sub_frame2.grid(row=3, column=0, padx=5, pady=5)
        for i in range(3):
            combobox = ttk.Combobox(sub_frame2, values=self.new_character.skills.get(RACE_SKILLS))
            combobox.grid(row=0, column=i, padx=5, pady=5)
            self.race_skills_combobox_map[combobox] = f"Plus_Five{i}"

        sub_frame3 = tk.LabelFrame(skill_talent_frame, text="Umiejętności rasowe +3")
        sub_frame3.grid(row=4, column=0, padx=5, pady=5)
        for i in range(3, 6):
            combobox = ttk.Combobox(sub_frame3, values=self.new_character.skills.get(RACE_SKILLS))
            combobox.grid(row=0, column=i, padx=5, pady=5)
            self.race_skills_combobox_map[combobox] = f"Plus_Three{i}"

        self.sub_frame4 = tk.LabelFrame(skill_talent_frame, text="Umiejętności z pofesji")
        self.sub_frame4.grid(row=5, column=0, padx=5, pady=5)
        for i in range(length_profession_skills):
            spinbox = spinbox_with_label(self.sub_frame4, text=self.new_character.skills.get(PROFESSION_SKILLS)[0][i],
                                         var=None, from_=0, to=10, column=i, row=0)
            spinbox.set(0)
            self.profession_skills_spinbox_map[spinbox] = f"{self.new_character.skills.get(PROFESSION_SKILLS)[0][i]}"
            spinbox.bind("<<Increment>>", self.skills_spinbox_plus)
            spinbox.bind("<<Decrement>>", self.skills_spinbox_minus)
        label_with_label(self.sub_frame4, text="Punkty do wydania", var=self.var_point_buy_skills,
                         column=length_profession_skills + 1)

    def skills_spinbox_plus(self, event):
        value = event.widget.get()
        if int(value) < 10:
            self.var_point_buy_skills.set(self.var_point_buy_skills.get() - 1)

    def skills_spinbox_minus(self, event):
        value = event.widget.get()
        if int(value) > 0:
            self.var_point_buy_skills.set(self.var_point_buy_skills.get() + 1)

    def aesthetics_and_name(self):
        frame = tk.LabelFrame(self.main_frame, text="Wygląd i imie")
        frame.grid(row=5, column=0, padx=5, pady=5)

        self.name_entry = entry_with_label(frame, text="Imię", column=0, var=self.var_name)
        self.adjust_width()
        entry_with_label(frame, text="Wzorst", column=1, var=self.var_hight)
        entry_with_label(frame, text="Wiek", column=2, var=self.var_age)
        entry_with_label(frame, text="Kolor włosów", column=3, var=self.var_hair_color)
        entry_with_label(frame, text="Kolor oczu", column=4, var=self.var_eye_color)

        reroll_profession_button = tk.Button(frame, text="Przerzuć", command=self.reroll_aesthetics_and_name)
        reroll_profession_button.grid(row=1, column=5, pady=5)

    def reroll_aesthetics_and_name(self):
        self.new_character.get_name_and_look()
        self.var_name.set(value=self.new_character.name)
        self.var_hight.set(value=self.new_character.height)
        self.var_age.set(value=self.new_character.age)
        self.var_hair_color.set(value=self.new_character.hair_color)
        self.var_eye_color.set(value=self.new_character.eye_color)

    def adjust_width(self):
        current_text = self.var_name.get()
        self.name_entry.config(width=len(current_text) + 1)


if __name__ == "__main__":
    app = CharacterApp()
    app.mainloop()
