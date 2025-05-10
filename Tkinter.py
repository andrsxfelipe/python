#Importar
import tkinter as tk
from tkinter import messagebox #Para las advertencias

#Crear ventana principal
root = tk.Tk() 
root.title("Mi App") #El nombre que aparecera en la parte izq superior
root.mainloop() # Sin esa línea, la ventana aparecería por una fracción de segundo y se cerraría de inmediato.

#Widgets
label = tk.Label(root, text="Hola") #Texto en la interfaz
entry = tk.Entry(root) #Campo para escribir
button = tk.Button(root, text="Haz clic", command=mi_funcion) #Botón con la acción mi_función
text = tk.Text(root) #Caja de texto más grande, para contenido largo

#Organización con grid
label.grid(row=0, column=0)
entry.grid(row=0, column=1)

#Validación básica
if not entry.get():
    messagebox.showerror("Error", "Campo vacío") #Muestra un mensaje

#Area de visualización
text_area = tk.Text(root, height=10, width=40)
text_area.grid(row=7, column=0, columnspan=2) #En la columna 7, en la columna 0 y ocupa 2 columnas
text_area.insert(tk.END, "Texto inicial")
text_area.delete(1.0, tk.END)  # Borra todo
