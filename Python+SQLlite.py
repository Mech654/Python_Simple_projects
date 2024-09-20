import sqlite3
import random

connectToDBFile = sqlite3.connect('FruitManager.db')

cursor = connectToDBFile.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS orders (
        order_id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer_name TEXT NOT NULL,
        ordered_fruit TEXT NOT NULL,
        quantity INTEGER NOT NULL
    )
''')

listofnames = ('Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Oliver', 'Hannah', 'Frank')
fruits = ["Apple", "Banana", "Cherry", "Date", "Elderberry", "Fig", "Grape", "Honeydew"]

x = 0
while (x < 100):
    x += 1
    randName = random.randint(0, len(listofnames) - 1)
    getName = listofnames[randName]
    randFruit = random.randint(0, len(fruits) - 1)
    getFruit = fruits[randFruit]
    randAmount = random.randint(1, 10)
    cursor.execute("INSERT INTO orders (customer_name, ordered_fruit, quantity) VALUES (?, ?, ?)", (getName, getFruit, randAmount))

connectToDBFile.commit()
connectToDBFile.close()
