def calculator(number1, operator, number2):
    if number2==0 and operator=='/':
        return 'Нельзя делить на 0!'
    else:
        return int(eval(f'{number1}{operator}{number2}')) # функция eval() подсчитывет динамически обновляемое выражение

calculator()