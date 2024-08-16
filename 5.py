def some_func(N) -> int:
    BN = bin(N)[2:]

    if int(BN) % 3 == 0:
        BN += BN[-3]
    else:
        BN += bin((int(BN) % 3) * 3)[2:]

    res = int(BN, 2)
    return res

for R in range(2, 100):
    if some_func(R) > 151:
        print(R)
        break


