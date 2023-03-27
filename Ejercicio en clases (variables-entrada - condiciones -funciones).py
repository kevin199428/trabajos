print("Hola Mundo!!Soy Kevin Villamarin:)")
print("Hola Mundo1!!")
print("Hola Mundo2!!")

# Variables

texto = "Repaso de Python con Yeiko"
nombre = "Kevin Miranda"
altura = "187cm"
year = 2020 

print(f"{texto} - {nombre} - {altura} - {str(year)}")
print(texto + " - " + nombre + " - " + altura + " - " + str(year))

# Entrada

sitioweb = input("¿Cual es tu pagina web: ")
print("El sitio web del usuario es: " + sitioweb)

# Condiciones

altura = int(input("¿Cual es tu altura?: "))

if altura >= 180:
    print("Eres una persona Alta!!")
else:
    print("Eres BAJITO!!")    

# Funciones 

def mostrarAltura():
    altura = int(input("¿Cual es tu altura?: "))

if altura >= 180:
    print("Eres una persona Alta!!")
else:
    print("Eres BAJITO!!")   

mostrarAltura()
mostrarAltura()
mostrarAltura()    

