num_a = input("Ingrese primer número entero: ")
num_b = input("Ingrese segundo número entero: ")
between_qty = abs(int(num_a) - int(num_b)) - 1

if between_qty < 1:
    print(f"Entre {num_a} y {num_b} no hay números.")
else:
    lowest = min(int(num_a), int(num_b))
    largest = max(int(num_a), int(num_b))
    qty_between = largest - lowest -1
    all_even_between = []
    
    for i in range(lowest + 1, largest):
        print(i)
        if not(i % 2):
            all_even_between.append(i)
            
    qty_even_between = len(all_even_between)
    sum_even_between = sum(all_even_between)
    # print(all_even_between)
    print(f"Entre {lowest} y {largest} hay {qty_between} números siendo {qty_even_between} de ellos pares.")
    print(f"La suma de los pares es de {sum_even_between}.")
