# # paises_y_capitales = {
# #     "Japon": "Tokio",
# #     "Inglaterra": "Londres",
# #     "Francia": "Paris",
# #     "Alemania": "Berlin",
# # }

# # for key, value in paises_y_capitales:
# #     print(f"{key} - {value}")


# # for key, value in kwargs.

# ja = ["a", "b", "2", "3", "4", "7"]


# # def average(lst):
# #     # suma = 0

# #     for index, item in enumerate(lst, start=3):
# #         # suma += suma + float(item[index])
# #         # print(item[index])
# #         print(item)
# #         print(index)

# # return suma / index


# # print(average(ja))


# # Convert list to a string
# # xs = ["1", "2", "3"]
# # s = "".join(xs)
# # print(s)
# # def medi(self):
# # datos, total = [], []
# # my_numbers = input("Dime los numeros: ")
# # for num in [int(n) for n in my_numbers.split(" ")]:
# #     if num > 0:
# #         datos.append(num)
# # media = sum(datos) / len(datos)
# # eleva = (num - media) ** 2
# # total.append(round(eleva))
# # mivar = sum(total) / (len(datos))

# # print(datos)
# # print(media)
# # print(eleva)
# # print(sum(total))
# # print(mivar)

# # my_list = []

# # for i in ["PYTHON", "PHP"]:
# #     my_list.append(i)

# # print(my_list)

# my_list2 = [
#     "*",
#     "I",
#     "B",
#     "M",
#     " ",
#     "i",
#     "s",
#     " ",
#     "a",
#     " ",
#     "t",
#     "r",
#     "a",
#     "d",
#     "e",
#     "m",
#     "a",
#     "r",
#     "k",
#     " ",
#     "o",
#     "f",
#     " ",
#     "t",
#     "h",
#     "e",
#     " ",
#     "I",
#     "n",
#     "t",
#     "e",
#     "r",
#     "n",
#     "a",
#     "t",
#     "i",
#     "o",
#     "n",
#     "a",
#     "l",
#     " ",
#     "B",
#     "u",
#     "s",
#     "i",
#     "n",
#     "e",
#     "s",
#     "s",
#     " ",
#     "M",
#     "a",
#     "c",
#     "h",
#     "i",
#     "n",
#     "e",
#     " ",
#     "C",
#     "o",
#     "r",
#     "p",
#     "o",
#     "r",
#     "a",
#     "t",
#     "i",
#     "o",
#     "n",
#     ".",
# ]

# print("".join(my_list2))


# a = [1, "a", 3, "b"]
# print(f"unpack a list: {' '.join(str(x) for x in a)}")
# print(f"unpack a list: {' '.join([str(x) for x in a][1:3])}")
# print(f"unpack a list: {' '.join([str(x) for x in a])}")
# print(f"unpack a list: {', '.join([str(x) for x in a])}")

# names = ["Sam", "Peter", "James", "Julian", "Ann"]
# print(*names, sep=", ")
opt = opt
options = [opt + x for x in range(1,12)]
print(options)

# my_list = list(range(opt1, opt6))
# print(my_list, sep=", ")