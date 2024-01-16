num1=20
num2=4

print("La suma es: ",(num1+num2))
print("La resta es: ",(num1-num2))
print("La multiplicación es: ",(num1*num2))
print("La división es: ",(num1/num2))
print("La división exacta es: ",(num1//num2))
print("La potencia es: ",(num1 ** num2))


# Concatenación en python

texto1="Hola"
texto2="Mundo"
textoFinal= texto1 + " " + texto2 


print("El saludo es: %s %s" %(texto1, texto2))
#Sustituye el valor de la variable en posiciones

saludoFinal ="Saludo: {} {}".format(texto1, texto2)

print(saludoFinal)

saludoFinal2 ="Saludo 2: {x} {y}".format(x=texto1, y=texto2)

print(saludoFinal2)
