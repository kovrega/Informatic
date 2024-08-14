"""

"""


def move(n: int, lim: int, s: int, t: int) -> int:
    """
    :param n: Номер хода
    :param lim: Лимит ходов
    :param s: Кол-во камней в куче
    :param t: История сделанных ходов
    :return: Игрок/Соперник/Проигрыш обоих
    """

    """
    1 2 3
    П В П
    """

    # 1 - игрок ходит сейчас
    # 2 - игрок ходит следующим
    player = 2 - n % 2
    rival = 3 - player

    if s >= 50: return rival
    if n > lim: return 0

    # Список возможных ходов
    pos = [(s + 1, 0), (s + 2, 1), (s * 2, 2)]


    # Условие того, что игрок не может сделать предыдущий ход соперника
    if len(t) > 0: del pos[t[-1]]


    # Все возможные исходы
    res = [move(n + 1, lim, x[0], t + [x[1]]) for x in pos]


    if any([x == player for x in res]): return player
    if all([x == rival for x in res]): return rival

    return 0


print('№_19:', *[s for s in range(1, 50) if move(1, 2, s, []) == 2])
print('№_20:', *[s for s in range(1, 50) if move(1, 1, s, []) == 0 and move(1, 3, s, []) == 1])
print('№_21:', *[s for s in range(1, 50) if move(1, 2, s, []) == 0 and move(1, 4, s, []) == 2])
print( )


def two_moves(n: int, lim: int, s: tuple, t: int) -> int:
    """
    :param n: Номер хода
    :param lim: Лимит ходов
    :param s: Кол-во камней в куче
    :param t: История сделанных ходов
    :return: Игрок/Соперник/Проигрыш обоих
    """

    """
    1 2 3
    П В П
    """

    # 1 - игрок ходит сейчас
    # 2 - игрок ходит следующим
    player = 2 - n % 2
    rival = 3 - player

    if sum(s) >= 77: return rival
    if n > lim: return 0

    # Список возможных ходов
    pos = [(s[0] + 1, s[1], 0), (s[0] * 2, s[1], 1), (s[0], s[1] + 1, 2), (s[0], s[1] * 2, 3)]


    # Условие того, что игрок не может сделать предыдущий ход соперника
    # if len(t) > 0: del pos[t[-1]]


    # Все возможные исходы
    res = [two_moves(n + 1, lim, (x[0], x[1]), t + [x[-1]]) for x in pos]

    ps = [x == player for x in res]
    rs = [x == rival for x in res]
    if any(ps): return player
    if any(rs): return rival #  №_19
    # if all(rs): return rival # №_20-21

    return 0


print('№_19:', *[s for s in range(1, 70) if two_moves(1, 2, (s, 7), []) == 2])
print('№_20:', *[s for s in range(1, 70) if two_moves(1, 1, (s, 7), []) == 0 and two_moves(1, 3, (s, 7), []) == 1])
print('№_21:', *[s for s in range(1, 70) if two_moves(1, 2, (s, 7), []) == 0 and two_moves(1, 4, (s, 7), []) == 2])



