# Games Rock Paper Scissors
import random

user_input = True
while user_input:
    user_choice = input('Введите (r/s/p) ').lower()
    if user_choice not in ['s', 'r', 'p']:
        print('Вы не правильно ввели значение, попробуйте снова')
        continue
    comp_choice = random.choice(['r','s','p'])
    winning_combinations = [('p','r'),('r','s'),('s','p')]
    if user_choice == comp_choice:
        print('Ничья')
    elif (user_choice,comp_choice) in winning_combinations:
        print('Вы попбедили :)')
    else:
        print('Вы проиграли :(')
    user_input = input('Вы хотите продолжить?Если да введите Да, если нет введите нет ') == 'Да' 