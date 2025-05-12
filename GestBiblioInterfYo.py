import tkinter as tk
from tkinter import messagebox #Para las advertencias
from datetime import datetime

#dic={'Book1':["Author","Genre",1900,1,100.00]}
dic = {
    "Cien Años de Soledad": ["Gabriel", "Comedia", 1967, 3, 120.00],
    "1984": ["George", "Comedia", 1949, 5, 85.50],
    "El Principito": ["Antoine de Saint-Exupéry", "Ficcion", 1943, 4, 60.00],
    "El Amor en los Tiempos del Cólera": ["Gabriel", "Ficcion", 1985, 2, 130.00],  # Mismo autor
    "Rebelión en la Granja": ["George", "Romance", 1945, 3, 75.00],  # Mismo autor
    "La Sombra del Viento": ["Carlos Ruiz Zafón", "Drama", 2001, 6, 95.00]
}


def actualizarInfo():
    display.delete(1.0, tk.END)
    for book,info in dic.items():
        linea=(
        f"Libro: {book}, Autor: {info[0]}, Género: {info[1]}, Año de publicación: {info[2]}, "
        f"Cantidad: {info[3]}, Precio de reposición: {info[4]} \n"
        "------------------------------------------------------\n"
        )
        display.insert(tk.END,linea)


def newBook():
    titulo = libroEntry.get().strip().title()
    autor = autorEntry.get().strip().title()
    genero = generoEntry.get().strip().title()
    year = anioEntry.get().strip()
    cant = cantEntry.get().strip()
    precio = precioEntry.get().strip()

    if not titulo or not autor or not genero:
        messagebox.showerror("Error", "Todos los campos son obligatorios")
        return
    if not (year.strip('-').isdigit() and int(year)<datetime.now().year):
        messagebox.showerror("Error","Ingresa un año válido")
        return
    if not (cant.isdigit()):
        messagebox.showerror("Error","Ingresa una cantidad válida")
        return
    if not (precio.replace(".","",1).isdigit()):
        messagebox.showerror("Error","Ingresa un precio válido")
        return
    
    dic[titulo]=[autor,genero,int(year),int(cant),float(precio)]
    actualizarInfo()

def searchBook():
    titulo2 = libroEntry.get().strip().title()
    autor2 = autorEntry.get().strip().title()
    if not titulo2 and not autor2:
        messagebox.showerror("Error","Ingresa un título o un autor")
        return
    if titulo2:
        if titulo2 in dic.keys():
            lis=f"Autor: {dic[titulo2][0]}, Genero: {dic[titulo2][1]}, Año de publicación: {dic[titulo2][2]}, Cantidad: {dic[titulo2][3]}, Precio de reposición: {dic[titulo2][4]}"
            display.delete(1.0, tk.END)
            display.insert(tk.END, lis)
        else:
            messagebox.showerror("Error","Libro no encontrado. ¿Desea registrarlo?")
            return
    else:
        authors=list(filter(lambda x:x[1][0]==autor2, dic.items()))
        if not authors:
            messagebox.showerror("Error","No hay libros con estos autores")
            return
        else:
            display.delete(1.0, tk.END)
            for book2,info2 in authors:
                line=(
                f"Libro: {book2}, Autor: {info2[0]}, Género: {info2[1]}, Año de publicación: {info2[2]}, "
                f"Cantidad: {info2[3]}, Precio de reposición: {info2[4]} \n"
                )
                display.insert(tk.END,line)

def modificarCant_Precio():
    titulo3 = libroEntry.get().strip().title()
    cant3 = cantEntry.get().strip()
    precio3 = precioEntry.get().strip()
    if not titulo3:
        messagebox.showerror("Error", "Todos los campos son obligatorios")
        return
    if not (cant3.isdigit()):
        messagebox.showerror("Error","Ingresa una cantidad válida")
        return
    if not (precio3.replace(".","",1).isdigit()):
        messagebox.showerror("Error","Ingresa un precio válido")
        return
    if not titulo3 in dic.keys():
        messagebox.showerror("Error", "Libro no encontrado")
        return
    else:
        dic[titulo3][3]=cant3
        dic[titulo3][4]=precio3
        actualizarInfo()

