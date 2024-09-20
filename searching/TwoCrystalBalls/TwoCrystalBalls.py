import math

def twoCrystalBalls(breaks):
    jmpAmount = math.floor(math.sqrt(len(breaks)))

    i = jmpAmount
    while i < len(breaks):
        if breaks[i]:
            break
        i += jmpAmount

    i -= jmpAmount
    for j in range(jmpAmount + 1):
        if i < len(breaks) and breaks[i]:
            return i
        i += 1

    return -1