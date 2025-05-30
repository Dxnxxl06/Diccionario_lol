
import os
libros = {}
prestamos = {}
historial = {}

def limpiarConsola():
    os.system("csl" if os.name == "nt" else "clear")

#Gestion de Libros
def agregarLibro():
    codigo = input("Codigo del libro: ")
    if codigo in libros:
        print("El libro ya existe")
        return
    nombre= input("Nombre del libro: ")
    autor= input("Nombre del autor: ")
    editorial= input("Nombre de la editorial: ")
    libros(codigo) = {"nombre": nombre, "autor": autor, "editorial": editorial}
    print("Libro agregado correctamente")

def actualizarLibro():
    codigo= input("Codigo del libro a actualizar:")
    if codigo not in libros:
        print("Libro no encontrado")
        return
    print("Datos actuales:", libros[codigo])
    nombre=("Ingrese el nombre del libro a actualizar")
    autor=("Ingrese el nombre del autor a actualizar")
    editorial=("Ingrese el nombre de la editorial a actualizar")
    if libros[codigo]["nombre"]: nombre 
    if libros[codigo]["autor"]: autor 
    if libros[codigo]["editorial"]: editorial 
    print("Libro Actualizado.")

def eliminarLibro():
    codigo = input("Codigo del librpo a eliminar: ")
    if codigo in libros:
        del libros[codigo]
        print("Libro eliminado exitosamente.")
    else:
        print("Libro no encontrado")

def menuGestionLibros():
    while True:
        print("MENU GESTION DE LIBROS")
        print("1. Agregar Libro")
        print("2. Actualizar Libro")
        print("3. Eliminar Libro")
        print("0. Menu Principal")
        limpiarConsola()
        opcion = input("Seleccione la tarea que desea realizar: ")
        if opcion == 1:
            agregarLibro()
        elif opcion ==2:
            actualizarLibro()
        elif opcion ==3:
            eliminarLibro()
        elif opcion ==0:
            break
        else:
            print("Opcion invalida")

#Prestamo de Libro






while True:
    limpiarConsola()
    print(menuOptions)
    input("Enter para continuar")
        


