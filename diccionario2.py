score = (["BAJO",0,25], ["ACEPTABLE",26,50], ["SOBRESALIENTE",51,80],["EXCELENTE",81,100])

print(score[:])
print(score[1:])
print(score[:1])
print(score[1:1])
print(score[1:-1:2])

def funcion(nota):
    for i, n in enumerate(score, start= 1):
        if(nota >= n[1] and nota <= n[2]):
            print(f"La nota es: {i} - {n[0]}")
            break

def promedios():
    mensaje= "Notas: \n"
    for i, n in enumerate(score, start=1):
        mensaje += promedionota(posicion= i, nombre= n[0], rango= [n[1], n[2]]) + "\n"
        #mensaje += f"{i}. {n[0]} a {n[2]} \n"
    return mensaje



def promedionota(posicion: int, nombre: str, rango: list):
    return f"{posicion}. {rango[0]} a {rango[1]} -> {nombre}"


nota = float(input("Ingrese la nota: "))
print(promedios())
funcion(nota)



