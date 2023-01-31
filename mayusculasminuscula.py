#Programa que toma una cadena de caracteres digitada por pantalla
#cuenta mayusculas, minusculas, espacios, numeros y caracteres especiales
#Los totaliza cada uno y genera una nueva cadena invirtiendo mayusculas por minisculas
#y minusculas por mayuscular
#Desarrollado por Oswaldo Ardila Medina
#Bogotá, Colombia
#Enero 30 de 2023
import os
os.system("cls")
string = input("Ingrese una cadena de carateres: ")
newstring = ''
count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0
  
for a in string:
  
    # Revisa si es minuscula y
    # la convierte en mayuscula
    if (a.isupper()) == True:
        count1 += 1
        newstring += (a.lower())
  
    # Revisa si la letra es mayuscula y
    # la convierte en minuscula
    elif (a.islower()) == True:
        count2 += 1
        newstring += (a.upper())
  
    # Revisa si es un espacio y
    # lo adiciona a la nueva cadena
    elif (a.isspace()) == True:
        count3 += 1
        newstring += a
    #Revisa si el caracter corresponde a un número
    #y lo adiciona a la nueva cadena
    elif a=="1" or a=="2" or a=="3" or a=="4" or a=="5" or a=="6" or a=="7" or a=="8" or a=="9" or a=="0":
        count5 +=1
        newstring +=a
    #si no es mayuscula, minuscula o espacio entonces
    #es un caracter especial, lo cuenta y lo pasa a la cadena
    #sin transformarlo
    else:
        count4 += 1
        newstring += a
        
  
print("La cadena original fue : " + string)
print("MAYUSCULAS SON: -", count1)
print("MINUSCULAS SON: -", count2)
print("ESPACIOS -", count3)
print("NUMEROS HAY ", count5)
print("CARACTERES ESPECIALES -", count4)
  
print("\t\tNueva cadena transformada: ")
print("\t\t\t" + newstring)