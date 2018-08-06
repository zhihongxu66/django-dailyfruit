from random import choice


def ran():
    start_str = 'zxcvbnmasdfghjklqwertyuiop0987654321'
    sum_str = ''
    for _ in range(20):
        one_str = choice(start_str)
        sum_str += one_str

    return sum_str
