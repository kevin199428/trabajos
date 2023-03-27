# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 00:39:03 2023

@author: Kevin
"""
#El contenido de la lista y el diccionario no se imprimió porque las sentencias 
#de impresión no hacían referencia a las variables que contenían la lista y el diccionario. 

#En cambio, solo estaban imprimiendo las cadenas literales "país" y "capitales".

#Para arreglar el código, necesitamos reemplazar los literales de cadena 
#con las variables que contienen la lista y el diccionario.



# Create a list of the BRICS countries
countries = [
    "Brazil",
    "Russia",
    "India",
    "China",
    "South Africa"
]

"""Create a dictionary of BRICS capitals.
Note that South Africa has 3
 capitals. Therefore, we embed a list inside
the dictionary.
"""


capitals = {
    "Brazil": "Brasilia",
    "Russia": "Moscow",
    "India": "New Delhi",
    "China": "Beijing",
    "South Africa": [
        "Pretoria",
        "Cape Town",
        "Bloemfontein"
    ]
}

# Print the list and dictionary
print(countries)
print(capitals)


"""
What response did you get?
Why did the list and dictionary
 contents not print?
Fix the code and run the script again.
"""

# Access the 2nd capital of South Africa (Cape Town)
print(capitals["South Africa"][1])


"""
Why did you get an error for the
 2nd capital of South Africa?
Hint: Check the syntax for the 
index value.
"""


#Con respecto al error que obtuvimos para la segunda capital de Sudáfrica, 
#la sintaxis utilizada para acceder al valor del diccionario era incorrecta.

#La sintaxis correcta para acceder al segundo elemento de la lista dentro de la clave "Sudáfrica"
#​​del diccionario "capitales" es capitales["Sudáfrica"][1], 
#no capitales["Sudáfrica"[1]]. Este último intenta acceder al segundo carácter de la cadena "Sudáfrica", 
#que no existe, en lugar de acceder 
#al segundo elemento de la lista dentro de la clave "Sudáfrica".














