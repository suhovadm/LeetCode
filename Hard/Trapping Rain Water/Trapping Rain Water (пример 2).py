# Пример 2.
# Ввод: height = [4,2,0,3,2,5] // Вывод: 9

# Инициализация.
# height = [4, 2, 0, 3, 2, 5]
# indices = 0  1  2  3  4  5
# left = 0, right = 5
# left_max = height[0] = 4
# right_max = height[5] = 5
# water = 0

# Итерация 1.
# left = 0, right = 5, left_max = 4, right_max = 5
# left_max < right_max? Да (4 < 5)
# left += 1 -> left = 1
# left_max = max(4, height[1] = 2) -> left_max = 4
# water += max(0, 4 - height[1] = 2) -> water += 2
# water = 2

# Итерация 2.
# left = 1, right = 5, left_max = 4, right_max = 5
# left_max < right_max? Да (4 < 5)
# left += 1 -> left = 2
# left_max = max(4, height[2] = 0) -> left_max = 4
# water += max(0, 4 - height[2] = 0) -> water +=4
# water = 6

# Итерация 3.
# left = 2, right = 5, left_max = 4, right_max = 5
# left_max < right_max? Да (4 < 5)
# left += 1 -> left = 3
# left_max = max(4, height[3] = 3) -> left_max = 4
# water += max(0, 4 - height[3] = 3) -> water += 1
# water = 7

# Итерация 4.
# left = 3, right = 5, left_max = 4, right_max = 5
# left_max < right_max? Да (4 < 5)
# left += 1 -> left = 4
# left_max = max(4, height[4] = 2) -> left_max = 4
# water += max(0, 4 - height[4] = 2) -> water += 2
# water = 9

# Итерация 5.
# left = 4, right = 5, left_max = 4, right_max = 5
# left_max < right_max? Да (4 < 5)
# left += 1 -> left = 5
# left_max = max(4, height[5] = 5) -> left_max = 5
# water += max(0, 5 - height[5] = 5) -> water += 0
# water = 9

# Конец.
# left = 5, right = 5 -> условие left < right ложно (5 < 5 = False).
# Выходим из цикла.

# Высота:    [4, 2, 0, 3, 2, 5]
# Вода:      [0, 2, 4, 1, 2, 0]
# Всего: 2 + 4 + 1 + 2 = 9

# Уровень 5:               [5]
# Уровень 4: [0]         W [5]
# Уровень 3: [0] W       [3] W [5]
# Уровень 2: [0][1] W   [3][4] W [5]
# Уровень 1: [0][1][2] W [3][4][5]
# Уровень 0: [0][1][2][3][4][5]

# Легенда:
# # - стена
# W - вода

# Полная вертикальная визуализация:
# Индекс 0: 4      ####        0 воды
# Индекс 1: 2      ##WW        2 воды
# Индекс 2: 0      #WWW        4 воды
# Индекс 3: 3      ###W        1 вода
# Индекс 4: 2      ##WW        2 воды
# Индекс 5: 5      #####       0 воды

# Индекс 1: min(max_left=4, max_right=5) - height[1]=2 = 4-2=2 > +2 вода
# Индекс 2: min(max_left=4, max_right=5) - height[2]=0 = 4-0=4 > +4 вода
# Индекс 3: min(max_left=4, max_right=5) - height[3]=3 = 4-3=1 > +1 вода
# Индекс 4: min(max_left=4, max_right=5) - height[4]=2 = 4-2=2 > +2 вода

# Итого: 2 + 4 + 1 + 2 = 9 единиц воды.

# ----------------------------------------------------------------------------------- #