# Импорты:
import sqlite3
import tkinter as tk
from tkinter import Button
from tkinter import Text
from tkinter import PhotoImage

# Создаем базу данных:
connect = sqlite3.connect('Anecdotes.db')
cursor = connect.cursor()

# Создаем таблицу Jokes:
cursor.execute('''CREATE TABLE IF NOT EXISTS Jokes(
    id INT PRIMARY KEY,
    joke TEXT NOT NULL);
''')
connect.commit()

# Наполняем таблицу Jokes:
jokes = [('1', 'Есть такая категория соседей: перфорасты'),
         ('2', 'Муж на час" подал на развод через 39 минут.'),
         ('3', 'Eсли в лeсу вы встрeтили мeдвeдя, клeщeй ужe нe стoит бoяться.'),
         ('4', 'Можно ли желать сладких снов диабетикам?'),
         ('5', 'На директора Автоваза решили завезти уголовное дело. Но оно не завелось.')]
cursor.executemany('INSERT INTO Jokes VALUES(?, ?);', jokes)
connect.commit()

# Создаем графическое окно, используя Tkinter:
joke = tk.Tk()
joke.title('Joke')
joke.geometry('1000x500')
joke.protocol('WM_DELETE_WINDOW', joke.quit)

# Изображение, для кнопки:
image = PhotoImage(file="refresh.png")

# Функция, для генерации рандомного анекдота:
def get_random_anecdote():
    cursor.execute('SELECT joke FROM Jokes ORDER BY RANDOM() LIMIT 1;')
    anecdote = cursor.fetchone()[0]
    return anecdote

# Функция для комфортного визуализирования анекдота:
def show_random_anecdote():
    anecdote = get_random_anecdote()
    text.delete(0.0, tk.END)
    text.insert(0.0, anecdote)

# Кнопка (Button):
button = Button(joke, image=image, command=show_random_anecdote)
button.pack()

# Текст (Text):
text = Text(wrap='word')
text.pack()

# Бесконечный цикл окна приложения:
joke.mainloop()