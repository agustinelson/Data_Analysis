'''
Ejercicio 2:
Descargar el archivo ciencia_de_datos_wikipedia.txt y obtener:

Número de parrafos.

Número de palabras totales y número de palabras diferentes.

Número de caracteres totales y número caracteres de diferentes.
'''

file = open("ciencia_de_datos_wikipedia.txt","r")

character = file.read(1)
word = ""
numcharacters = 0
numparagraphs = 0
numwords = 0
newcharacters = [character]
newwords = []


while character:
    
  #  print(character, end = "")
    numcharacters += 1
    if character not in newcharacters:
        newcharacters.append(character)
	
    if character == " ":
        if word not in newwords:
           # print(word)
            newwords.append(word)
        numwords += 1
        word = ""
    elif character == "\n":
        print(numparagraphs)
        numparagraphs += 1
        
        
    word += character
    character = file.read(1) 
