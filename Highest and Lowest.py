def high_and_low(numbers):
    a = [int(x) for x in numbers.split()]
    return (f'{max(a)} {min(a)}')
    