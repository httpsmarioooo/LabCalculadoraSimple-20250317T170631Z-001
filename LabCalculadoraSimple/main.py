# while True:
#     print("1 Take two numbers and subtract the second from the first number.")
#     print("2 Take two numbers and multiply the two.")
#     print("3 Take two numbers and divide the first number by the second number")
#     print("4 Take two numbers and perform a modulus operation.")
#     print("5 Allow users to choose which operation they want to perform on two numbers.")
#     print("6 Take 3 numbers and add them together.")
#     print("7 Allow users to mix operations with 3 numbers or more")
#     print("8 Sumar dos numeros??????")

#     try:
#         opcion = int(input("Ingrese una opcion: "))

#         if opcion == 1:
#             numeroUno = float(input("number 1: "))
#             numeroDos = float(input("number 2: "))

#             resta = numeroUno - numeroDos
#             print("El resultado de la resta es: ",resta)

#         elif opcion == 2:
#             numeroUno = float(input("number 1: "))
#             numeroDos = float(input("number 2: "))

#             multiplicacion = numeroUno * numeroDos
#             print("El resultado de la multiplicacion es: ",multiplicacion)

#         elif opcion == 3:
#             numeroUno = float(input("number 1: "))
#             numeroDos = float(input("number 2: "))

#             division = numeroUno / numeroDos
#             print("El resultado de la division es: ",division)

#         elif opcion == 4:
#             numeroUno = float(input("number 1: "))
#             numeroDos = float(input("number 2: "))

#             modulo = numeroUno % numeroDos
#             print("El resultado de la operacion de moodulo  es: ",modulo)

#         elif opcion == 5:
#             numeroUno = float(input("Ingrese el primer numero: "))
#             operador = input("Ingrese la operacion (+, -, *, /, %): ")
#             numeroDos = float(input("Ingrese el segundo numero: "))

#             if operador == "+":
#                 print("Resultado:", numeroUno + numeroDos)

#             elif operador == "-":
#                 print("Resultado:", numeroUno - numeroDos)

#             elif operador == "*":
#                 print("Resultado:", numeroUno * numeroDos)

#             elif operador == "/":
#                 if numeroDos == 0:
#                     print("Error: No se puede dividir por cero.")
#                 else:
#                     print("Resultado:", numeroUno / numeroDos)

#             elif operador == "%":
#                 print("Resultado:", numeroUno % numeroDos)

#             else:
#                 print("Operador no valido.")

#         elif opcion == 6:
#             numeroUno = float(input("number 1: "))
#             numeroDos = float(input("number 2: "))
#             numeroTres = float(input("number 3: "))

#             sumaTresNumeros = numeroDos + numeroUno + numeroTres
#             print("El resultado de la suma de tres numeros es: ",sumaTresNumeros)

#         elif opcion == 7:
#             expresion = input("Ingresa una expresion matematica /Ejemplo (2+3*2-3/3): ")
#             try:
#                 resultado = eval(expresion)
#                 print("Resultado:", resultado)
#             except Exception:
#                 print("Error: expresion no valida.")

#         elif opcion == 8:
#             numeroUno = float(input("number 1: "))
#             numeroDos = float(input("number 2: "))

#             suma = numeroUno + numeroDos
#             print("El resultado de la suma es: ",suma)

#         else:
#             print("Opcion invalida")
#         break

#     except ValueError:
#         print("Error, ingrese un numero")


#! Con solo esto pasó el 2 de 2 ajajajajajajaj pero el otro codigo esta bien, lo que pienso es
#! el test se topa con el while, diciendo "yo estoy esperando un valor para una suma, no un valor
#! para elegir una opcion" entonces supongo sho, que es eso y creo que el while hace ruido y por eso pasaba el error :)
numeroUno = float(input("number 1: "))
numeroDos = float(input("number 2: "))

suma = numeroUno + numeroDos
print("El resultado de la suma es: ",suma)
