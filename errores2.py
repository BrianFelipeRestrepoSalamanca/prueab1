Lista1=[1,2,3,4,55,66,88,60]

for i in Lista1: 
    print(i)

Lista1.sort()
print(Lista1)
print(len(Lista1))
try:
    busca=int (input("que numero de la lista deseas buscar: "))
    if busca in Lista1:
        print(f"el numero {busca} esta ubicado en la posicion {Lista1.index(busca)} del arreglo")    
except :
    print("parece que el numero no esta")   

