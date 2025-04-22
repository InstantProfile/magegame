import random
import UI
import Handler


class Person:
    # Базовые статы персонажа
    __BASE_HP = 100
    __BASE_DAMAGE = 12
    __BASE_ARMOR = 0.1
    __CONSTANT_DAMAGE = 2  # +2 урона за очко
    __CONSTANT_ARMOR = 0.1  # +0.1 брони за очко
    __HEALTH = 7.5  # Восстановление здоровья за лечение
    __MAX_ARMOR = 0.9  # Максимальная броня
    __MIN_ARMOR = 0.1  # Минимальная броня
    __INTERLOCK_STEP_COUNT = 4  # Длительность блокировки умения

    def __init__(self, name: str, step: int, point: int):
        """
        Инициализация:
        - name: Имя
        - step: Счетчик блокировки умений
        - point: Очки для распределения характеристик
        """
        # Инициализация персонажа: имя, здоровье, урон, броня, счетчик шагов, очки улучшений
        self.__name = name
        self.__health = self.__BASE_HP
        self.__damage = self.__BASE_DAMAGE
        self.__armor = self.__BASE_ARMOR
        self._step = step  # Счетчик блокировки умений
        self._point = point  # Очки для распределения

    def __str__(self):
        return (f"name: {self.__name}, "
                f"health: {self.__health}, "
                f"damage: {self.__damage}, "
                f"armor: {self.__armor}, "
                f"count: {self._step} ")

    def name_mage(self):
        return self.__name

    def health(self):
        return self.__HEALTH

    def max_armor(self):
        return self.__MAX_ARMOR

    def min_armor(self):
        return self.__MIN_ARMOR

    def interlock_step_count(self):
        return self.__INTERLOCK_STEP_COUNT

    @property
    def magician_damage(self):
        return self.__damage

    @magician_damage.setter
    def magician_damage(self, value):
        self.__damage = value

    @property
    def magician_health(self):
        return self.__health

    @magician_health.setter
    def magician_health(self, value):
        self.__health = value

    @property
    def magician_armor(self):
        return self.__armor

    @magician_armor.setter
    def magician_armor(self, value):
        self.__armor = value

    @property
    def step_mage(self):
        return self._step

    @step_mage.setter
    def step_mage(self, value):
        self._step = value

    def get_base_hp(self):
        return self.__BASE_HP

    def __return_point(self):
        return self._point

    def __dict_list_mage(self, damage_points, armor_points):
        self.magician_damage = self.magician_damage + damage_points * self.__CONSTANT_DAMAGE
        self.magician_armor = round(float(self.magician_armor + armor_points * self.__CONSTANT_ARMOR), 2)
        return self

    def set_action_person(self):
        while True:
            UI.EntityUI.print_set_action_person(self.__return_point())
            damage = Handler.ChoiceHandler.get_positive_number("Урон: ")
            armor = Handler.ChoiceHandler.get_positive_number("Броня: ")
            if damage >= 0 and armor >= 0 and damage + armor == self.__return_point():
                return self.__dict_list_mage(damage, armor)
            UI.EntityUI.print_set_action_person(self.__return_point(), warning=True)

    def set_random_person(self):
        damage = random.randint(0, self._point)
        armor = self._point - damage
        return self.__dict_list_mage(damage, armor)

    def attack(self, enemy):
        """Атака персонажа"""
        damage = max(round(self.magician_damage - self.magician_damage * enemy.magician_armor, 2), 0)
        enemy.magician_health -= damage
        print(UI.BattleUI.view_attacks(enemy.name_mage(), damage, enemy.name_mage()))

    def health_recovery(self):
        """Восстановление здоровья"""
        self.magician_health = min(round(self.magician_health + self.health(), 2), self.get_base_hp())
        print(UI.BattleUI.view_heal(self, health=self.health()))

    def mage_armor_plus(self):
        """Увеличение брони"""
        self.magician_armor = min(round(self.magician_armor * 2, 2), self.max_armor())
        print(UI.BattleUI.view_armor_plus(self))

    def mage_armor_minus(self):
        """Возвращение брони в исходное состояние"""
        self.magician_armor = max(round(self.magician_armor, 2) / 2, self.min_armor())
        UI.BattleUI.view_armor_minus(self)

    def step_mage_armor(self):
        """Возвращение счетчика блокировки умения"""
        return self.step_mage
