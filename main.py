
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

def crearPrestamo():
    codigo = input("Ingrese el codigo del libro que quiere pedir prestado: ")
    nombre= input("Nombre de la persona: ")
    documento = input("Ingrese el numero de documento")
    fecha = input("La fecha del prestamo fue (YYYY-MM-DD):")
    prestamo= {"Codigo": codigo, "Nombre": nombre, "Documento": documento, "Fecha del prestamo": fecha, "Devuelto": False }
    prestamo.append(prestamo)
    historial.append(prestamo.copy())
    print("Prestamo Registrado.")

#Devolucion de los libros

def devolucionLibro():
    documento = input("Ingrese el documento del usuario")
    encontrados = [p for p in prestamos if p["documento"] == documento and not p["Devuelto"]]
    if not encontrados:
        print("Este documento no tiene ningun libro prestado")
        return
    for p in encontrados:
        p["Devuelto"] = True
    print("Todos los libros marcados han sido devueltos")

#Lista de libros

def listarLibros():
    pass








while True:
    limpiarConsola()
    print()
    input("Enter para continuar")
        


