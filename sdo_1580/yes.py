n = int(input())
l = [list(input().split()) for _ in range(n)]


# n = 5
# l = [
#     'Валерия Гордиенко 112',
#     'Варя Финоченко 216',
#     'Василиса Шахматова 156',
#     'Анна Сибирова 124',
#     'Дарья Фурман 120',
# ]

sr_r = 0

for el in range(n):
    sr_r += int(l[el].split()[-1])

sr_r /= n

res = list(filter(lambda player: int(player.split()[-1]) > sr_r, l))
# -> ['Варя Финоченко 216', 'Василиса Шахматова 156']


sorted(res, key=lambda x: x.split()[-1], reverse=True)
for el in range(len(res) - 1):
    if int(res[el].split()[-1]) == int(res[el + 1].split()[-1]):
        sorted(res[el : el + 2], key= lambda x: x.split()[-2])
    if res[el].split()[-2] == res[el + 1].split()[-2]:
        sorted(res[el: el + 2], key=lambda x: x.split()[0])
print(res)




# for el in range(len(res)):
#     for i in range(len(res) - el - 1):
#         if int(res[i][-1]) > int(res[i + 1][-1]):
#             res[i], res[i + 1] = res[i + 1], res[i]
#         elif int(res[i][-1]) ==  int(res[i + 1][-1]):
#             sorted(res, key=res[2])
