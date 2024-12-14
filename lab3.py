"""
 Чаевые. Входные переменные: качество блюда, качество обслуживания.
 Выходная переменная: величина чаевых.
 Качество блюда - X
 Качество обслуживания - Y
 Величина чаевых - Z
"""


def centroide(c, m, left, right):
    """Функция для вычисления центроида, который используется для дефазификации"""

    def cx(t):
        return t * c(t)  # Умножаем значение t на функцию c(t)

    n = 2 * m  # Увеличиваем количество точек для интеграции
    h = (right - left) / n  # Шаг интеграции
    numerator = cx(left) + cx(right)  # Начальные значения для числителя
    denominator = c(left) + c(right)  # Начальные значения для знаменателя

    # Итерация для вычисления числителя и знаменателя
    for k in range(1, m + 1):
        numerator += 4 * cx(left + h * (2 * k - 1))  # Числитель
        denominator += 4 * c(left + h * (2 * k - 1))  # Знаменатель
    for k in range(1, m):
        numerator += 2 * cx(left + h * 2 * k)  # Числитель
        denominator += 2 * c(left + h * 2 * k)  # Знаменатель

    return numerator / denominator  # Возвращаем значение центроида


def trapf(t, alpha, beta, gamma, delta):
    """Трапециевидная функция для нечеткой логики"""
    if t <= alpha or t > delta:
        return 0.0  # Значение вне диапазона
    elif alpha < t <= beta:
        return (t - alpha) / (beta - alpha)  # Возрастающая часть
    elif beta < t <= gamma:
        return 1.0  # Плоская часть
    elif gamma < t <= delta:
        return (t - delta) / (gamma - delta)  # Убывающая часть
    else:
        return None  # Неверное значение


def trif(t, alpha, beta, delta):
    """Треугольная функция для нечеткой логики"""
    if t <= alpha or t > delta:
        return 0.0  # Значение вне диапазона
    elif alpha < t <= beta:
        return (t - alpha) / (beta - alpha)  # Возрастающая часть
    elif beta < t <= delta:
        return (t - delta) / (beta - delta)  # Убывающая часть
    else:
        return None  # Неверное значение


def ltrapf(t, alpha, beta):
    """Левосторонняя трапециевидная функция"""
    if t <= alpha:
        return 0.0  # Значение вне диапазона
    elif alpha < t <= beta:
        return (t - alpha) / (beta - alpha)  # Возрастающая часть
    elif beta < t:
        return 1.0  # Плоская часть
    else:
        return None  # Неверное значение


def rtrapf(t, gamma, delta):
    """Правосторонняя трапециевидная функция"""
    if t <= gamma:
        return 1.0  # Плоская часть
    elif gamma < t <= delta:
        return (t - delta) / (gamma - delta)  # Убывающая часть
    elif delta < t:
        return 0.0  # Значение вне диапазона
    else:
        return None  # Неверное значение


# Входные термины для качества блюда и качества обслуживания
input_terms = [
    [[rtrapf, 0.1, 0.9], [trapf, 0.2, 0.5, 0.7, 0.8], [ltrapf, 0.5, 0.9]],  # Качество блюда
    [[rtrapf, 0.1, 0.9], [trapf, 0.2, 0.5, 0.7, 0.8], [ltrapf, 0.5, 0.9]]  # Качество обслуживания
]

# Выходные термины для величины чаевых
output_terms = [
    [rtrapf, 0.1, 0.5], [trapf, 0.2, 0.4, 0.6, 0.8], [ltrapf, 0.5, 1.0]
]

# Правила вывода
concls = [
    [0, 0, 1], [0, 1, 0], [0, 2, 0],
    [1, 0, 2], [1, 1, 1], [1, 2, 0],
    [2, 0, 2], [2, 1, 2], [2, 2, 1]
]

# Входные значения для качества блюда и качества обслуживания
input_args = [0.8, 0.6]  # Пример значений

u = []  # Список для хранения уровней

# Вычисление уровня для каждого правила
for concl in concls:
    levels = []  # Список для хранения уровней для текущего правила
    for k, elem in enumerate(input_args):
        function = input_terms[k][concl[k]][0]  # Получаем функцию для текущего входного термина
        arguments = [elem] + input_terms[k][concl[k]][1:]  # Аргументы для функции
        levels.append(function(*arguments))  # Вычисляем уровень и добавляем в список
    u.append(min(levels))  # Добавляем минимальный уровень для текущего правила


def c(z):
    """Функция для вычисления величины чаевых"""
    truncated = []  # Список для хранения усеченных значений
    for k, concl in enumerate(concls):
        function = output_terms[concl[-1]][0]  # Получаем функцию для текущего выходного термина
        arguments = [z] + output_terms[concl[-1]][1:]  # Аргументы для функции
        truncated.append(min(u[k], function(*arguments)))  # Вычисляем усеченное значение
    return max(truncated)  # Возвращаем максимальное усеченное значение


# Вычисление чаевых
print(f'Величина чаевых: ', zo := centroide(c, 10, 0, 1))  # Выводим величину чаевых
