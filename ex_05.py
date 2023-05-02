num_a = int(input("Ingrese primer número entero: "))
num_b = int(input("Ingrese segundo número entero: "))

between_qty = abs(num_a - num_b) - 1

if between_qty < 1:
    print(f"Entre {num_a} y {num_b} no hay números.")
else:
    mini = min(num_a, num_b)
    maxi = max(num_a, num_b)

    count_even_between, sum_even_between = 0, 0
    # count_even_between = sum_even_between = 0

    for i in range(mini + 1, maxi):
        print(i)
        if i % 2 == 0:  # if not(i % 2):
            sum_even_between += i
            count_even_between += 1

    print(
        f"Entre {mini} y {maxi} hay {maxi - mini -1} números siendo {count_even_between} de ellos pares."
    )
    print(f"La suma de los pares es: {sum_even_between}.")
