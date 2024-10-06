import random

# Generar instancia del problema
def generar_instancia(num_cursos, num_salas, num_bloques, num_dias):
    # Parámetros de la instancia
    capacidad_sala = [random.randint(20, 45) for _ in range(num_salas)]
    capacidad_curso = [random.randint(10, 40) for _ in range(num_cursos)]
    prioridad = [random.randint(6, 10) if (_ + 1) % 5 == 0 else random.randint(1, 5) for _ in range(num_cursos)]
    bloques_necesarios = [2 if random.random() < 0.65 else 1 for _ in range(num_cursos)]

    # Generar disponibilidad aleatoria de profesores
    disponibilidad_profesor = [[[[
        random.choice([True, False]) for _ in range(num_bloques)
    ] for _ in range(num_dias)] for _ in range(num_salas)] for _ in range(num_cursos)]

    # Escribir la instancia en formato MiniZinc
    with open('instancia.txt', 'w') as f:
        f.write(f'num_salas = {num_salas};\n')
        f.write(f'num_cursos = {num_cursos};\n')
        f.write(f'num_bloques = {num_bloques};\n')
        f.write(f'num_dias = {num_dias};\n')

        f.write('capacidad_sala = ' + str(capacidad_sala) + ';\n')
        f.write('capacidad_curso = ' + str(capacidad_curso) + ';\n')
        f.write('prioridad = ' + str(prioridad) + ';\n')
        f.write('bloques_necesarios = ' + str(bloques_necesarios) + ';\n')

        # Guardar disponibilidad en formato MiniZinc
        f.write('disponibilidad_profesor = array4d(Cursos, Salas, Dias, Bloques, [')
        for c in range(num_cursos):
            for s in range(num_salas):
                for d in range(num_dias):
                    for b in range(num_bloques):
                        f.write(f'{int(disponibilidad_profesor[c][s][d][b])}, ')
        f.write(']);\n')

Rango = 0
num_asignaturas = 0
num_salas = 0
Tamaño = int(input("Seleccione capacidad:\n 1.Pequeña\n 2.Mediana\n 3.Grande\n ingrese número: "))
if Tamaño == 1:
    num_salas = 1
    num_asignaturas = int(input("Ingrese número de asignaturas: "))
elif Tamaño == 2:
    Rango = int(input("Seleccionar rango de asignaturas:\n 1.30-35\n 2.45-49\n 3.60-64\n 4.70-74\n 5.80-84\n ingrese número: "))
    if Rango == 1:
        num_asignaturas = random.randint(30, 35)
        num_salas = 3
    elif Rango == 2:
        num_asignaturas = random.randint(45, 49)
        num_salas = 4
    elif Rango == 3:
        num_asignaturas = random.randint(60, 64)
        num_salas = 5
    elif Rango == 4:
        num_asignaturas = random.randint(70, 74)
        num_salas = 6
    elif Rango == 5:
        num_asignaturas = random.randint(80, 84)
        num_salas = 7
elif Tamaño == 3:
    Rango = int(input("Seleccionar rango de asignaturas:\n 1.140-160\n 2.170-190\n 3.200-220\n 4.230-250\n 5.280-300\n ingrese numero:"))
    if Rango == 1:
        num_asignaturas = random.randint(140, 160)
        num_salas = random.randint(10, 12)
    elif Rango == 2:
        num_asignaturas = random.randint(170, 190)
        num_salas = random.randint(13, 15)
    elif Rango == 3:
        num_asignaturas = random.randint(200, 220)
        num_salas = random.randint(16, 18)
    elif Rango == 4:
        num_asignaturas = random.randint(130, 250)
        num_salas = random.randint(19, 22)
    elif Rango == 5:
        num_asignaturas = random.randint(280, 300)
        num_salas = random.randint(23, 25)

bloques_por_dia = 7
dias_por_semana = 5

# Generar una instancia de prueba
generar_instancia(num_asignaturas, num_salas, bloques_por_dia, dias_por_semana)
