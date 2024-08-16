a = []
def cheching(x, y, A) -> bool:
    return (x + 2 * y < A) or (y > x) or (x > 60)

for A in range(0, 300):
    f= True
    for x in range(0, 300):
        for y in range(0, 300):
            if not(cheching(x, y ,A)):
                f = False

    if f:
        a.append(A)

print(min(a))

