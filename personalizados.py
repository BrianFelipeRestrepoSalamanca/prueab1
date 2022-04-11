try:
    nombre= input("introduce tu nombre: ")
    edad = int(input("introduce tu edad: "))

    if edad< 5 or edad > 100:
        raise ValueError ("la edad introducida no es real")

    elif len(nombre)<= 1:
        raise ValueError("El nombre no esta completo")

    else:
        print("bienvenido al master de python")
except ValueError:
    print("introduce los datos correctos por fis ")
except Exception as e:
    print("tienes un problema", e)