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
    
    numcharacters += 1
    if character not in newcharacters:
        newcharacters.append(character)
	
    if character in " .,;::()\"":
        if word.upper() not in newwords and word != "" and word != "\n":
           newwords.append(word.upper())
        
        if word !="":
            numwords += 1
            word = ""
            
    elif character == "\n":
        numparagraphs += 1
    else:
        word += character
        
    character = file.read(1) 
   
    
numparagraphs = int((numparagraphs)/2 +1 )

print(f"Number of characters: {numcharacters}")
print(f"Number of words: {numwords}")
print(f"Number of paragraphs: {numparagraphs}")
print(f"Number of new characters: {len(newcharacters)}")
print(f"Number of new words: {len(newwords)}")