#Первый способ решиния

# def whos_first1(p1, p2):
#     no_space1 = p1.rstrip()
#     simvol1 = len(no_space1) - 6
#     no_space2 = p2.rstrip()
#     simvol2 = len(no_space2) - 6
#     if simvol1 == simvol2:
#         print('Ничья')
#     elif simvol1 < simvol2:
#         print('Победил p1')
#     elif simvol1 > simvol2:
#         print('Победил p2')
# whos_first1("     Bang!   ", "     Bang!   ")

#Второй способ решения

def whos_first2(p1, p2):
    if p1.find('B') > p2.find('B'): # с помощь метода find находим вхождение В у первого игрока и сравниваем с вхождением у другого игрока
        print('Cтреляет быстрее p2')
    elif p1.find('B') < p2.find('B'): 
        print('Cтреляет быстрее p2')
    elif p1.find('B') == p2.find('B'): 
        print('Ничья')


whos_first2("               Bang! ", "             Bang!   ")