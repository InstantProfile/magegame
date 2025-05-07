import tkinter as tk
from tkinter import messagebox
import random
from magegame.gui import ShowTkinterApp
from magegame.core import Entity, Match
from magegame.console import MainMenu

root = tk.Tk()
root.geometry("1280x860")
initialize_game = MainMenu.Game()
create_menu = MainMenu.CreateMenu(initialize_game.mage_list)
frame1 = tk.Frame(root)
inner_frame1 = tk.Frame(frame1)
inner_frame1.pack(expand=True, anchor="center")
frame2 = tk.Frame(root)
inner_frame2 = tk.Frame(frame2)
inner_frame2.pack(expand=True, anchor="center")
frame3 = tk.Frame(root)
inner_frame3 = tk.Frame(frame3)
inner_frame3.pack(expand=True, anchor="center")
frame4 = tk.Frame(root)
inner_frame4 = tk.Frame(frame4)
inner_frame4.pack(expand=True, anchor="center")
frame5 = tk.Frame(root)
inner_frame5 = tk.Frame(frame5)
inner_frame5.pack(expand=True, anchor="center")

# func
current_frame = None
is_player_turn = True


def show_frame(frame):
    global current_frame
    if current_frame:
        current_frame.pack_forget()
    # скрыть текущий фрейм
    frame.pack(fill="both", expand=True)  # Показать новый
    current_frame = frame


def create_button(frame, text, command):
    btn = tk.Button(frame,
                    text=text,
                    font=("Arial", 20, "bold"),
                    command=command)
    return btn


def start_battle():
    global fighters, is_player_turn
    if len(initialize_game.mage_list) < 2:
        messagebox.showerror("Ошибка: Не хватает игроков")
        return

    fighters = initialize_game.mage_list[:2]
    is_player_turn = True
    update_battle_ui()
    show_frame(frame5)
    toggle_buttons(True)


# ------------------------ frame 1 go to main menu ------------------------ #
# Label
description_go_to_main_menu = tk.Label(
    inner_frame1,
    text="Добро пожаловать",
    font=("Arial", 35, "bold")
)
description_go_to_main_menu.pack(anchor="s", pady=20, expand=True)

# Button
button_go_to_main_menu = create_button(inner_frame1, "Start Game", lambda: show_frame(frame2))
button_go_to_main_menu.pack(anchor="center", pady=5)

# ------------------------ frame 2 main menu ------------------------ #
# Label
description_main_menu = tk.Label(inner_frame2, text="Главное меню", font=("Arial", 30, "bold"))
description_main_menu.pack()

# Button
button_main_menu_create_custom_person = create_button(inner_frame2,
                                                      "Создать персонажа",
                                                      lambda: show_frame(frame3))
button_main_menu_create_custom_person.pack(pady=10)
button_main_menu_create_random_person = create_button(inner_frame2,
                                                      "Рандомный персонаж",
                                                      command=lambda: [
                                                          initialize_game.mage_list.append(
                                                              ShowTkinterApp.create_random_mage_tkinter()),
                                                          show_label_create_random_person()
                                                      ]
                                                      )

button_main_menu_create_random_person.pack(pady=10)
button_main_menu_show_person = tk.Button(
    inner_frame2,
    text="Список персонажей",
    font=("Arial", 20, "bold"),
    command=lambda: [show_frame(frame4), update_mage_labels()]
)
button_main_menu_show_person.pack(pady=10)

button_main_menu_start_game = tk.Button(inner_frame2,
                                        text="Начать игру",
                                        font=("Arial", 20, "bold"),
                                        command=start_battle)
button_main_menu_start_game.pack(pady=10)
button_main_menu_back = tk.Button(inner_frame2,
                                  text="Назад",
                                  font=("Arial", 20, "bold"),
                                  command=lambda: show_frame(frame1))
button_main_menu_back.pack(pady=10)


def show_label_create_random_person():
    label = tk.Label(inner_frame2, text="Рандомный персонаж создан!", font=("Arial", 20))
    label.pack(pady=5)
    label.after(2000, label.destroy)


# ------------------------ frame 3 create_custom_person ------------------------ #
description_create_person_back = tk.Label(inner_frame3, text="Создание персонажа", font=("Arial", 20, "bold"))
description_create_person_back.pack(pady=15)

# Создаем поле ввода Имя
name_label = tk.Label(inner_frame3, text="Имя персонажа", font=("Arial", 20, "bold"))
name_label.pack()
entry_name = tk.Entry(inner_frame3, width=15, font=("Arial", 20, "bold"))
entry_name.pack(pady=10)

# Создаем поле ввода Урон
damage_label = tk.Label(inner_frame3, text="Урон", font=("Arial", 20, "bold"))
damage_label.pack()
entry_damage = tk.Entry(inner_frame3, width=15, font=("Arial", 20, "bold"))
entry_damage.pack(pady=10)

