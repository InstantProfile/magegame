import Entity
import Match
import UI
import Handler


class CreateMenu:
    def __init__(self, game_state):
        self.game_state = game_state

    def create_custom_mage(self):
        name = input(UI.MainUI.input_name())
        mage = Entity.Person(name, 0, 5).set_action_person()
        self.game_state.append(mage)
        print(UI.MainUI.append_list_mage(mage.name_mage()))

    def create_random_mage(self):
        mage = Entity.Person('enemy', 0, 5).set_random_person()
        self.game_state.append(mage)
        print(UI.MainUI.append_list_mage(mage.name_mage()))

    @staticmethod
    def lists_mage_view(arr):
        for mage in arr:
            print(mage)

    def start_match(self):
        if len(self.game_state) >= 2:
            Match.StartFight(self.game_state).fight()
        else:
            print(UI.MainUI.not_enough_players())

    # @staticmethod
    def initialise_menu(self):
        menu_actions = {
            1: self.create_custom_mage,
            2: self.create_random_mage,
            3: self.lists_mage_view,
            4: self.start_match,
            5: UI.MainUI.quit_game
        }
        while True:
            choice = Handler.ChoiceHandler.get_user_choice(
                scenario="main_menu_choice",
                message=UI.MainUI.view_main_menu()
            )
            action = menu_actions.get(choice)
            if choice == 5:
                action()
                break
            elif choice == 3:
                action(self.game_state)
            else:
                action()


class Game:
    def __init__(self):
        self.mage_list = []

    @staticmethod
    def start_game():
        game_instance = Game()
        CreateMenu(game_instance.mage_list).initialise_menu()


if __name__ == "__main__":
    Game().start_game()
