import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Определяем целевую функцию f(x1, x2, x3)
def f(x):
    # Вычисляем значение функции по заданной формуле
    return np.log(0.4 * (x[0] - 0.9) ** 4 + 0.4 * (x[1] - 0.6) ** 4 + 0.6 * (x[2] - 0.9) ** 4 + 4)

# Функция для выполнения алгоритма имитации отжига
def simulated_annealing():
    # Начальные значения для переменных x1, x2, x3
    x_old = np.array([0.0, 0.0, 0.0])
    t = 1000  # Начальная температура
    t_min = 0.001  # Минимальная температура для завершения алгоритма
    max_step = 0.1  # Максимальный шаг для изменения переменных
    k = 0  # Счетчик итераций

    # Создаем DataFrame для хранения результатов
    results = pd.DataFrame(columns=["Iteration", "Temperature", "x1", "x2", "x3", "f(x)", "df", "Probability", "Message"])
    f_values = []  # Список для хранения значений целевой функции

    # Основной цикл алгоритма, продолжается, пока температура больше минимальной
    while t > t_min:
        k += 1  # Увеличиваем счетчик итераций
        t *= 0.9  # Уменьшаем температуру

        # Генерируем случайные изменения для x1, x2 и x3
        a = max_step * (np.random.rand() - 0.5)
        b = max_step * (np.random.rand() - 0.5)
        c = max_step * (np.random.rand() - 0.5)
        x_new = x_old + np.array([a, b, c])  # Новые значения переменных

        # Вычисляем изменение значения функции
        df = f(x_new) - f(x_old)

        # Если новое значение функции меньше или равно старому, переходим к новой точке
        if df <= 0:
            x_old = x_new
            message = "перешли в новую точку с уменьшением f(x)"
            probability = 0  # Вероятность перехода
        else:
            # Если новое значение функции больше, решаем, переходить ли к новой точке
            if np.random.rand() < np.exp(-df / t):
                x_old = x_new
                message = "перешли в новую точку с увеличением f(x)"
            else:
                message = "остались в старой точке"  # Остаемся в старой точке
            probability = np.exp(-df / t)  # Вычисляем вероятность перехода

        # Сохраняем результаты текущей итерации в DataFrame
        results = pd.concat([results, pd.DataFrame([{
            "Iteration": k,
            "Temperature": t,
            "x1": x_old[0],
            "x2": x_old[1],
            "x3": x_old[2],
            "f(x)": f(x_old),
            "df": df,
            "Probability": probability,
            "Message": message
        }])], ignore_index=True)

        # Сохраняем значение целевой функции
        f_values.append(f(x_old))

    return results, f_values  # Возвращаем результаты и значения функции

# Запуск алгоритма
results, f_values = simulated_annealing()

# Построение трехмерного графика динамики значения целевой функции
fig = C.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Отображаем итерации, x1 и x2
ax.plot(results['x1'], results['x2'], f_values, marker='o', color='b', label='Динамика f(x)')

# Настраиваем заголовок и метки осей
ax.set_title('Динамика значения целевой функции f(x) в процессе имитации отжига')
ax.set_xlabel('x1')
ax.set_ylabel('x2')
ax.set_zlabel('f(x)')
ax.legend()  # Добавляем легенду

plt.show()  # Отображаем график

# Вывод результатов
print(results)