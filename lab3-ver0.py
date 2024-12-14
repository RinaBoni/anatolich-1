"""Чаевые. Входные переменные: качество блюда, качество обслуживания.
 Выходная переменная: величина чаевых.
 Качество блюда - X
 Качество обслуживания - Y
 Величина чаевых - Z
"""


def centroide(c, m, left, right):
    def cx(t):

        return t * c(t)

    n = 2 * m
    h = (right - left) / n
    numerator = cx(left) + cx(right)
    denominator = c(left) + c(right)
    for k in range(1, m + 1):
        numerator += 4 * cx(left + h * (2 * k - 1))
        denominator += 4 * c(left + h * (2 * k - 1))
    for k in range(1, m):
        numerator += 2 * cx(left + h * 2 * k)
        denominator += 2 * c(left + h * 2 * k)
    return numerator / denominator


def trapf(t, alpha, beta, gamma, delta):
    if t <= alpha or t > delta:
        return 0.0
    elif alpha < t <= beta:
        return (t - alpha) / (beta - alpha)
    elif beta < t <= gamma:
        return 1.0
    elif gamma < t <= delta:
        return (t - delta) / (gamma - delta)
    else:
        return None


def trif(t, alpha, beta, delta):
    if t <= alpha or t > delta:
        return 0.0
    elif alpha < t <= beta:
        return (t - alpha) / (beta - alpha)
    elif beta < t <= delta:
        return (t - delta) / (beta - delta)
    else:
        return None


def ltrapf(t, alpha, beta):
    if t <= alpha:
        return 0.0
    elif alpha < t <= beta:
        return (t - alpha) / (beta - alpha)
    elif beta < t:
        return 1.0
    else:
        return None


def rtrapf(t, gamma, delta):
    if t <= gamma:
        return 1.0
    elif gamma < t <= delta:
        return (t - delta) / (gamma - delta)
    elif delta < t:
        return 0.0
    else:
        return None


input_terms = [
    [[rtrapf, 0.11, 0.83], [trapf, 0.12, 0.23, 0.85, 0.91], [ltrapf, 0.23, 0.82]],
    [[rtrapf, 0.17, 0.76], [trapf, 0.13, 0.62, 0.72, 0.87], [ltrapf, 0.14, 0.92]]
]

output_terms = [
    [rtrapf, 0.21, 0.85], [trapf, 0.12, 0.36, 0.47, 0.89], [ltrapf, 0.37, 0.95]
]

concls = [
    [0, 0, 1], [0, 1, 0], [0, 2, 0],
    [1, 0, 2], [1, 1, 1], [1, 2, 0],
    [2, 0, 2], [2, 1, 2], [2, 2, 1]
]

input_args = [0.9, 0.2]

u = []

for concl in concls:
    levels = []
    for k, elem in enumerate(input_args):
        function = input_terms[k][concl[k]][0]
        arguments = [elem] + input_terms[k][concl[k]][1:]
        levels.append(function(*arguments))
    u.append(min(levels))


def c(z):
    truncated = []
    for k, concl in enumerate(concls):
        function = output_terms[concl[-1]][0]
        arguments = [z] + output_terms[concl[-1]][1:]
        truncated.append(min(u[k], function(*arguments)))
    return max(truncated)


print(zo := centroide(c, 10, 0, 1))
