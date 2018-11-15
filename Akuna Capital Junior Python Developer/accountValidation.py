def process(line):
    try:
        num = int(line[0: 6], 16)
    except:
        return "INVALID"

    num = int(line[0: 6], 16)
    summ = 0
    while num != 0:
        summ = summ + num % 10
        num = num // 10

    compare = (str(hex(summ))[2:]).upper()
    if line[6:] == compare:
        return "VALID"
    return "INVALID"
