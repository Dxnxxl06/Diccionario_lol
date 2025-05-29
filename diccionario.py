score = (["BAJO",0,25], ["ACEPTABLE",26,50], ["SOBRESALIENTE",51,80],["EXCELENTE",81,100])

def funcion(nota):
    
    

    if nota > 0 and nota <= score[0][1]:
        print(f"LA nota es: {score[0][0]}")
    elif nota >= score [0][1] and nota <= score [1][1]:
        print(f"La nota es: {score[1][0]}")
    elif nota >= score [1][1] and nota <= score[2][1]:
        print(f"La nota es: {score[2][0]}")
    elif nota >= score [2][1] and nota <= score[3][1]:
        print(f"La nota es: {score[3][0]}")
    else:
        print("Nota no valida...")

nota = float(input("Ingrese la nota:"))
funcion(nota)


print(score)
print (score[0])
print(score[0][0])
print(score[0][1])


