rut = input("Ingrese run sin dv: ")  # el input ya es un str

print(type(rut))
tupla = (2, 3, 4, 5, 6, 7)
indice, sumaX = 0, 0

print(f"line 07 reversed rut: {reversed(rut)}")
print(f"line 08 {type(reversed(rut))}")
for i in reversed(rut):
    print(int(i))
    print(type(int(i)))
    # sumaX += int(i) * tupla[indice]
    # indice += 1
    
    # if indice == 6:
    #     indice = 0
    
# dv = 11 - (sumaX % 11)

# if dv == 10:
#     dv = "K"
# elif dv == 11:
#     dv = 0
# print(f"El dv es: {dv}")

