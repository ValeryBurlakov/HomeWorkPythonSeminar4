n = int(input("введите количество элементов 1 множества: "))
m = int(input("Введите количество элементов 2 множества: "))

list_1 = []
list_2 = []

print("Введите элементы первого множества:")
for i in range(n):
    list_1.append(int(input(f"введите элемент {i + 1}: ")))
print("Введите элементы второго множества:")
for i in range(m):
    list_2.append(int(input(f"введите элемент {i + 1}: ")))

list_1 = set(list_1)
list_2 = set(list_2)

# print(list_1.union(list_1, list_2)) # можно не создавать новый список а запихнуть всё в один из имеющихся
list_3 = list_1.union(list_2)
print(list_3)




# n = int(input("введите количество элементов 1 множества: "))
# m = int(input("Введите количество элементов 2 множества: "))
# list_1 = []
# list_2 = []
# print("Введите элементы первого множества")
# for i in range(n):
#     list_1.append(int(input()))
# print("Введите элементы второго множества")
# for i in range(m):
#     list_2.append(int(input()))
# # print(list_1)
# # print(list_2)
# list_1 = set(list_1)
# list_2 = set(list_2)
# # print(list_1)
# # print(list_2)
# list_3 = list_1.union(list_2)
# print(list_3)