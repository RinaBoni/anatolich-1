import numpy as np
import matplotlib.pyplot as plt


# Определение функций принадлежности
def trapf(t, alpha, beta, gamma, delta):
    """Трапецоидальная функция принадлежности."""
    if t <= alpha or t > delta:
        return 0.0  # Значение вне диапазона
    elif alpha < t <= beta:
        return (t - alpha) / (beta - alpha)  # Левый наклон
    elif beta < t <= gamma:
        return 1.0  # Плоская часть
    elif gamma < t <= delta:
        return (delta - t) / (delta - gamma)  # Правый наклон
    else:
        return None


def trif(t, alpha, beta, delta):
    """Треугольная функция принадлежности."""
    if t <= alpha or t > delta:
        return 0.0  # Значение вне диапазона
    elif alpha < t <= beta:
        return (t - alpha) / (beta - alpha)  # Левый наклон
    elif beta < t <= delta:
        return (delta - t) / (delta - beta)  # Правый наклон
    else:
        return None


def ltrapf(t, alpha, beta):
    """Левая трапецоидальная функция принадлежности."""
    if t <= alpha:
        return 0.0  # Значение вне диапазона
    elif alpha < t <= beta:
        return (t - alpha) / (beta - alpha)  # Наклон
    elif beta < t:
        return 1.0  # Плоская часть
    else:
        return None


def rtrapf(t, gamma, delta):
    """Правая трапецоидальная функция принадлежности."""
    if t <= gamma:
        return 1.0  # Плоская часть
    elif gamma < t <= delta:
        return (delta - t) / (delta - gamma)  # Наклон
    elif delta < t:
        return 0.0  # Значение вне диапазона
    else:
        return None


# Задание термов для входных и выходных переменных
input_terms = [
    [[rtrapf, 0.0, 0.4], [trif, 0.3, 0.5, 0.7], [ltrapf, 0.6, 1.0]],  # Качество блюда
    [[rtrapf, 0.0, 0.4], [trif, 0.3, 0.5, 0.7], [ltrapf, 0.6, 1.0]]  # Качество обслуживания
]

output_terms = [
    [rtrapf, 0.0, 0.4],  # Низкие чаевые
    [trif, 0.3, 0.5, 0.7],  # Средние чаевые
    [ltrapf, 0.6, 1.0]  # Высокие чаевые
]

# База знаний: правила вывода
rules = [
    [0, 0, 0],  # Если качество блюда низкое и обслуживание низкое, то чаевые низкие
    [0, 1, 0],  # Если качество блюда низкое и обслуживание среднее, то чаевые низкие
    [0, 2, 1],  # Если качество блюда низкое и обслуживание высокое, то чаевые средние
    [1, 0, 0],  # Если качество блюда среднее и обслуживание низкое, то чаевые низкие
    [1, 1, 1],  # Если качество блюда среднее и обслуживание среднее, то чаевые средние
    [1, 2, 2],  # Если качество блюда среднее и обслуживание высокое, то чаевые высокие
    [2, 0, 1],  # Если качество блюда высокое и обслуживание низкое, то чаевые средние
    [2, 1, 2],  # Если качество блюда высокое и обслуживание среднее, то чаевые высокие
    [2, 2, 2]  # Если качество блюда высокое и обслуживание высокое, то чаевые высокие
]

# Входные значения для качества блюда и обслуживания
food = float(input("Введите качество блюда (число от 0 до 10): "))/10
service = float(input("Введите качество обслуживания (число от 0 до 10): "))/10
input_values = [food, service]  # Качество блюда и обслуживания

# Вычисление уровней отсечения для каждого правила
u = []  # Уровни отсечения
z_values = []  # Значения выходной переменной

for rule in rules:
    levels = []  # Уровни принадлежности для текущего правила
    for i, value in enumerate(input_values):
        func = input_terms[i][rule[i]][0]  # Функция принадлежности
        params = input_terms[i][rule[i]][1:]  # Параметры функции
        levels.append(func(value, *params))  # Вычисление уровня принадлежности
    u_level = min(levels)  # Уровень отсечения - минимум из уровней принадлежности
    u.append(u_level)

    # Решение уравнения u = f(z) для выходной переменной
    output_func = output_terms[rule[2]][0]  # Функция принадлежности выходной переменной
    output_params = output_terms[rule[2]][1:]  # Параметры функции

    # Найдем z, при котором f(z) = u_level
    z = None
    for z_candidate in [i / 100.0 for i in range(101)]:  # Перебор значений z от 0 до 1
        if abs(output_func(z_candidate, *output_params) - u_level) < 0.01:  # Проверка на соответствие
            z = z_candidate
            break
    z_values.append(z)  # Сохраняем найденное значение z

# Вычисление итогового значения z0
numerator = sum(u[i] * z_values[i] for i in range(len(u)))  # Числитель
denominator = sum(u)  # Знаменатель
z0 = numerator / denominator if denominator != 0 else 0  # Итоговое значение чаевых
z0 *= 10

print(f"Рассчитанная величина чаевых: {z0:.2f}")

# Визуализация функций принадлежности и результата
x = np.linspace(0, 1, 100)  # Значения для построения графиков

# Создание графиков для входных и выходных переменных
fig, axs = plt.subplots(3, 1, figsize=(10, 15))  # Создание подграфиков
for i, variable_name in enumerate(['Качество блюда', 'Качество обслуживания']):
    for term, (func, *params) in zip(['Низкое', 'Среднее', 'Высокое'], input_terms[i]):
        axs[i].plot(x, [func(val, *params) for val in x], label=term)  # Построение графика
    axs[i].set_title(variable_name)  # Заголовок графика
    axs[i].legend()  # Легенда
    axs[i].set_ylim(0, 1.1)  # Ограничение по оси Y

# График для выходной переменной
for term, (func, *params) in zip(['Низкие чаевые', 'Средние чаевые', 'Высокие чаевые'], output_terms):
    axs[2].plot(x, [func(val, *params) for val in x], label=term)  # Построение графика
axs[2].set_title('Величина чаевых')  # Заголовок графика
axs[2].legend()  # Легенда
axs[2].set_ylim(0, 1.1)  # Ограничение по оси Y

# Показать графики
plt.tight_layout()  # Автоматическая настройка отступов
plt.show()  # Отображение графиков