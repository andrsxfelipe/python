import tkinter as tk
from tkinter import messagebox
from datetime import datetime

dic = {'Book1': ["Author", "Genre", 1900, 1, 100.00]}

def newBook(newTit, newAu, newGen, newYear, newQuan, newPrice):
    dic[newTit] = [newAu, newGen, newYear, newQuan, newPrice]
    update_display()

def update_display():
    display.delete(1.0, tk.END)
    display.insert(tk.END, "-"*80 + "\n")
    for title, data in dic.items():
        line = f"Book: {title}, Author: {data[0]}, Genre: {data[1]}, Year: {data[2]}, Quantity: {data[3]}, Price: {data[4]}"
        display.insert(tk.END, line + "\n")
    display.insert(tk.END, "-"*80)

def submit():
    title = entry_title.get().strip()
    author = entry_author.get().strip()
    genre = entry_genre.get().strip()
    year = entry_year.get().strip()
    quantity = entry_quantity.get().strip()
    price = entry_price.get().strip()

    if not title or not author or not genre:
        messagebox.showerror("Error", "Título, autor y género son obligatorios.")
        return

    if not (year.isdigit() and 0 < int(year) < datetime.now().year):
        messagebox.showerror("Error", "Año inválido.")
        return

    if not (quantity.isdigit() and int(quantity) > 0):
        messagebox.showerror("Error", "Cantidad inválida.")
        return

    try:
        price_val = float(price)
        if price_val <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Error", "Precio inválido.")
        return

    newBook(title, author, genre, int(year), int(quantity), price_val)

# Crear ventana
root = tk.Tk()
root.title("Gestor de Libros")

# Campos de entrada
tk.Label(root, text="Título").grid(row=0, column=0)
entry_title = tk.Entry(root)
entry_title.grid(row=0, column=1)

tk.Label(root, text="Autor").grid(row=1, column=0)
entry_author = tk.Entry(root)
entry_author.grid(row=1, column=1)

tk.Label(root, text="Género").grid(row=2, column=0)
entry_genre = tk.Entry(root)
entry_genre.grid(row=2, column=1)

tk.Label(root, text="Año").grid(row=3, column=0)
entry_year = tk.Entry(root)
entry_year.grid(row=3, column=1)

tk.Label(root, text="Cantidad").grid(row=4, column=0)
entry_quantity = tk.Entry(root)
entry_quantity.grid(row=4, column=1)

tk.Label(root, text="Precio").grid(row=5, column=0)
entry_price = tk.Entry(root)
entry_price.grid(row=5, column=1)

# Botón
submit_btn = tk.Button(root, text="Agregar Libro", command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, pady=10)

# Área de visualización
display = tk.Text(root, height=10, width=80)
display.grid(row=7, column=0, columnspan=2)

# Inicializa vista
update_display()

root.mainloop()
