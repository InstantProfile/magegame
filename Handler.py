class ChoiceHandler:
    SCENARIOS = {
        "main_menu_choice": [1, 2, 3, 4, 5],
        "game_menu_choice": [1, 2, 3],
        "game_menu_no_defence": [1, 3],
        "game_menu_no_heal": [1, 2],
        "game_menu_only_attack": [1],
    }

    @staticmethod
    def _get_number_input(message):
        """Получение числа (для других методов)"""
        while True:
            try:
                return int(input(message))
            except ValueError:
                print("Ошибка: введите число.")

    @staticmethod
    def get_user_choice(scenario, message):
        """Обработка ввода пользователя с проверкой на число"""
        options = ChoiceHandler.SCENARIOS.get(scenario, [])
        value = ' '.join(str(ChoiceHandler.
                             SCENARIOS.
                             get(scenario)).
                         replace('[', '').
                         replace(']', '').
                         split(', '))
        while True:
            number = ChoiceHandler._get_number_input(message)
            if number in options:
                return number
            print(f"Некорректный выбор. Допустимые варианты: {value}")

    @staticmethod
    def get_positive_number(message):
        """Обработка ввода пользователя с проверкой на положительное число"""
        while True:
            number = ChoiceHandler._get_number_input(message)
            if number >= 0:
                return number
            print(f"Ошибка: число должно быть положительным")
