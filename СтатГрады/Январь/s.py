from collections import Counter
import csv

# Чтение данных из CSV-файла
with open("Материалы/09.csv", newline='', encoding='UTF-8') as f:
    reader = csv.reader(f, delimiter=';')
    data = [list(map(int, row)) for row in reader]

# Количество строк и столбцов
n_rows = len(data)
n_cols = len(data[0])

# Предварительный расчет среднего арифметического для каждой строки
averages = [sum(row) / n_cols for row in data]

# Создание списка для хранения количества каждого элемента в каждом столбце
column_counts = [Counter() for _ in range(n_cols)]

# Заполнение column_counts
for row in data:
    for col in range(n_cols):
        column_counts[col].update([row[col]])


# Функция проверки наличия одной интересной ячейки в строке
def has_one_interesting_cell(row_index):
    row = data[row_index]
    average = averages[row_index]

    interesting_cells = 0

    for col in range(n_cols):
        value = row[col]

        # Условие 1: число не встречается в других ячейках той же строки
        if row.count(value) == 1:

            # Условие 2: число встречается не менее 330 раз в других ячейках того же столбца
            if column_counts[col][value] >= 330:

                # Условие 3: число больше среднего арифметического всех чисел строки
                if value > average:
                    interesting_cells += 1

                    # Если найдена одна интересная ячейка, возвращаемся
                    if interesting_cells == 1:
                        return True

    return False


# Подсчет строк с ровно одной интересной ячейкой
result = sum(1 for i in range(n_rows) if has_one_interesting_cell(i))

print(result)