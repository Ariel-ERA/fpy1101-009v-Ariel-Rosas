#Disponibilidad_:
#Stock Inicial:

stock_libros = 120
capacidad_maxima = 120

#Variabilidad de control:

prestamos_activos = 0
total_prestamos = 0

print(" ¡Bienvenidos al sistema de gestión de préstamos de la biblioteca central! ")

while True:
    print("\n********** MENÚ PRINCIPAL ********** ")
    print("1) - Libros disponibles")
    print("2) - Realizar préstamos")
    print("3) - Devolver Préstamos")
    print("4) - Historial de préstamos")
    print("5) - Salir")
    
    opcion = input("Seleccione una opción: ")
    
    #Opción 1:
    
    if opcion == "1":
        print(f"Libros disponibles: {stock_libros}")
        
    #Opción 2:
    
    elif opcion == "2":
        try:
            cantidad = int(input("Ingrese cantidad de libros a prestar: "))
            if cantidad <= 0:
                print("ERROR: Debe ingresar una cantidad mayor a ( 0 ) ")
                
            elif cantidad > stock_libros:
                print("No hay suficientes libros disponibles para realizar préstamos")
            else:
                stock_libros -= cantidad
                prestamos_activos += cantidad
                total_prestamos += cantidad
                
                print("Prestamos realizados correctamente")
                print(f"Libros disponibles: {stock_libros}")
                
        except ValueError:
            print("Debe ingresar un N° entero")
    
    #opción 3:
    
    elif opcion == "3":
        try:
            cantidad =  int(input("Ingrese cantidad de Libros a devolver: "))
            
            if cantidad <= 0:
                print("ERROR: Debe ingresar una cantidad mayor a 0")
                
            elif cantidad > prestamos_activos:
                print("No puede devolver mas libros de los que están prestados")
            
            elif stock_libros + cantidad > capacidad_maxima:
                print("La devolución supera la capacidad máxima de la biblioteca")
                
            else:
                stock_libros += cantidad
                prestamos_activos += cantidad
                
                print("Devolución realizada correctamente")
                print(f"Libros disponibles {stock_libros}")
    
        except ValueError:
            print("Debe ingresar un N° entero")
            
    #Opción 4:
    
    elif opcion == "4":
        print("\n********** HISTORIAL DE PRESTAMOS ********** ")
        print(f"Préstamos activos: {prestamos_activos}")
        print(f"Total de préstamos realizados en la sesión: {total_prestamos}")
        
    #Opción 5:
    
    elif opcion == "5":
        print("Gracias!!! por utilizar nuestro software, hasta la próxima Beyby")
        break
    else:
        print("Opción no válida. Intente nuevamente :) ")          
                
               
    