# Создаем поле ввода Броня
armor_label = tk.Label(inner_frame3, text="Броня", font=("Arial", 20, "bold"))
armor_label.pack()
entry_armor = tk.Entry(inner_frame3, width=15, font=("Arial", 20, "bold"))
entry_armor.pack(pady=10)

result_label = tk.Label(inner_frame3, font=("Arial", 20, "bold"))
result_label.pack(pady=10)

# Метка для вывода результата
result_label = tk.Label(inner_frame3, font=("Arial", 20, "bold"))
result_label.pack(pady=20)


def show_label_create_custom_person(name):
    label = tk.Label(inner_frame2, text=f"Персонаж {name} создан!", font=("Arial", 20))
    label.pack(pady=5)
    label.after(2000, label.destroy)


def save_all():
    name = entry_name.get()  # Удаляем пробелы в начале и конце
    damage_str = entry_damage.get()
    armor_str = entry_armor.get()
    # Отладочный вывод для проверки значений (можно удалить после тестирования)
    # print(f"[DEBUG] Name: '{name}', Damage: '{damage_str}', Armor: '{armor_str}'")

    # Проверка на пустые поля
    if not name or not damage_str or not armor_str:
        messagebox.showerror("Ошибка", "Все поля должны быть заполнены!")
        return

    try:
        damage = int(damage_str)
        armor = int(armor_str)
    except ValueError:
        messagebox.showerror("Ошибка", "Урон и Броня должны быть целыми числами!")
        return

    # Создаем персонажа
    mage = Entity.Person(name, 0, 5)

    # Устанавливаем характеристики и проверяем ошибки
    error = mage.set_stats(damage, armor)
    if error:
        messagebox.showerror("Ошибка", error)
        return

    initialize_game.mage_list.append(mage)

    # Очищаем поля
    entry_name.delete(0, tk.END)
    entry_damage.delete(0, tk.END)
    entry_armor.delete(0, tk.END)

    # Возвращаемся в главное меню (frame2)
    show_frame(frame2)
    show_label_create_custom_person(name)
    # Обновляем вывод (если нужно)
    # result_label.config(text=f"Создан: {mage.get_stats()}")


# Кнопка для подтверждения ввода
btn_save = tk.Button(
    inner_frame3,
    text="Сохранить всё",
    command=save_all,
    font=("Arial", 20, "bold"),
    bg="#4CAF50",
    fg="white"
)
btn_save.pack(pady=20)

button_create_person_back = tk.Button(inner_frame3,
                                      text="Назад",
                                      font=("Arial", 20, "bold"),
                                      command=lambda: show_frame(frame2))
button_create_person_back.pack()

# ------------------------ frame 4 show_person ------------------------ #

# Элементы для отображения списка
title_label = tk.Label(
    inner_frame4,
    text="Список персонажей",
    font=("Arial", 20, "bold")
)
title_label.pack(pady=10)

back_button = tk.Button(
    inner_frame4,
    text="Назад",
    font=("Arial", 16, "bold"),
    command=lambda: show_frame(frame2)
)
back_button.pack(pady=10)

list_container = tk.Frame(inner_frame4)
list_container.pack(anchor="center", expand=True, before=back_button)


def update_mage_labels():
    # Удаляем только метки персонажей
    for widget in list_container.winfo_children():
        widget.destroy()

    # Добавляем персонажей в контейнер списка
    for mage in initialize_game.mage_list:
        lbl = tk.Label(
            list_container,
            text=(
                f"{mage.name} | "
                f"HP: {mage.health} | "
                f"DMG: {mage.damage} | "
                f"ARM: {mage.armor}"
            ),
            font=("Arial", 12),
            relief="groove",
            padx=10,
            pady=5
        )
        lbl.pack(fill="x", pady=2)


# ------------------------ Frame 5 start battle ------------------------ #

# Элементы управления боем
battle_status = tk.StringVar()
lbl_status = tk.Label(inner_frame5, textvariable=battle_status, font=("Arial", 16))
lbl_status.pack(pady=20)

# Лог действий
log_frame = tk.Frame(inner_frame5)
log_frame.pack(pady=10, fill=tk.BOTH, expand=True)

log_text = tk.Text(log_frame, height=8, width=50, font=("Arial", 12), state=tk.DISABLED)
scrollbar = tk.Scrollbar(log_frame, command=log_text.yview)
log_text.configure(yscrollcommand=scrollbar.set)

log_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

action_frame = tk.Frame(inner_frame5)
action_frame.pack(pady=10)

btn_attack = tk.Button(action_frame, text="Атака", font=("Arial", 14), command=lambda: player_turn(1))

