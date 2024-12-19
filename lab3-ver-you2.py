import numpy as np

class SugenoFuzzySystem:
    def init(self):
        self.rules = []

    def add_rule(self, condition, output):
        self.rules.append((condition, output))

    def evaluate(self, inputs):
        total_weighted_output = 0
        total_weight = 0

        for condition, output in self.rules:
            # Вычисляем степень истинности условия
            weight = condition(inputs)
            if weight > 0:
                # Вычисляем выходное значение
                weighted_output = output(inputs) * weight
                total_weighted_output += weighted_output
                total_weight += weight

        # Возвращаем взвешенное среднее
        return total_weighted_output / total_weight if total_weight > 0 else 0

# Пример использования
def condition1(inputs):
    x, y = inputs
    return max(0, min(1, (x + y - 1)))  # Пример нечеткого условия

def output1(inputs):
    x, y = inputs
    return 2 * x + 3 * y  # Линейная функция

# Создаем систему
sugeno_system = SugenoFuzzySystem()
sugeno_system.add_rule(condition1, output1)

# Оценка системы с входными данными
inputs = (0.5, 0.5)
result = sugeno_system.evaluate(inputs)
print(f"Результат вывода: {result}")