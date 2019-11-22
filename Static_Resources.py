import random


def moveset_create_batting(user, diff):
    res = {user}
    while len(res) < diff + 4:
        res = res.union({random.randint(0, 10)})
    return list(res)


def moveset_create_bowling(user, diff):
    res = {user}
    while len(res) < 7 - diff:
        res = res.union({random.randint(0, 10)})
    return list(res)


if __name__ == '__main__':
    print(moveset_create_bowling(6, 3))
