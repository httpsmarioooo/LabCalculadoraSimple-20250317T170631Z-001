while True:
    print("* Take two numbers and subtract the second from the first number.")
    print("* Take two numbers and multiply the two.")
    print("* Take two numbers and divide the first number by the second number")
    print("* Take two numbers and perform a modulus operation.")
    print("* Take 3 numbers and add them together.")
    print("* Allow users to mix operations with 3 numbers or more")

    try:
        opcion = int(input("Ingrese una opcion: "))

        if opcion == 1:
            numeroUno = float(input("number 1: "))
            numeroDos = float(input("number 2: "))

            resta = numeroUno - numeroDos
            print(f"El resultado de la resta es: {resta}")

        if opcion == 2:
            numeroUno = float(input("number 1: "))
            numeroDos = float(input("number 2: "))

            multiplicacion = numeroUno * numeroDos
            print(f"El resultado de la multiplicacion es: {multiplicacion}")

        if opcion == 3:
            numeroUno = float(input("number 1: "))
            numeroDos = float(input("number 2: "))

            division = numeroUno / numeroDos
            print(f"El resultado de la division es: {division}")

        if opcion == 4:
            numeroUno = float(input("number 1: "))
            numeroDos = float(input("number 2: "))

            modulo = numeroUno % numeroDos
            print(f"El resultado de la operacion de moodulo  es: {modulo}")

        if opcion == 5:
            numeroUno = float(input("number 1: "))
            numeroDos = float(input("number 2: "))
            numeroTres = float(input("number 2: "))

            sumaTresNumeros = numeroDos + numeroUno + numeroTres
            print(f"El resultado de la suma de tres numeros es: {sumaTresNumeros}")

        elif opcion == 6:
            try:
                print("Resultado:", eval(input("Ingresa una expresión matemática: ")))
            except Exception:
                print("EXPRESION NO VALIDAD")

        else:
            print("Opcion invalida")

    except ValueError:
        print("Error, ingrese un numero")
