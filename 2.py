print('x y w z')
for x in range(0, 2):
    for y in range(0, 2):
        for w in range(0, 2):
            for z in range(0, 2):
                if ((x and not(y)) or (y == z) or not(w)) == 0:
                    print(x, y, w, z)
# Вывод
# x y w z
# 0 0 1 1
# 0 1 1 0
# 1 1 1 0

# Ответ: wzyx




"""
И               | or
Или             | and
Отрицание       | not()
Следование      | <=
"""