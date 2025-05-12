from datetime import datetime
dic={'Book1':["Author","Genre",1900,1,100.00]}
def newBook(newTit:str,newAu:str,newGen:str,newYear:int,newQuan:int,newPrice:float):
    dic[newTit]=[newAu,newGen,newYear,newQuan,newPrice]
def showDict():
    l=[f"Book: {x[0]}, Author: {x[1][0]}, Genre: {x[1][1]}, Year of publication: {x[1][2]}, Quantity:{x[1][3]}, Price:{x[1][4]}" for x in dic.items()]
    print('-'*80)
    print('\n'.join(l))
    print('-'*80)
def OptionSelected(option):
    if option ==1:
        title1=input("Ingrese el nombre del libro: ")
        author1=input("Ingrese el autor del libro: ")
        genre1=input("Ingrese el género del libro: ")
        year1=input("Ingrese el año de publicación: ").strip()
        while True:
            if (year1.isdigit()) and (int(year1)>0 and int(year1)<datetime.now().year):
                break
            else:
                year1=input("Introduce un año válido: ").strip()
        year1=int(year1)

        quantity1=input("Ingrese la cantidad del libro: ").strip()
        while True:
            if (quantity1.isdigit()) and (int(quantity1)>0):
                break
            else:
                quantity1=input("Introduce una cantidad válida: ").strip()
        quantity1=int(quantity1)
        price1=input("Ingrese el precio de reposicion: ").strip()
        while True:
            if (price1.replace(".","",1).isdigit()) and (float(price1)>0):
                break
            else:
                price1=input("Introduce un precio válido: ").strip()
        price1=float(price1)
        dic[title1]=[author1,genre1,year1,quantity1,price1]
        showDict()
        main()

def main():
    op=input("¿Qué quieres hacer?\n" \
    "1: Agregar un nuevo libro\n" \
    "Otro para salir: ")
    if op.isdigit() and int(op)==1:
        print('-'*80)
        OptionSelected(int(op))
    else:
        print("Salida exitosa")
main()