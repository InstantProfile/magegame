from project.magegame.core import Entity


def create_random_mage_tkinter():
    """Создание рандомного персонажа для GUI"""
    mage = Entity.Person("Enemy", 0, 5).set_random_stat()
    return mage