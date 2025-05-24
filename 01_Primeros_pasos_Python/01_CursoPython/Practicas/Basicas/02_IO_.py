import io


name = input("Ingrese su nombre: ")
age = input("Ingrese su edad: ")

print(type(name))
print(type(age))


##print( "La variable nombre es de tipo -> " + type(name))
##print("La variable edad es de tipo -> " +type(age))

print(f" Tu edad ingresas es: {age} , Tu nombre Ingresado es: {name} ")
print(" Tu edad ingresas es: {0} , Tu nombre Ingresado es: {1} ".format(age, name))