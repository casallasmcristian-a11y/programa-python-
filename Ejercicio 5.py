recursos = [
    ["Juan", 8, 8, 8, 8, 8],
    ["Ana", 9, 8, 9, 8, 9],
    ["Luis", 7, 8, 7, 8, 7],
    ["María", 10, 9, 10, 9, 10]
]

def clasificar_jornada(total_horas):
    if total_horas > 40:
        return "Sobretiempo"
    else:
        return "Horario Estándar"

for recurso in recursos:
    nombre = recurso[0]
    total_horas = sum(recurso[1:])
    clasificacion = clasificar_jornada(total_horas)

    print("Nombre:", nombre)
    print("Total de horas:", total_horas)
    print("Clasificación:", clasificacion)
    print("---------------------------")