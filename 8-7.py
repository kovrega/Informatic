cnt = 0
alf = 'FEDCBA9876543210'
for x1 in range(6):
    for x2 in range(x1 + 1,7):
        for x3 in range(x2 + 1, 8):
            for x4 in range(x3 + 1, 9):
                for x5 in range(x4 + 1, 10):
                    for x6 in range(x5 + 1, 11):
                        for x7 in range(x6 + 1, 12):
                            for x8 in range(x7 + 1, 13):
                                for x9 in range(x8 + 1, 14):
                                    for x10 in range(x9 + 1, 15):
                                        for x11 in range(x10 + 1, 16):
                                            for x12 in range(x11 + 1, 16):
                                                #x = [x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12]
                                                #if  all(int(x[i], 16) > int(x[i + 1], 16)  for i in range(len(x) - 1)):
                                                #    if all(int(x[i], 16) % 2 != int(x[i + 1], 16) % 2 for i in range(len(x) - 1)):
                                                if x1 < x2 < x3 < x4 < x5 < x6 < x7 < x8 < x9 < x10 < x11 < x12 and\
                                                    x1 % 2 == x3 % 2 == x5 % 2 == x7 % 2 == x9 % 2 == x11 % 2 and \
                                                    x2 % 2 == x4 % 2 == x6 % 2 == x8 % 2 == x10 % 2 == x12 % 2 and \
                                                    x1 % 2 != x2 % 2:
                                                        cnt += 1
print(cnt)
