#como manejar diferentes errores
try:
    numero = (input("dame un numero para convertirlo "))

    print("el cuadrado es ", int(numero*numero))
except ValueError:
    print("debes convertir a entero")

except TypeError:
    print("introduce cosas correctas")

except Exception as e:
    print("ha ocurrido un error", type(e).__name__)