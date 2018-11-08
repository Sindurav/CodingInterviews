def is_power_of_four(n):
    if n < 1:
        return False
    while n % 4 == 0:
        n /= 4
    return n == 1
