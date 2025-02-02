import tkinter as tk
from tkinter import messagebox

# Основные переменные
kol = 0
vsego = 3

# Создание основного окна
root = tk.Tk()
root.title("Тест для школы")

# Вопрос 1
question1_label = tk.Label(root, text="История. В каком году закончилась Великая Отечественная война?")
question1_label.pack(pady=10)

entry1 = tk.Entry(root, width=30)
entry1.pack(pady=10)

# Вопрос 2
question2_label = tk.Label(root, text="Геометрия. Как называется треугольник у которого все стороны равны?")
question2_label.pack(pady=10)

entry2 = tk.Entry(root, width=30)
entry2.pack(pady=10)

# Вопрос 3
question3_label = tk.Label(root, text="Биология. Как называется процесс синтеза углеводов из неорганических веществ за счёт энергии солнца?")
question3_label.pack(pady=10)

entry3 = tk.Entry(root, width=30)
entry3.pack(pady=10)

# Кнопка для проверки ответов
def check_answers():
    global kol
    # Проверка первого вопроса
    if entry1.get().strip() == "1945":
        kol += 1
    # Проверка второго вопроса
    if entry2.get().strip().lower() == "равносторонний":
        kol += 1
    # Проверка третьего вопроса
    if entry3.get().strip().lower() == "фотосинтез":
        kol += 1
    # Показ результатов
    messagebox.showinfo("Результат", f"{kol} верных ответов из {vsego}")
    root.quit()

submit_button = tk.Button(root, text="Проверить ответы", command=check_answers)
submit_button.pack(pady=20)

# Запуск основного цикла
root.mainloop()