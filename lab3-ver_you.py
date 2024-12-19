import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

# Определение входных и выходных переменных
quality_of_dish = np.arange(0, 11, 1)
quality_of_service = np.arange(0, 11, 1)
tip_amount = np.arange(0, 26, 1)

# Определение функций принадлежности для входных переменных
quality_of_dish_low = fuzz.membership.gaussmf(quality_of_dish, 3, 1)
quality_of_dish_medium = fuzz.membership.gaussmf(quality_of_dish, 6, 1)
quality_of_dish_high = fuzz.membership.gaussmf(quality_of_dish, 9, 1)

quality_of_service_poor = fuzz.membership.gaussmf(quality_of_service, 3, 1)
quality_of_service_average = fuzz.membership.gaussmf(quality_of_service, 6, 1)
quality_of_service_excellent = fuzz.membership.gaussmf(quality_of_service, 9, 1)

# Определение функций принадлежности для выходной переменной
tip_low = fuzz.membership.gaussmf(tip_amount, 5, 2)
tip_medium = fuzz.membership.gaussmf(tip_amount, 15, 2)
tip_high = fuzz.membership.gaussmf(tip_amount, 22, 2)

# Определение базы правил нечеткого вывода
rules = [
    (quality_of_dish_low, quality_of_service_poor, 5),
    (quality_of_dish_low, quality_of_service_average, 10),
    (quality_of_dish_low, quality_of_service_excellent, 15),
    (quality_of_dish_medium, quality_of_service_poor, 10),
    (quality_of_dish_medium, quality_of_service_average, 15),
    (quality_of_dish_medium, quality_of_service_excellent, 20),
    (quality_of_dish_high, quality_of_service_poor, 15),
    (quality_of_dish_high, quality_of_service_average, 20),
    (quality_of_dish_high, quality_of_service_excellent, 25)
]


# Агрегация правил и дефаззификация
def sugeno_tip(quality_of_dish, quality_of_service):
    tip_values = []
    membership_values = []
    for rule in rules:
        membership = np.minimum(rule[0][quality_of_dish], rule[1][quality_of_service])
        tip_values.append(rule[2])
        membership_values.append(membership)

    return np.average(tip_values, weights=membership_values)


# Пример использования
print(f"Рекомендуемая величина чаевых: {sugeno_tip(5, 8):.2f}%")