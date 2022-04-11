try:
    nombre = input("cual es tu nombre: ")
    if len(nombre) >1:
        nombre_nuevo = "el nombre es " + nombre

    print(nombre_nuevo)
except:
    print("paso un error, coloca bien el nombre")

else:
    print("todo esta bien")# por si todo sale bein 
finally:
    print("fin de la iteracion ")#asi tenga error se ejecuta