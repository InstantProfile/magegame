from .Adapters import show_message, get_input

SCENARIOS = {
    "main_menu_choice": [1, 2, 3, 4, 5],
    "game_menu_choice": [1, 2, 3],
    "game_menu_no_defence": [1, 3],
    "game_menu_no_heal": [1, 2],
    "game_menu_only_attack": [1],
}


def _get_number_input(*args):
    """Получение числа (для других методов)"""
    while True:
        try:
            return int(get_input(*args))
        except ValueError:
            show_message("Ошибка: введите число.")


def get_user_choice(scenario, message=""):
    """Обработка ввода пользователя с проверкой на число"""
    options = SCENARIOS.get(scenario, [])
    value = ' '.join(str(SCENARIOS.get(scenario)).replace('[', '').replace(']', '').split(', '))
    while True:
        number = _get_number_input(message)
        if number in options:
            return number
        show_message(f"Некорректный выбор. Допустимые варианты: {value}")


def get_positive_number(*args):
    """Обработка ввода пользователя с проверкой на положительное число"""
    while True:
        number = _get_number_input(*args)
        if number >= 0:
            return number
        show_message(f"Ошибка: число должно быть положительным")
