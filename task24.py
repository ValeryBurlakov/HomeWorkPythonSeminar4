import random

# чистая рабочая версия
n = int(input("Введите количество кустов: "))
list_1 = []
list_2 = []
numeration = []
x = 2
for x in range(n):
    numeration.append(x + 1)
for i in range(n):
    list_1.append(int(random.randint(1, 9)))

print(f"на кустах выросло столько ягод:\n{numeration}\n{list_1}")

if n == 2:
    print(f"На двух кустах выросло: {list_1[0] + list_1[1]} ")
elif n == 1:
    print(f"На одном кусте: {list_1[0]}")

max1 = 0
if n > 2:
    sum_null_index = list_1[0] + list_1[1] + list_1[n-1]
    sum_n_index = list_1[0] + list_1[n - 2] + list_1[n - 1]
    for index in range(len(list_1)):
        if index > 0 and index < n - 1:
            sum = list_1[index - 1] + list_1[index] + list_1[index + 1]
            list_2.append(sum)
            if sum > max1:
                max1 = sum
    max_berry = max(list_2)
    print(f"Максимальное количество ягод за 1 заход: {max_berry}")



# версия с выводом каждого действия
# n = int(input("Введите количество кустов: "))
# list_1 = []
# list_2 = []
# for i in range(n):
#     list_1.append(int(random.randint(1, 9)))
# print(f"на кустах выросло столько ягод:\n{list_1}")
# sum_null_index= list_1[0] + list_1[1] + list_1[n-1]
# sum_n_index = list_1[0] + list_1[n - 2] + list_1[n - 1]
# max1 = 0
# for index in range(len(list_1)):
#     if index > 0 and index < n - 1:
#         sum = list_1[index - 1] + list_1[index] + list_1[index + 1]
#         # print( list_1[index], list_1[index - 1], list_1[index + 1])
#         list_2.append(sum)
#         if sum > max1:
#             max1 = sum
# # print(f"между {list_2}")
# # print(f"Нулевой индекс {sum_null_index}, максимальный между {max1}, последний индекс {sum_n_index}")
# max_berry = max(list_2)
# # print(max_berry)
# print(f" Максимальное количество ягод за 1 заход: {max_berry}")




# самая грубая версия

# n = int(input())
# list_1 = []
# list_2 = []
# for i in range(n):
#     list_1.append(int(random.randint(1, 9)))
# print(list_1)
# sum_null_index= list_1[0] + list_1[1] + list_1[n-1]
# sum_n_index = list_1[0] + list_1[n - 2] + list_1[n - 1]
# max1 = 0
# for index in range(len(list_1)):
#     if index > 0 and index < n - 1:
#         sum = list_1[index - 1] + list_1[index] + list_1[index + 1]
#         # print( list_1[index], list_1[index - 1], list_1[index + 1])
#         list_2.append(sum)
#         if sum > max1:
#             max1 = sum
# print(f"между {list_2}")
# print(f"Нулевой индекс {sum_null_index}, максимальный между {max1}, последний индекс {sum_n_index}")
# max_berry = max(list_2)
# print(max_berry)

# # max_berry = 0
# # if sum_null_index > max1:
# #     max_berry = sum_null_index
# # else:
# #     max_berry = max1
# # if sum_n_index > max_berry:
# #     max_berry = sum_n_index
# # else:
# #     max_berry
# print(f" Максимальное количество ягод за 1 заход: {max_berry}")