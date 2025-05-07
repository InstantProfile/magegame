from ..core import Match
from ..console import Handler
from ..console import Adapters


class CreateMenu:
    """Главное меню игры."""

    def __init__(self, game_state):
        self.game_state = game_state

    def return_mage_list(self):
        return self.game_state

    @staticmethod
    def show_mage_list(arr) -> str:
        """Возвращает строку с информацией о персонажах. Универсальна для консоли и GUI."""
        if not arr:
            return "Список персонажей пуст."
        return "\n".join([f"name: {mage.name}, "
                          f"health: {mage.health}, "
                          f"damage: {mage.damage}, "
                          f"armor: {mage.armor}" for mage in arr])

    def start_match(self):
        if len(self.game_state) >= 2:
            input_callback = lambda scenario: Handler.get_user_choice(
                scenario,
                message=Adapters.view_get_choice_mage())
            output_callback = lambda msg: print(msg)
            Match.StartFight(self.game_state, input_callback, output_callback).fight()

        else:
            Adapters.show_message(Adapters.not_enough_players())

    @staticmethod
    def quit_game():
        Adapters.show_message(Adapters.quit_game())
        exit()

    def initialise_menu_console(self):
        menu_actions = {
            1: lambda: self.game_state.append(Adapters.set_custom_stats()),
            2: lambda: self.game_state.append(Adapters.create_random_mage()),
            3: lambda: Adapters.show_message(self.show_mage_list(self.game_state)),
            4: self.start_match,
            5: self.quit_game
        }
        while True:
            selection = Handler.get_user_choice(
                scenario="main_menu_choice",
                message=Adapters.view_main_menu()
            )
            action = menu_actions.get(selection)
            action()


class Game:
    def __init__(self):
        self.mage_list = []

    @staticmethod
    def start_game():
        game_instance = Game()
        CreateMenu(game_instance.mage_list).initialise_menu_console()
