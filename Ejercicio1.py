#Datos a considerar:

especialistas = 0
residentes = 0

#Validar cantidad de profesionales (médicos)

while True:
    try:
        cantidad = int(input("¿Cuántos médicos desea registrar?: "))
        if cantidad > 0:
            break
        else:
            print("¡¡¡Registro médico inválido!!! Ingresa un N° entero positivo para continuar.")
    except ValueError:
        print("¡¡¡Registro médico inválido!!! Ingresa un N° entero positivo para continuar.")

# Registro de profesionales médicos:

for i in range(cantidad):
    print(f"\nRegistro del médico {i + 1}")

    # Validación nombre de profesionales:
    
    while True:
        nombre = input(" ***** Ingrese el nombre del profesional***** : ")

        if len(nombre) >= 6 and " " not in nombre:
            break
        else:
            print("¡¡¡Nombre del profesional inválido!!! ¡¡¡Debe tener al menos 6 caracteres y no contener espacios!!! ")

    # Validar experiencia clínica:
    
    while True:
        try:
            experiencia = int(input("Ingrese los años de experiencia clínica: "))

            if experiencia > 0:
                break
            else:
                print("¡¡¡Error clínico!!! ¡¡¡Ingresa un N° positivo para la experiencia!!! ")
        except ValueError:
            print("¡¡¡Error clínico!!! ¡¡¡Ingresa un N° positivo para la experiencia!!! ")

    # Clasificación a determinar:
    
    if experiencia > 5:
        clasificacion = "Especialista Senior"
        especialistas += 1
    else:
        clasificacion = "Residente Junior"
        residentes += 1

    print(f"{nombre} ha sido clasificado como {clasificacion}.")

# Resumen final: 
print("\n********** RESUMEN FINAL **********")
print(f"¡El hospital cuenta con {especialistas} Especialistas Senior y {residentes} Residentes Junior! ¡Sistema listo para operar!")