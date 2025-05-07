from ..core import Entity
from ..console import Handler


def show_message(text):
    print(text)


def get_input(prompt):
    return input(prompt)


def set_custom_stats():
    name = get_input("Введите имя: ")
    mage = Entity.Person(name, 0, 5)

    # Запрос характеристик
    while True:
        show_message(print_set_custom_person(mage.point))
        damage = Handler.get_positive_number("Урон: ")
        armor = Handler.get_positive_number("Броня: ")
        if damage >= 0 and armor >= 0 and damage + armor == mage.point:
            mage.set_stats(damage, armor)
            print(f"{mage.name} Добавлен")
            return mage  # Возвращаем созданного персонажа
        show_message(print_set_custom_person(mage.point, warning=True))


def create_random_mage():
    mage = Entity.Person('enemy', 0, 5).set_random_stat()
    append_list_mage(mage.name)
    return mage


def quit_game():
    return "Выход"


def view_main_menu():
    """Вывод главного меню."""
    return (
        "1 - Добавить в ручную игрока.\n"
        "2 - Добавить рандомно игрока.\n"
        "3 - Список игроков.\n"
        "4 - Начать игру.\n"
        "5 - Выход\n"
        "Ваш выбор: ")


def append_list_mage(mage):
    show_message(f"{mage} добавлен.")


def not_enough_players():
    return "Недостаточно игроков"


def print_set_custom_person(point, warning=False):
    if warning:
        return f"Используйте положительные числа и ровно {point} очков!"
    else:
        return f"У вас {point} очков характеристик\n+2 к урону или +0.1 к броне"


def view_attacks(*args):
    return "{} нанес {} урона {}".format(*args)


def view_heal(mage, health=0, ):
    view_console = (
        f"{mage.name} восстановил {health} здоровья.\n"
        f"Теперь у {mage.name} {mage.health} здоровья.")
    return view_console


def view_armor_plus(defender):
    return f"{defender.name} увеличил броню в 2 раза. Теперь броня: {defender.armor}"


def view_armor_minus(defender):
    return f"{defender.name} вернулась в исходное состояние. Теперь броня: {defender.armor}"


def view_get_choice_mage():
    return "Выберите действие:\n1 - Атака.\n2 - Защита.\n3 - Лечение: "


def view_get_no_armor():
    return "Выберите действие:\n1 - Атака.\n3 - Лечение: "


def view_condition_mage(mage, first=False, second=False):
    if first:
        return f"{mage.name} - Проиграл."
    if second:
        return f"У {mage.name} осталось {round(mage.health, 2)} здоровья."
