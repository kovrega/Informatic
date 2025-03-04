# with open('9_2024.csv', 'r') as f:
#     k_ = f.readlines()
#
# k = [list(map(int, el.split(';'))) for el in k_]
# count_line = 0
#
#
# for line in k:
#     count = 0
#     t = []
#     for el in line:
#         if line.count(el) == 2 and el not in t:
#             count += 1
#             t.append(el)
#
#
#     if count == 2:
#         if sum(t) / 2 < sum(line) / len(line):
#             count_line += 1
#
# print(count_line)




# import csv
#
#
# with open("C:\\Users\\kovre\\Downloads\\9-8-A1-B2-95101.csv") as f:
#     # l = [tuple(map(int, s.split(';'))) for s in f.read().split()]
#     l = [tuple(map(int, s)) for s in csv.reader(f, delimiter=';')]
#
#
# # print(l[:5])
# st_cnt = []
# # 1
#
# # for st in l:
# #     if all(x % 2 != 0 if st.count(x) == 1 else x % 2 == 0 for x in st):
# #         if sum(st.count(x) == 2 for x in st) == 2 :
# #             st_cnt.append(st)
#
# # 2
# # for st in l:
# #     if st.count(max(st)) == 1:
# #         if all(x % 2 != 0 if st.count(x) == 1 else x % 2 == 0 for x in st):
# #             st_cnt.append(st)
#
# print(len(l))
# # print(len(st_cnt))
# for st in l:
#     if sum(st.count(x) == 1 for x in st) == 6:
#         if st.count(max(st)) == st.count(min(st)):
#             st_cnt.append(st)
#
#
#
#
# print(len(st_cnt))

















import csv


with open("C:\\Users\\kovre\\Downloads\\9-8-A3-B3-98836.csv") as f:
    l = [tuple(map(int, s)) for s in csv.reader(f, delimiter=';')]


st_cnt = []

# Ср арифм

# for st in l:
#     if  2 * (max(st) + min(st)) < sum(st):
#         nep, pov = [], []
#         for x in st:
#             if st.count(x) == 1:    nep.append(x)
#             else:   pov.append(x)
#         if len(pov) == 0:   sr_pov, sr_nep = 0, sum(nep) / len(nep)
#         else:   sr_pov, sr_nep = sum(pov) / len(pov), sum(nep) / len(nep)
#
#
#         if sr_nep < sr_pov:
#
#
#         # if all(x % 2 != 0 if st.count(x) == 1 else x % 2 == 0 for x in st):
#             st_cnt.append(st)




for st in l:
    if sum(st.count(x) == 2 for x in set(st)) == 3:

        if max(st) % min(st) != 0:
            st_cnt.append(st)


print(f'Всего: {len(l)}')
print(f'Ответ: {len(st_cnt)}')


















































