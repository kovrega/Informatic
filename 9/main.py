





with open('9-4-B2-C1-94183.csv') as f:
    l = f.read().split()

c = 0
for st in l:
    s = sorted(map(int, st.split(';')))
    if s.count(s[-1]) == s.count(s[0]):
        p = []
        np = set()
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                p.append(s[i])
            else:
                if s[i] not in p:   np.add(s[i])

        sr_1 = sum(np) / len(np)
        if len(p) == 0:     sr_2 = 0
        else:  sr_2 = sum(p) / len(p)
        if sr_1 < sr_2:
            c += 1



print(c)











