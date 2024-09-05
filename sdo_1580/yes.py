# n = int(input())
# l = [list(input().split()) for _ in range(n)]
from turtle import Terminator

n = 5
l = [
    'Валерия Гордиенко 112'.split(),
    'Варя Финоченко 216'.split(),
    'Василиса Шахматова 156'.split(),
    'Анна Сибирова 124'.split(),
    'Дарья Фурман 120'.split(),
]

sr_r = 0

for el in range(n):
    sr_r += int(l[el][-1])

sr_r /= n

res = list(filter(lambda player: int(player[-1]) > sr_r, l))
# -> [['Варя', 'Финоченко', '216'], ['Василиса', 'Шахматова', '156']]



print(sorted(res, key=lambda x: x[-1]))
if


# for el in range(len(res)):
#     for i in range(len(res) - el - 1):
#         if int(res[i][-1]) > int(res[i + 1][-1]):
#             res[i], res[i + 1] = res[i + 1], res[i]
#         elif int(res[i][-1]) ==  int(res[i + 1][-1]):
#             sorted(res, key=res[2])
