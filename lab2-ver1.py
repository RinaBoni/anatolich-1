import numpy as np


def solve_bimatrix_game(A, B):
    # A - матрица выигрышей первого игрока
    # B - матрица выигрышей второго игрока

    # Определяем количество стратегий
    m, n = A.shape

    # Ищем смешанные стратегии
    p = np.zeros(m)  # Вероятности для первого игрока
    q = np.zeros(n)  # Вероятности для второго игрока

    # Начальные вероятности
    p[0] = 1
    q[0] = 1

    # Итеративный процесс для нахождения равновесия Нэша
    for _ in range(1000):
        # Обновляем вероятности первого игрока
        for i in range(m):
            p[i] = np.sum(q * A[i])  # Ожидаемая выплата для стратегии i

        p /= np.sum(p)  # Нормируем

        # Обновляем вероятности второго игрока
        for j in range(n):
            q[j] = np.sum(p * B[:, j])  # Ожидаемая выплата для стратегии j

        q /= np.sum(q)  # Нормируем

    return p, q


# Пример матриц выплат
A = np.array([[3, 0], [5, 1]])  # Матрица выигрышей первого игрока
B = np.array([[2, 4], [1, 3]])  # Матрица выигрышей второго игрока

p, q = solve_bimatrix_game(A, B)

print("Вероятности для первого игрока:", p)
print("Вероятности для второго игрока:", q)