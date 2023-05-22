# part_2.part_1.part_2.part_2
# Исследующий поиск
from example import *
a = 0
b = 0


def until_search(base_point, radius, func):
    """
      Минимизация функции с помощью метода штрафных функций
      :param base_point: начальная точка
      :param radius: "радиус" строящегося куба для поиска новых базисных точек
      :param func: функция
      :return: результат исследующего поиска вокруг базисной точки
    """
    new_base_point = base_point[:]  # Ищем новую базисную точку
    new_func = func(new_base_point)
    for i in range(0, len(new_base_point)):
        bn = new_base_point
        bn[i] = bn[i] + radius[i]  # Для новой точки снова ищем новую базисную точку
        fc = func(bn)
        if fc < new_func:
            new_base_point = bn
            new_func = fc
        else:
            bn[i] = bn[i] - 2 * radius[i]
            fc = func(bn)
            if fc < new_func:
                new_base_point = bn
                new_func = fc
    return new_base_point  # Возвращаем базисную точку


# Метод поиска Хука-Дживса
def hooke_jeeves_method(old_base_point, h, e, f):
    steps = 0
    stips = 0
    z = 0.1
    run_outer_loop = True
    while run_outer_loop:
        global b
        stips += 1
        b = stips
        run_outer_loop = False
        run_inner_loop = True
        xk = old_base_point  # step1
        base_ponit = until_search(old_base_point, h, f)  # step2
        while run_inner_loop:
            global a
            steps += 1
            a = steps
            run_inner_loop = False
            for i in range(len(old_base_point)):  # step3
                xk[i] = old_base_point[i] + 2 * (base_ponit[i] - old_base_point[i])
            x = until_search(xk, h, f)  # step4
            old_base_point = base_ponit  # step5
            fx = f(x)
            fb1 = f(old_base_point)
            if fx < fb1:  # step6
                base_ponit = x
                run_inner_loop = True  # to step3
            elif fx > fb1:  # step7
                run_outer_loop = True  # to step1
                break
            else:
                s = 0
                for i in range(len(h)):
                    s += h[i] * h[i]
                if e * e > s:  # step8
                    break  # to step10
                else:
                    for i in range(len(h)):  # step9
                        h[i] = h[i] * z
                    run_outer_loop = True  # to step1
    return old_base_point  # step10



precision = 0.0001

print(hooke_jeeves_method([1, 1, 1], [1, 1, 1], precision, f),
      f(hooke_jeeves_method([1, 1, 1], [1, 1, 1], precision, f)), a, b)

"""Данный код реализует метод конфигураций Хука-Дживса для поиска минимума многомерной функции. Метод состоит из следующих шагов:

part_1. Задать начальную точку b1, шаг h и погрешность e.
part_2. Исследующий поиск: найти точку b2, лучше b1.
3. Отразить точку b2 относительно точки xk = b1 + part_2*(b2 - b1).
4. Исследующий поиск: найти точку x, лучше xk.
5. Обновить точку b1 = b2.
6. Если f(x) < f(b1), обновить точку b2 = x, перейти к шагу 3.
7. Если f(x) > f(b1), перейти к шагу part_1.
8. Если h^part_2 + e^part_2 < , прекратить поиск и вернуть b1.
9. Изменить размер шага h на z (обычно z=0.part_1), вернуться к шагу part_1.
10. Вернуть b1 как найденный минимум функции.

Также в коде сохраняются пути, которые проходят точки b1, b2, xk и x."""