btn_defense = tk.Button(action_frame, text="Защита", font=("Arial", 14), command=lambda: player_turn(2))

btn_heal = tk.Button(action_frame, text="Лечение", font=("Arial", 14), command=lambda: player_turn(3))

btn_attack.pack(side=tk.LEFT, padx=5)
btn_defense.pack(side=tk.LEFT, padx=5)
btn_heal.pack(side=tk.LEFT, padx=5)

btn_back = tk.Button(inner_frame5, text="Назад", font=("Arial", 14), command=lambda: reset_battle())
btn_back.pack(pady=20)


def player_turn(action):
    global is_player_turn
    player, bot = fighters
    Match.players_selection(player, bot, action, initialize_game.mage_list, output_callback=update_log)
    is_player_turn = False
    toggle_buttons(False)
    update_battle_ui()
    Match.update_step_mage(player)
    root.after(1000, bot_turn)


def bot_turn():
    global is_player_turn
    if check_battle_end():
        return
    player, bot = fighters
    fight_manager = Match.StartFight(
        game_state=fighters,
        input_callback=lambda: None,
        output_callback=update_log
    )
    fight_manager.selection_bot(bot, player, initialize_game.mage_list, update_log)
    update_battle_ui()
    Match.update_step_mage(bot)
    if not check_battle_end():
        root.after(1000, lambda: [toggle_buttons(True), set_player_turn(True)])


def set_player_turn(value):
    global is_player_turn
    is_player_turn = value


def update_battle_ui():
    status = ""

    for mage in fighters:
        status += f"{mage.name}: ❤{mage.health} 🛡{mage.armor} {mage.step}\n"

    battle_status.set(status)
    check_battle_end()


def reset_battle():
    global fighters
    for mage in fighters:
        mage.health = Entity.Person.BASE_HP
    log_text.config(state=tk.NORMAL)
    log_text.delete(1.0, tk.END)  # Очищаем лог
    log_text.config(state=tk.DISABLED)
    battle_status.set("")  # Сбрасываем статус
    show_frame(frame2)


# def check_battle_end():
#     for mage in fighters:
#         if mage.health <= 0:
#             winner = fighters[0] if fighters[1].health <= 0 else fighters[1]
#             battle_status.set(f"{battle_status.get()}\n\nПобедитель: {winner.name}!")
#             toggle_buttons(False)
#             return True
#     return False
def check_battle_end():
    for mage in fighters:
        if mage.health <= 0:
            winner = fighters[0] if fighters[1].health <= 0 else fighters[1]
            # Заменяем содержимое вместо добавления
            battle_status.set(f"{fighters[0].name}: ❤{fighters[0].health} 🛡{fighters[0].armor}\n"
                              f"{fighters[1].name}: ❤{fighters[1].health} 🛡{fighters[1].armor}"
                              f"\n\nПобедитель: {winner.name}!")
            toggle_buttons(False)
            return True
    return False


def toggle_buttons(state):
    global fighters
    player, bot = fighters

    # Всегда блокируем кнопки, если state = False (бой завершен)
    if not state:
        btn_attack.config(state=tk.DISABLED)
        btn_heal.config(state=tk.DISABLED)
        btn_defense.config(state=tk.DISABLED)
        return

    # Блокируем "Защиту", если у игрока активна броня (step > 0)
    defense_state = tk.DISABLED if player.step > 0 else tk.NORMAL

    btn_attack.config(state=tk.NORMAL)
    btn_heal.config(state=tk.NORMAL)
    btn_defense.config(state=defense_state)


def reset_battle():
    global fighters
    for mage in fighters:
        mage.health = Entity.Person.BASE_HP
    show_frame(frame2)


def update_log(message):
    log_text.config(state=tk.NORMAL)  # Разблокируем для редактирования
    log_text.insert(tk.END, message + "\n")  # Добавляем сообщение
    log_text.see(tk.END)  # Автоматическая прокрутка к новому сообщению
    log_text.config(state=tk.DISABLED)  # Блокируем обратно


show_frame(frame1)

root.mainloop()

