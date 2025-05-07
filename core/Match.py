import random
from .scenarios import SCENARIOS


def mage_dead(mage):
    return mage.health <= 0


def players_selection(player, enemy, choices, mage_list, output_callback):
    if choices == 1:
        result = player.attack(enemy)
        output_callback(result)
        condition_result = condition_mage(enemy, mage_list, )
        output_callback(condition_result)

    elif choices == 2:
        result = player.mage_armor_plus()
        output_callback(result)
        player.step = player.INTERLOCK_STEP_COUNT
    elif choices == 3:
        result = player.health_recovery()
        output_callback(result)


def condition_mage(target, mage_list, ):
    """Проверка на отрицательное здоровье мага:"""
    if mage_dead(target):
        mage_list.remove(target)
        return f"{target.name} - Проиграл."
    return f"У {target.name} осталось {round(target.health, 2)} здоровья."


def update_step_mage(mage):
    """Обновление счетчика"""
    if mage.step > 0:
        mage.step -= 1
        if mage.step == 0:
            mage.mage_armor_minus()


class StartFight:
    def __init__(self, game_state, input_callback, output_callback):
        self.game_state = game_state
        self.input_callback = input_callback
        self.output_callback = output_callback

    def handler_user(self, user, enemy, mage_list):
        if user.step == 0:
            scenario = "game_menu_choice"
        else:
            scenario = "game_menu_no_defence"
        choice = self.input_callback(scenario)
        players_selection(user, enemy, choice, mage_list, self.output_callback)

    @staticmethod
    def get_bot_choice(scenario, scenarios=SCENARIOS):
        """Случайный выбор действия бота из доступных сценариев."""
        return random.choice(scenarios.get(scenario))

    def selection_bot(self, bot, enemy, mage_list, output_callback, scenarios=SCENARIOS):
        """Логика действий бота в зависимости от состояния."""
        # Выбор сценария:
        # - Если здоровье <50 и броня неактивна → полное меню
        # - Если здоровье <50 и броня активна → нельзя использовать защиту
        # - Если здоровье ≥50 → нельзя лечиться
        if bot.health < 50 and bot.step == 0:
            choices = StartFight.get_bot_choice("game_menu_choice", scenarios)
        elif bot.health < 50 and bot.step > 0:
            choices = StartFight.get_bot_choice("game_menu_no_defence", scenarios)
        elif bot.health >= 50 and bot.step == 0:
            choices = StartFight.get_bot_choice("game_menu_no_heal", scenarios)
        else:
            choices = StartFight.get_bot_choice("game_menu_only_attack", scenarios)

        players_selection(bot, enemy, choices, mage_list, self.output_callback)

    @staticmethod
    def preparation_for_battle(target):
        """ Обновление здоровья для новой игры с другим игроком"""
        if target.health < 100:
            target.health = target.BASE_HP
            target.step = 0

    def fight(self):
        user, bot = self.game_state[:2]
        StartFight.preparation_for_battle(user)
        StartFight.preparation_for_battle(bot)
        while not mage_dead(user) and not mage_dead(bot):
            # Пользователь
            self.handler_user(user, bot, self.game_state)
            if mage_dead(bot):
                break
            # Бот
            self.selection_bot(bot, user, self.game_state)
            if mage_dead(user):
                break
            update_step_mage(user)
            update_step_mage(bot)
