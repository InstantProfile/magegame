import tkinter as tk

# Создание главного окна
root = tk.Tk()
root.title("Мое первое приложение")
root.geometry("300x200")  # размер окна

# Запуск главного цикла
root.mainloop()


def button_click():
    label.config(text="Кнопка нажата!")


root = tk.Tk()
root.title("Пример с кнопкой")

# Метка
label = tk.Label(root, text="Привет, Tkinter!")
label.pack(pady=10)

# Кнопка
button = tk.Button(root, text="Нажми меня", command=button_click)
button.pack(pady=10)

root.mainloop()


def show_text():
    input_text = entry.get()
    label_result.config(text=f"Вы ввели: {input_text}")


root = tk.Tk()
root.title("Форма ввода")

# Поле ввода
entry = tk.Entry(root, width=30)
entry.pack(pady=10)

# Кнопка для подтверждения
btn_submit = tk.Button(root, text="Показать текст", command=show_text)
btn_submit.pack(pady=5)

# Метка для результата
label_result = tk.Label(root, text="")
label_result.pack(pady=10)

root.mainloop()

root = tk.Tk()
root.title("Grid Layout")

# Создание виджетов
label1 = tk.Label(root, text="Логин:")
label2 = tk.Label(root, text="Пароль:")
entry1 = tk.Entry(root)
entry2 = tk.Entry(root, show="*")
btn = tk.Button(root, text="Войти")

# Размещение с помощью grid
label1.grid(row=0, column=0, padx=5, pady=5, sticky="e")
label2.grid(row=1, column=0, padx=5, pady=5, sticky="e")
entry1.grid(row=0, column=1, padx=5, pady=5)
entry2.grid(row=1, column=1, padx=5, pady=5)
btn.grid(row=2, columnspan=2, pady=10)

root.mainloop()


import tkinter as tk

def update():
    selection = f"Выбрано: {var.get()}"
    label.config(text=selection)

root = tk.Tk()
var = tk.StringVar()

# Радиокнопки
tk.Radiobutton(root, text="Вариант 1", variable=var, value="A", command=update).pack()
tk.Radiobutton(root, text="Вариант 2", variable=var, value="B", command=update).pack()

# Checkbutton
check_var = tk.BooleanVar()
check = tk.Checkbutton(root, text="Согласен", variable=check_var)
check.pack(pady=10)

label = tk.Label(root, text="")
label.pack()

root.mainloop()