rom project.magegame.core import Match, Entity


def show_message(text):
    tk.messagebox.showinfo("Информация", text)


# В PracticTkinter.py
def on_attack_click():
    result = Entity.attack(enemy)
    show_message(result)
    update_health_bars()  # обновление интерфейса
