# 1.Напишите программу, удаляющую из текста все слова, содержащие ""абв""
# text = 'Привет абвменя зовут Иван абвя живу в абвБеларуси'

# def some_words(text):
#     text = list(filter(lambda x: 'абв' not in x, text.split()))
#     return " ".join(text)

# text = some_words(text)
# print(text)
#2.Создайте программу для игры с конфетами человек против человека.Условие задачи: На столе лежит 2021 конфета. 
# Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота "интеллектом"
# from random import randint

# def input_dat(name):
#     x = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
#     while x < 1 or x > 28:
#         x = int(input(f"{name}, введите корректное количество конфет: "))
#     return x

# def p_print(name, k, counter, value):
#     print(f"Ходил {name}, он взял {k}, теперь у него {counter}. Осталось на столе {value} конфет.")

# player1 = input("Введите имя первого игрока: ")
# player2 = input("Введите имя второго игрока: ")
# value = int(input("Введите количество конфет на столе: "))
# flag = randint(0,2) # флаг очередности
# if flag:
#     print(f"Первый ходит {player1}")
# else:
#     print(f"Первый ходит {player2}")

# counter1 = 0 
# counter2 = 0

# while value > 28:
#     if flag:
#         k = input_dat(player1)
#         counter1 += k
#         value -= k
#         flag = False
#         p_print(player1, k, counter1, value)
#     else:
#         k = input_dat(player2)
#         counter2 += k
#         value -= k
#         flag = True
#         p_print(player2, k, counter2, value)

# if flag:
#     print(f"Выиграл {player1}")
# else:
#     print(f"Выиграл {player2}")
#3.Создайте программу для игры в "Крестики-нолики"

# from random import randint

# VERTICAL_COORDINATS = ('a', 'b', 'c')

# def get_user_char():
#     user_char = input('Select char (x, 0): ').strip(' ').lower()
#     while user_char not in ('x', '0'):
#         print('Not available char')
#         user_char = input('Select char (x, 0): ').strip(' ').lower()
#     return user_char

# def show_field(field):
#     print(' ', '1', '2', '3')
#     for y, v in enumerate(VERTICAL_COORDINATS):
#         print(v, ' '.join(field[y]))

# def is_draw(field):
#     count = 0
#     for y in range(3):
#         count += 1 if '_' in field[y] else 0
#     return count == 0

# def get_user_position(field):
#     real_x, real_y = 0, 0
#     while True:
#         coordinats = input('Input coordinats: ').lower().strip(' ')
#         y, x = tuple(coordinats)

#         if int(x) not in (1, 2, 3) or y not in VERTICAL_COORDINATS:
#             print('Not valid coordinats')
#             continue

#         real_x, real_y = int(x) - 1, VERTICAL_COORDINATS.index(y)
#         if field[real_y][real_x] == '_':
#             break
#         else:
#             print('Position not empty')

#     return real_x, real_y

# def get_opponent_char(char):
#     return '0' if char == 'x' else 'x'

# def is_win(char, field):
#     opponent_char = get_opponent_char(char)
#     # проверяем строки
#     for y in range(3):
#         if opponent_char not in field[y] and '_' not in field[y]:
#             return True

#     # проверяем колонки
#     for x in range(3):
#         col = [field[0][x], field[1][x], field[2][x]]
#         if opponent_char not in col and '_' not in col:
#             return True

#     # проверяем диагонали
#     diagonal = [field[0][0], field[1][1], field[2][2]]
#     if opponent_char not in diagonal and '_' not in diagonal:
#         return True
#     diagonal = [field[0][2], field[1][1], field[2][0]]
#     if opponent_char not in diagonal and '_' not in diagonal:
#         return True

#     return False

# field = [
#     ['_' for x in range(3)] for y in range(3)
# ]

# user_char = get_user_char()
# computer_char = get_opponent_char(user_char)

# def get_computer_position(field):
#     x,y = randint(0,2), randint(0,2)
#     while field[y][x] != '_':
#         x,y = randint(0,2), randint(0,2)
#     return x,y

# while True:
#     show_field(field)
#     if is_draw(field):
#         print('is draw')
#         break

#     x, y = get_user_position(field)
#     field[y][x] = user_char
#     if is_win(user_char, field):
#         print('you win')
#         break

#     x, y = get_computer_position(field)
#     field[y][x] = computer_char
#     if is_win(computer_char, field):
#         print('you lose')
#         break

#4.Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# def coding(txt):
#     count = 1
#     res = ''
#     for i in range(len(txt)-1):
#         if txt[i] == txt[i+1]:
#             count += 1
#         else:
#             res = res + str(count) + txt[i]
#             count = 1
#     if count > 1 or (txt[len(txt)-2] != txt[-1]):
#         res = res + str(count) + txt[-1]
#     return res

# def decoding(txt):
#     number = ''
#     res = ''
#     for i in range(len(txt)):
#         if not txt[i].isalpha():
#             number += txt[i]
#         else:
#             res = res + txt[i] * int(number)
#             number = ''
#     return res


# s = input("Введите текст для кодировки: ")
# print(f"Текст после кодировки: {coding(s)}")
# print(f"Текст после дешифровки: {decoding(coding(s))}")