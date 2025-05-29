score = [
    ("BAJO", 0, 25),
    ("ACEPTABLE", 26, 50),
    ("SOBRESALIENTE", 51, 80),
    ("EXCELENTE", 81, 100)
]

def clasificar_nota(nota):
    for i, (nombre, inicio, fin) in enumerate(score, start=1):
        if inicio <= nota <= fin:
            return f"✨ Resultado: {i}. {nombre} ✨"
    return "❌ Nota fuera de rango ❌"

def mostrar_rangos():
    mensaje = "\n" + "="*40 + "\n"
    mensaje += "     RANGOS DE NOTAS DISPONIBLES\n"
    mensaje += "="*40 + "\n"
    for i, (nombre, inicio, fin) in enumerate(score, start=1):
        mensaje += f"{i}. {inicio:3} a {fin:3} -> {nombre}\n"
    mensaje += "="*40 + "\n"
    return mensaje

nota = float(input("Ingrese la nota: "))
print(mostrar_rangos())
print(clasificar_nota(nota))
print("="*40)