def eliminarTitulo():
    titulo4 = libroEntry.get().strip().title()
    if not titulo4:
        messagebox.showerror("Error", "Porfavor, introduce el libro que quieres eliminar")
        return
    if not titulo4 in dic.keys():
        messagebox.showerror("Error", "Libro no encontrado")
        return
    else:
        del dic[titulo4]
        actualizarInfo()

def generarReporte():
    totalValue=sum(map(lambda x: x[-1]*x[-2], dic.values()))
    antiguos={}
    recientes={}
    for libro5,info5 in dic.items():
        if not info5[1] in antiguos.keys():
            antiguos[info5[1]]=[libro5] + info5[:1] + info5[2:] #Libro,Autor,Año
        else:
            if antiguos[info5[1]][2]>info5[2]:
                antiguos[info5[1]]=[libro5] + info5[:1] + info5[2:]
        if not info5[1] in recientes.keys():
            recientes[info5[1]]=[libro5] + info5[:1] + info5[2:] #Libro,Autor,Año
        else:
            if recientes[info5[1]][2]<info5[2]:
                recientes[info5[1]]=[libro5] + info5[:1] + info5[2:]
    display.delete(1.0, tk.END)
    display.insert(tk.END,"Libros más antiguos por género:\n")
    for genAn,infAn in antiguos.items():
        lAnt=(
        f"{genAn}: Libro: {infAn[0]}, Autor: {infAn[1]}, Año de publicación: {infAn[2]}, "
        f"Cantidad: {infAn[3]}, Precio de reposición: {infAn[4]} \n"
        )
        display.insert(tk.END,lAnt)
    display.insert(tk.END,"--------------------------------------\n")
    display.insert(tk.END,"Libros más recientes por género:\n")
    for genRe,infRe in recientes.items():
        lAnt=(
        f"{genRe}: Libro: {infRe[0]}, Autor: {infRe[1]}, Año de publicación: {infRe[2]}, "
        f"Cantidad: {infRe[3]}, Precio de reposición: {infRe[4]} \n"
        )
        display.insert(tk.END,lAnt)

root = tk.Tk() 
root.title("Gestor Biblioteca") #El nombre que aparecera en la parte izq superior

libroLabel = tk.Label(root, text="Libro:") #Texto en la interfaz
libroLabel.grid(row=0,column=1)
libroEntry = tk.Entry(root) #Campo para escribir
libroEntry.grid(row=0,column=2)

autorLabel = tk.Label(root, text="Autor:") #Texto en la interfaz
autorLabel.grid(row=1,column=1)
autorEntry = tk.Entry(root) #Campo para escribir
autorEntry.grid(row=1,column=2)

generoLabel= tk.Label(root,text="Genero:")
generoLabel.grid(row=2,column=1)
generoEntry= tk.Entry(root)
generoEntry.grid(row=2,column=2)

anioLabel = tk.Label(root, text="Año de publicación:")
anioLabel.grid(row=3,column=1)
anioEntry = tk.Entry(root)
anioEntry.grid(row=3,column=2)

cantLabel = tk.Label(root,text="Cantidad del libro:")
cantLabel.grid(row=4,column=1)
cantEntry = tk.Entry(root)
cantEntry.grid(row=4,column=2)

precioLabel = tk.Label(root,text="Precio de reposición:")
precioLabel.grid(row=5,column=1)
precioEntry = tk.Entry(root)
precioEntry.grid(row=5,column=2)

addButton = tk.Button(root,text="Añadir libro", anchor="center",command=newBook)
addButton.grid(row=6,column=0)

buscarButton = tk.Button(root,text="Buscar libro", anchor="center",command=searchBook)
buscarButton.grid(row=6,column=1)

nuevaInfoButton = tk.Button(root,text="Actualizar info del libro", anchor="center",command=modificarCant_Precio)
nuevaInfoButton.grid(row=6,column=2)

eliminarButton = tk.Button(root,text="Eliminar libro", anchor="center",command=eliminarTitulo)
eliminarButton.grid(row=6,column=3)

reportButton = tk.Button(root,text="Generar Reporte", anchor="center",command=generarReporte)
reportButton.grid(row=6,column=4)

display = tk.Text(root, height=20, width=140)
display.grid(row=7, column=0, columnspan=5)



actualizarInfo()
root.mainloop()