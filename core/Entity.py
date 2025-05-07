import random


class Person:
    # Базовые характеристики персонажа
    BASE_HP = 100
    BASE_DAMAGE = 12
    BASE_ARMOR = 0.1
    CONSTANT_DAMAGE = 2
    CONSTANT_ARMOR = 0.1
    HEALTH_AMOUNT = 7.5
    MAX_ARMOR = 0.9
    MIN_ARMOR = 0.1
    INTERLOCK_STEP_COUNT = 4

    def __init__(self, name: str, step: int, point: int):
        """
        - name: Имя
        - step: Счетчик блокировки умений
        - point: Очки для распределения характеристик
        """
        self._name = name
        self._health = self.BASE_HP
        self._damage = self.BASE_DAMAGE
        self._armor = self.BASE_ARMOR
        self._step = step  # Счетчик блокировки умений
        self._point = point  # Очки для распределения

    def __str__(self):
        return (f"name: {self._name}, "
                f"health: {self._health}, "
                f"damage: {self._damage}, "
                f"armor: {self._armor}, "
                f"count: {self._step} ")

    @property
    def name(self):
        return self._name

    @property
    def health(self) -> float:
        return round(self._health, 2)

    @health.setter
    def health(self, value):
        self._health = max(0, value)

    @property
    def damage(self):
        return self._damage

    @damage.setter
    def damage(self, value):
        self._damage = value

    @property
    def armor(self):
        return round(self._armor, 2)

    @armor.setter
    def armor(self, value):
        self._armor = max(self.MIN_ARMOR, min(value, self.MAX_ARMOR))

    # if not (self.MIN_ARMOR <= value <= self.MAX_ARMOR):
    #     raise ValueError("Броня за пределами границ")
    # self._armor = value
    @property
    def step(self):
        return self._step

    @step.setter
    def step(self, value):
        self._step = max(0, value)

    @property
    def point(self):
        return self._point

    def __dict_list_mage(self, damage_points, armor_points):
        self.damage += damage_points * self.CONSTANT_DAMAGE
        self.armor += armor_points * self.CONSTANT_ARMOR
        return self

    def set_stats(self, damage_points: int, armor_points: int):
        """Установка характеристик. Возвращает сообщение об ошибке или None."""
        if damage_points < 0 or armor_points < 0:
            return "Ошибка: значения не могут быть отрицательными!"
        if damage_points + armor_points != self._point:
            return f"Используйте ровно {self._point} очков!"
        if damage_points + armor_points == self._point:
            self.__dict_list_mage(damage_points, armor_points)
        return None

    def get_stats(self):
        return {
            "name": self.name,
            "health": self.health,
            "damage": self.damage,
            "armor": self.armor,
        }

    def set_random_stat(self):
        damage = random.randint(0, self._point)
        armor = self._point - damage
        return self.__dict_list_mage(damage, armor)

    def attack(self, enemy):
        """Атака персонажа"""
        damage = max(round(self.damage - self.damage * enemy.armor, 2), 0)
        enemy.health -= damage
        return f"{self.name} нанес {damage} урона {enemy.name}"

    def health_recovery(self):
        """Восстановление здоровья"""
        self.health = min(round(self.health + self.HEALTH_AMOUNT, 2), self.BASE_HP)
        return (f"{self.name} восстановил {self.HEALTH_AMOUNT} здоровья.\n"
                f"Теперь у {self.name} {self.health} здоровья.")

    def mage_armor_plus(self):
        """Увеличение брони"""
        self.armor = self.armor * 2
        return f"{self.name} увеличил броню в 2 раза. Теперь броня: {self.armor}"

    def mage_armor_minus(self):
        """Возвращение брони в исходное состояние"""
        self.armor = self.armor / 2
        return f"{self.name} вернулась в исходное состояние. Теперь броня: {self.armor}"