# BASE_STYLE = {
#     'bg': '#4CAF50',  # Цвет фона
#     'fg': 'white',  # Цвет текста
#     'font': ('Arial', 25, "bold"),  # Шрифт и размер
#     'padx': 20,  # Отступ по горизонтали
#     'pady': 10,  # Отступ по вертикали
#     'borderwidth': 2,  # Толщина рамки
#     'relief': 'groove'  # Стиль рамки (flat, raised, sunken, groove, ridge)
# }
#
#
# class MainApp(tk.Tk):
#     def __init__(self):
#         super().__init__()
#         self.geometry("1280x860+300+100")
#         self.title("mainApp")
#         self.frames = {}
#
#         for F in (MainMenu, CreateChar): #BattleScreen):
#             frame = F(parent=self, controller=self)
#             self.frames[F.__name__] = frame
#             # frame.grid(row=0, column=0, sticky="nsew")
#             frame.pack(expand=True, fill='both', pady=250)
#             self.show_frame("MainMenu")
#
#     def show_frame(self, name):
#         self.frames[name].tkraise()
#
#
# class MainMenu(tk.Frame):
#     def __init__(self, parent, controller):
#         super().__init__(parent)
#         self.controller = controller
#
#         main_container = tk.Frame(self, )
#         main_container.pack(expand=True, fill='both')
#         label_main = tk.Label(self, text="Главное меню", font=('Arial', 25, "bold"),padx=20,pady=10,)
#         btn_create = tk.Button(self, text="Создать персонажа 🧙",
#                                command=lambda: controller.show_frame("CreateChar"), **BASE_STYLE)
#         btn_show_list = tk.Button(self, text="Список игроков", command=lambda: print("Список игроков"), **BASE_STYLE)
#         btn_battle = tk.Button(self, text="Начать бой ⚔️",
#                                command=lambda: controller.show_frame("BattleScreen"), **BASE_STYLE)
#         label_main.pack(pady=10)
#         btn_create.pack(pady=10, anchor='center')
#         btn_show_list.pack(pady=10, anchor='center')
#         btn_battle.pack(pady=10, anchor='center')
#         btn_create.bind("<Enter>", lambda e: btn_create.config(bg='#45a049'))
#         btn_create.bind("<Leave>", lambda e: btn_create.config(bg=BASE_STYLE['bg']))
#         btn_show_list.bind("<Enter>", lambda e: btn_show_list.config(bg='#45a049'))
#         btn_show_list.bind("<Leave>", lambda e: btn_show_list.config(bg=BASE_STYLE['bg']))
#         btn_battle.bind("<Enter>", lambda e: btn_battle.config(bg='#45a049'))
#         btn_battle.bind("<Leave>", lambda e: btn_battle.config(bg=BASE_STYLE['bg']))
#
#
# class CreateChar(tk.Frame):
#     def __init__(self, parent, controller):
#         super().__init__(parent)
#         self.controller = controller
#
#         # Контейнер для кнопок выбора типа создания
#         self.choice_frame = tk.Frame(self)
#         self.choice_frame.pack(pady=50, expand=True)
#
#         # Кнопки выбора
#         btn_manual = tk.Button(
#             self.choice_frame,
#             text="Ручное создание 🛠️",
#             command=self.show_manual_creation,
#             **BASE_STYLE
#         )
#
#         btn_random = tk.Button(
#             self.choice_frame,
#             text="Случайный персонаж 🎲",
#             command=self.create_random_character,
#             **BASE_STYLE
#         )
#
#         btn_manual.pack(pady=15)
#         btn_random.pack(pady=15)
#
#         # Контейнер для форм создания
#         self.forms_container = tk.Frame(self)
#         self.forms_container.pack(fill='both', expand=True)
#
#         # Инициализация подфреймов
#         self.manual_frame = ManualCreationFrame(self.forms_container, controller)
#         self.random_frame = RandomCreationFrame(self.forms_container, controller)
#
#     def show_manual_creation(self):
#         """Показать форму ручного ввода"""
#         self.choice_frame.pack_forget()
#         self.manual_frame.pack(fill='both', expand=True)
#
#     def create_random_character(self):
#         """Создание случайного персонажа"""
#         name = f"Маг-{random.randint(100, 999)}"
#         new_mage = Entity.Person(name, 0, 5).set_random_stat()
#         self.controller.mage_list.append(new_mage)
#         messagebox.showinfo("Успех", f"Создан случайный персонаж: {name}")
#         self.controller.show_frame("MainMenu")
#
#
# class ManualCreationFrame(tk.Frame):
#     def __init__(self, parent, controller):
#         super().__init__(parent)
#         # Твоя текущая форма ручного ввода
#         lbl = tk.Label(self, text="Ручное создание", font=('Arial', 20))
#         lbl.pack(pady=20)
#
#         # ... остальные элементы формы ...
#
#
# class RandomCreationFrame(tk.Frame):
#     def __init__(self, parent, controller):
#         super().__init__(parent)
#         lbl = tk.Label(self, text="Подтвердите создание", font=('Arial', 20))
#         lbl.pack(pady=50)
#
#         btn_confirm = tk.Button(
#             self,
#             text="Сгенерировать случайно ✅",
#             command=lambda: print("Логика генерации"),
#             **BASE_STYLE
#         )
#         btn_confirm.pack()
#
# class BattleScreen(tk.Frame):
#     pass
#
#
# app = MainApp()
# app.mainloop()
