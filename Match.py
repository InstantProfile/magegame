import random
import Handler
import UI


class BotAIController:
    @staticmethod
    def get_bot_choice(scenario):
        """Возвращает выбор бота для разных ситуаций
        """
        options: dict = Handler.ChoiceHandler.SCENARIOS
        return random.choice(options.get(scenario))

    @staticmethod
    def handle_bot(bot, enemy, mage_list):
        if bot.magician_health < 50 and bot.step_mage == 0:
            choices = BotAIController.get_bot_choice(scenario="game_menu_choice")
        elif bot.magician_health < 50 and bot.step_mage > 0:
            choices = BotAIController.get_bot_choice(scenario="game_menu_no_defence")
        elif bot.magician_health >= 50 and bot.step_mage == 0:
            choices = BotAIController.get_bot_choice(scenario="game_menu_no_heal")
        else:
            choices = BotAIController.get_bot_choice(scenario="game_menu_only_attack")

        if choices == 1:
            bot.attack(enemy)
            BattleManager.condition_mage(enemy, mage_list)
        elif choices == 2:
            bot.mage_armor_plus()
            bot.step_mage = bot.interlock_step_count()
        elif choices == 3:
            bot.health_recovery()


class BattleManager:

    @staticmethod
    def get_choice_mage_interlock_armor():
        Handler.ChoiceHandler.get_user_choice(scenario="no_armor", message=UI.BattleUI.view_get_no_armor())

    @staticmethod
    def mage_dead(mage):
        return mage.magician_health <= 0

    @staticmethod
    def condition_mage(target, mage_list):
        """Проверка на отрицательное здоровье мага:"""
        if BattleManager.mage_dead(target):
            mage_list.remove(target)
            print(UI.BattleUI.view_condition_mage(target, first=True))
            return True
        print(UI.BattleUI.view_condition_mage(target, second=True))
        return False

    @staticmethod
    def update_step_mage(mage):
        """Обновление счетчика"""
        if mage.step_mage_armor() > 0:
            mage.step_mage -= 1
            if mage.step_mage_armor() == 0:
                mage.mage_armor_minus()


class StartFight:
    def __init__(self, game_state):
        self.game_state = game_state

    @staticmethod
    def handle_user(user, enemy, mage_list):
        if user.step_mage_armor() == 0:
            choices = (Handler.ChoiceHandler.get_user_choice(
                scenario="game_menu_choice",
                message=UI.BattleUI.view_get_choice_mage()))
            if choices == 1:
                user.attack(enemy)
                BattleManager.condition_mage(enemy, mage_list)
            elif choices == 2:
                user.mage_armor_plus()
                user.step_mage = user.interlock_step_count()
            elif choices == 3:
                user.health_recovery()
        else:
            choices = Handler.ChoiceHandler.get_user_choice(
                scenario="game_menu_no_defence",
                message=UI.BattleUI.view_get_no_armor())
            if choices == 1:
                user.attack(enemy)
                BattleManager.condition_mage(enemy, mage_list)
            elif choices == 3:
                user.health_recovery()

    @staticmethod
    def condition_start_game(target):
        """ Обновление здоровья для новой игры с другим игроком"""
        if target.magician_health < 100:
            target.magician_health = 100

    def fight(self):
        user, bot = self.game_state[:2]
        StartFight.condition_start_game(user)
        StartFight.condition_start_game(bot)
        while not BattleManager.mage_dead(user) and not BattleManager.mage_dead(bot):
            # Пользователь
            StartFight.handle_user(user, bot, self.game_state)
            if BattleManager.mage_dead(bot):
                break
            # Бот
            BotAIController.handle_bot(bot, user, self.game_state)
            if BattleManager.mage_dead(user):
                break

            BattleManager.update_step_mage(user)
            BattleManager.update_step_mage(bot)
