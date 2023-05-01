
# for i in numeros:
#   if i % 2 == 0:
#     pares += 1

    
num_1to19 = input("Dame un numero del 1 al 19 ==>")
for i in range(1, 20):
  if i == int(num_1to19):
    continue
  print(f"{i}-- ", end="")
print("",end="\n")
print("Terminé")