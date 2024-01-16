print("SUMA DE DOS NUMEROS")

numero1 = int(input("Dame un primer numero: "))
numero2 = int(input("Dame un segundo numero: "))

if numero1 > numero2 : 
    print("El numero {} es menor que el {}".format(numero1,numero2))
else:
    print("El numero {} es mayor que el {}".format(numero2,numero1))


print("----------- Pedir una edad -----------")
edad = int(input("Ingresa tu edad: "))
if edad > 18:
    print("Eres mayor de edad")
elif edad == 17:
    print("Ya casi cumples la mayoría")
else:
    print("No eres mayor de edad")