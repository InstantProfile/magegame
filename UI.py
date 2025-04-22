class MainUI:
    @staticmethod
    def view_main_menu():
        """Вывод главного меню ."""
        return (
            "1 - Добавить в ручную игрока.\n"
            "2 - Добавить рандомно игрока.\n"
            "3 - Список игроков.\n"
            "4 - Начать игру.\n"
            "5 - Выход\n"
            "Ваш выбор: ")

    @staticmethod
    def input_name():
        return "Введите имя: "

    @staticmethod
    def append_list_mage(mage):
        return f"{mage} добавлен."

    @staticmethod
    def not_enough_players():
        return "Недостаточно игроков"

    @staticmethod
    def quit_game():
        return "Выход"


class EntityUI:
    @staticmethod
    def print_set_action_person(point, warning=False):
        first = f"У вас {point} очков характеристик"
        second = "+2 к урону или +0.1 к броне"
        if warning:
            return f"Используйте положительные числа и ровно {point} очков!"
        return first, second


class BattleUI:
    @staticmethod
    # Шаблон сообщения об атаке
    def view_attacks(*args):
        return "{} нанес {} урона {}".format(*args)

    @staticmethod
    def view_heal(mage, health=0, ):
        view_console = (
            f"{mage.name_mage()} восстановил {health} здоровья.\n"
            f"Теперь у {mage.name_mage()} {mage.magician_health} здоровья.")
        return view_console

    @staticmethod
    def view_armor_plus(defender):
        return f"{defender.name_mage()} увеличил броню в 2 раза. Теперь броня: {defender.magician_armor}"

    @staticmethod
    def view_armor_minus(defender):
        return f"{defender.name_mage()} вернулась в исходное состояние. Теперь броня: {defender.magician_armor}"

    @staticmethod
    def view_get_choice_mage():
        return "Выберите действие:\n1 - Атака.\n2 - Защита.\n3 - Лечение: "

    @staticmethod
    def view_get_no_armor():
        return "Выберите действие:\n1 - Атака.\n3 - Лечение: "

    @staticmethod
    def view_condition_mage(mage, first=False, second=False):
        if first:
            return f"{mage.name_mage()} - Проиграл."
        if second:
            return f"У {mage.name_mage()} осталось {round(mage.magician_health, 2)} здоровья."
