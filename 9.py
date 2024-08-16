with open('9_2024.csv', 'r') as f:
    k_ = f.readlines()

k = [list(map(int, el.split(';'))) for el in k_]
count_line = 0


for line in k:
    count = 0
    t = []
    for el in line:
        if line.count(el) == 2 and el not in t:
            count += 1
            t.append(el)


    if count == 2:
        if sum(t) / 2 < sum(line) / len(line):
            count_line += 1

print(count_line)
