import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Определение входных переменных
# quality_food - качество блюда, принимает значения от 0 до 10
quality_food = ctrl.Antecedent(np.arange(0, 11, 1), 'quality_food')
# quality_service - качество обслуживания, также принимает значения от 0 до 10
quality_service = ctrl.Antecedent(np.arange(0, 11, 1), 'quality_service')

# Определение выходной переменной
# tip_amount - величина чаевых, принимает значения от 0 до 20
tip_amount = ctrl.Consequent(np.arange(0, 21, 1), 'tip_amount')

# Определение функций принадлежности для входной переменной quality_food
quality_food['poor'] = fuzz.trimf(quality_food.universe, [0, 0, 5])   # Плохое качество
quality_food['average'] = fuzz.trimf(quality_food.universe, [0, 5, 10]) # Среднее качество
quality_food['good'] = fuzz.trimf(quality_food.universe, [5, 10, 10])   # Хорошее качество

# Определение функций принадлежности для входной переменной quality_service
quality_service['poor'] = fuzz.trimf(quality_service.universe, [0, 0, 5])   # Плохое качество обслуживания
quality_service['average'] = fuzz.trimf(quality_service.universe, [0, 5, 10]) # Среднее качество обслуживания
quality_service['good'] = fuzz.trimf(quality_service.universe, [5, 10, 10])   # Хорошее качество обслуживания

# Определение функций принадлежности для выходной переменной tip_amount
tip_amount['low'] = fuzz.trimf(tip_amount.universe, [0, 0, 10])   # Низкие чаевые
tip_amount['average'] = fuzz.trimf(tip_amount.universe, [0, 10, 20]) # Средние чаевые
tip_amount['high'] = fuzz.trimf(tip_amount.universe, [10, 20, 20])   # Высокие чаевые

# Определение правил нечёткого вывода
# Правило 1: Если качество блюда или качество обслуживания плохое, то чаевые низкие
rule1 = ctrl.Rule(quality_food['poor'] | quality_service['poor'], tip_amount['low'])
# Правило 2: Если качество блюда и качество обслуживания средние, то чаевые средние
rule2 = ctrl.Rule(quality_food['average'] & quality_service['average'], tip_amount['average'])
# Правило 3: Если качество блюда или качество обслуживания хорошие, то чаевые высокие
rule3 = ctrl.Rule(quality_food['good'] | quality_service['good'], tip_amount['high'])

# Создание системы управления на основе определённых правил
tip_control = ctrl.ControlSystem([rule1, rule2, rule3])
# Создание симуляции системы управления
tip_simulation = ctrl.ControlSystemSimulation(tip_control)

# Ввод значений для оценки чаевых
tip_simulation.input['quality_food'] = 8  # Пример: хорошее качество блюда (8 из 10)
tip_simulation.input['quality_service'] = 9  # Пример: отличное качество обслуживания (9 из 10)

# Вычисление результата на основе введённых значений
tip_simulation.compute()

# Вывод результата: рекомендуемая величина чаевых
print(f'Рекомендуемая величина чаевых: {tip_simulation.output["tip_amount"]}')
# Визуализация результатов для выходной переменной
tip_amount.view(sim=tip_simulation)