import random

tries = 0
comp_random = random.randint(1,50) #Вернёт целое N , подходящее под описание: min <= N <= max from random
while tries <=6:
    user_input = int(input('Введите число от 1 до 50 '))
    tries+=1
    if user_input == comp_random: #проверка на число которое ввел пользовтель и число которое сгенерировал компьютер
        print('Ты угадал')
        break
    elif user_input > comp_random: 
        print('Попробуй ввести число по меньше) ')
    elif user_input < comp_random:
        print('Попробуй ввести число по больше )')
    elif user_input != comp_random and tries == 6: # условие когда не совпадает ввод пользователя и компьютера и попытки исчерпаны
        print('Твои попытки закончились, попробуй еще раз')
        break