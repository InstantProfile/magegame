from console.MainMenu import Game

if __name__ == "__main__":
    choice = input("Запустить консоль (C) или GUI (G)? ").upper()
    if choice == "G":
        from gui.run import start_tkinter

        start_tkinter()
    else:
        Game().start_game()
