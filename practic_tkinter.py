import tkinter as tk

from project.magegame import MainMenu

root = tk.Tk()
initialize_game = MainMenu.Game()
create_menu = MainMenu.CreateMenu(initialize_game.mage_list)

root.title("Game Battle")
root.geometry("1280x860")

# Метка
# description = tk.Label(root,
#                        text="Добро Пожаловать",
#                        font=("Arial", 16, "bold"),
#                        pady=80,
#                        height=5,
#                        anchor="s",
#                        )
# description.pack()
# button = tk.Button(
#     root,
#     text="Start Settings Game",
#     command=lambda: print("Кнопка нажата"),
#     bg="lightblue",
#     fg="black"
# )
# button.pack(pady=10)
# Кнопка
# button = tk.Button(root, text="Нажми меня", command=lambda: print("Кнопка нажата"))
# button.pack(pady=10)
# def show_screen1():
#     # Удалить все текущие виджеты
#     for widget in root.winfo_children():
#         widget.destroy()
#     # Создать виджеты для экрана 1
#     description = tk.Label(root,
#                            text="Добро Пожаловать",
#                            font=("Arial", 16, "bold"),
#                            pady=80,
#                            height=5,
#                            anchor="s",
#                            )
#     description.pack()
#     tk.Button(root, text="Старт игры", command=show_screen2).pack()
#
# def show_screen2():
#     for widget in root.winfo_children():
#         widget.destroy()
#     # Создать виджеты для экрана 2
#     tk.Label(root, text="Экран 2").pack()
#     tk.Button(root, text="Назад", command=show_screen1).pack()
# Создание фреймов
frame1 = tk.Frame(root)
frame2 = tk.Frame(root)

# Виджеты для frame1
description_go_to_main_menu = tk.Label(frame1,
                                       text="Добро Пожаловать",
                                       font=("Arial", 16, "bold"),
                                       pady=80,
                                       height=5,
                                       anchor="s",
                                       )
description_go_to_main_menu.pack()
button_go_to_main_menu = (tk.Button(frame1,
                                   text="В главное меню",
                                   font=("Arial", 20, "bold"),
                                   command=lambda: show_frame(frame2)
                                   ))
button_go_to_main_menu.pack()
# tk.Button(frame1, text="В экран 2", command=lambda: show_frame(frame2)).pack()

# Виджеты для frame2
tk.Label(frame2, text="Экран 2").pack()
tk.Button(frame2, text="Назад", command=lambda: show_frame(frame1)).pack()

current_frame = None

def show_frame(frame):
    global current_frame
    if current_frame:
        current_frame.pack_forget()  # Скрыть текущий фрейм
    frame.pack(fill="both", expand=True)  # Показать новый
    current_frame = frame

# Запустить первый экран
show_frame(frame1)
# show_screen1()
root.mainloop()
