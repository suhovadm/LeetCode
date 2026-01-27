# Пример.
# Для height = [0,1,0,2,1,0,1,3,2,1,2,1] // Вывод: 6

# Инициализация.
# height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
# indices = 0  1  2  3  4  5  6  7  8  9  10  11
# left = 0, right = 11
# left_max = height[0] = 0
# water = 0

# Итерация 1.
# left = 0, right = 11, left_max = 0, right_max = 1
# left_max < right_max? Да (0 < 1)
# left += 1 -> left = 1
# left_max = max(0, height[1] = 1) -> left_max = 1
# water += max(0, 1 - height[1] = 1) -> water += 0
# water = 0

# Итерация 2.
# left = 1, right 11, left_max = 1, right_max = 1
# left_max < right_max? Нет (1 == 1), идём в else
# right -= 1 -> right = 10
# right_max = max(1, height[10] = 2) -> right_max = 2
# water += max(0, 2 - height[10] = 2) -> water += 0
# water = 0

# Итерация 3.
# left = 1, right = 10, left_max = 1, right_max = 2
# left_max < right_max? Да (1 < 2)
# left += 1 -> left = 2
# left_max = max(1, height[2] = 0) -> left_max = 1
# water += max(0, 1 - height[2] = 0) -> water += 1
# water = 1

# Итерация 4.
# left = 2, right = 10, left_max = 1, right_max = 2
# left_max < right_max? Да (1 < 2)
# left += 1 -> left = 3
# left_max = max(1, height[3] = 2) -> left_max = 2
# water += max(0, 2 - height[3] = 2) -> water += 0
# water = 1

# Итерация 5.
# left = 3, right = 10, left_max = 2, right_max = 2
# left_max < right_max? Нет (2 == 2), идём в else
# right -= 1 -> right= 9
# right_max = max(2, height[9] = 1) -> right_max = 2
# water += max(0, 2 - height[9] = 1) -> water += 1
# water = 2

# Итерация 6.
# left = 3, right = 9, left_max = 2, right_max = 2
# left_max < right_max? Нет (2 == 2), идём в else
# right -= 1 -> right = 8
# right_max = max(2, height[8] = 2) -> right_max = 2
# water += max(0, 2 - height[8] = 2) -> water += 0
# water = 2

# Итерация 7.
# left = 3, right = 8, left_max = 2, right_max = 2
# left_max < right_max? Нет (2 == 2), идём в else
# right -= 1 -> right = 7
# right_max = max(2, height[7] = 3) -> right_max = 3
# water += max(0, 3 - height[7] = 3) -> water += 0
# water = 2

# Итерация 8.
# left = 3, right = 7, left_max = 2, right_max = 3
# left_max < right_max? Да (2 < 3)
# left += 1 -> left = 4
# left_max = max(2, height[4] = 1) -> left_max = 2
# water += max(0, 2 - height[4] = 1) -> water += 1
# water = 3

# Итерация 9.
# left = 4, right = 7, left_max = 2, right_max = 3
# left_max < right_max? Да (2 < 3)
# left += 1 -> left = 5
# left_max = max(2, height[5] = 0) -> left_max = 2
# water += max(0, 2 - height[5] = 0) -> water += 2
# water = 5

# Итерация 10.
# left = 5, right = 7, left_max = 2, right_max = 3
# left_max < right_max? Да (2 < 3)
# left += 1 -> left = 6
# left_max = max(2, height[6] = 1) -> left_max = 2
# water += max(0, 2 - height[6] = 1) -> water += 1
# water = 6

# Итерация 11.
# left = 6, right = 7, left_max = 2, right_max = 3
# left_max < right_max? Да (2 < 3)
# left += 1 -> left = 7
# left_max = max(2, height[7] = 3) -> left_max = 3
# water += max(0, 3 - height[7] = 3) -> water += 0
# water = 6

# Конец.
# left = 7, right = 7 -> условие: left < right ложно (7 < 7 = False).
# Выходим из цикла.

# Высота:    [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
# Вода:      [0, 0, 1, 0, 1, 2, 1, 0, 0, 1, 0, 0]
# Всего: 1 + 1 + 2 + 1 + 1 = 6

#     3 |           #           < высота 7 (индекс 7)
#     2 | #       # # #   #     < высоты 3,7,8,10 (индексы 3,7,8,10)
#     1 | # #   # # # # # # #   < все кроме индекса 0
#     0 | # # # # # # # # # # # < все индексы
#        0 1 2 3 4 5 6 7 8 9 10 11

# Вода (W):
#     3 |
#     2 |   W W W W           < вода на уровнях 1 и 2
#     1 | W   W W W W W W     < вода на уровне 1
#     0 |------------------
#        0 1 2 3 4 5 6 7 8 9 10 11

# Вычисления по индексам:
# Индекс 2: min(max_left=1, max_right=3) - height[2]=0 = 1 > +1 вода
# Индекс 4: min(max_left=2, max_right=3) - height[4]=1 = 1 > +1 вода
# Индекс 5: min(max_left=2, max_right=3) - height[5]=0 = 2 > +2 вода
# Индекс 6: min(max_left=2, max_right=3) - height[6]=1 = 1 > +1 вода
# Индекс 9: min(max_left=2, max_right=2) - height[9]=1 = 1 > +1 вода

# Итого: 1 + 1 + 2 + 1 + 1 = 6 едениц воды.

# ----------------------------------------------------------------------------------- #