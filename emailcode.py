'''

ejercicio:

leer documento correos para:

obtener una lista con los diferentes dominios

crear nuevo documento indicando nombre de usuario y numero de vocales que contiene el nombre
'''

file = open("lista_correos.csv", "r")
file2 = open("vowels.txt","w")
file2.write("#username\tnumber of vowels\n")

domains = []

while True:
    email  = file.readline()
    if not email: break
    [user, domain] = email.split("@")
    if domain[:-1] not in domains: domains.append(domain[:-1]) 
    usercap = user.upper()
    numvowels = (usercap.count("A") +
                 usercap.count("E") +
                 usercap.count("I") +
                 usercap.count("O") +
                 usercap.count("U"))
                 
    file2.write(f"{user}\t{numvowels}\n")
  
print(f"print domains list: {domains}",)
    
