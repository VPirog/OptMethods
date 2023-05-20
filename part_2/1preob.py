import re

with open('res.txt', 'r') as f:  # открываем файл для чтения
    with open('res_preob.txt', 'w') as g:  # открываем новый файл для записи
        for line in f:  # читаем файл построчно
            new_line = re.sub(r'\d+\.\d+', lambda x: str(round(float(x.group(0)), 5)),
                              line)  # ищем числа с плавающей запятой и округляем их до двух знаков после запятой
            g.write(new_line)  # записываем новую строку в новый файл
