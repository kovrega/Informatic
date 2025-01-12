input_q = int(input())
"""
_15_ 16 17 18 19 _20_ 21 22 23 24 _25_
"""

res = 0
for start_q in range(1, input_q + 1):
# for start_q in range(5):
    for q in range(start_q, 1_000, input_q):
        P = []
        Q = [x for x in range(q + 1, q+ input_q + 1)]
        sum_q = sum(Q)

        pi = q
        while pi > 0 and sum(P) < sum_q:
            P.append(pi)
            pi -= 1

        if sum(P) == sum_q:
            # print(len(P))
            # print(' '.join(map(str, reversed(P))), ":", ' '.join(map(str, reversed(Q))))
            # print(sum(P), ':', sum_q)
            # print('\n')
            res += 1


print(res)
