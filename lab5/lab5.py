import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import kurtosis, skew, shapiro, normaltest, anderson, kstest

# Функция для анализа данных
def analyze_data(file_path):
    # Загрузка данных
    df = pd.read_csv(file_path, sep=';', decimal=',')
    print(f"Данные из файла {file_path}:\n", df)

    # Вычисление числовых характеристик
    stats = {}
    for column in df.columns:
        stats[column] = {
            'минимальное значения': df[column].min(),
            'максимальное значения': df[column].max(),
            'размах выборки': df[column].max() - df[column].min(),
            'среднее выборочное': df[column].mean(),
            'выборочная дисперсия': df[column].var(ddof=1),
            'среднеквадратическое отклонение': df[column].std(ddof=1),
            'мода': df[column].mode().iloc[0],
            'медиана': df[column].median(),
            'коэффициент эксцесса': kurtosis(df[column]),
            'коэффициент асимметрии': skew(df[column]),
            'первый квартиль': df[column].quantile(0.25),
            'третий квартиль': df[column].quantile(0.75)
        }
    print("\nЧисловые характеристики:")
    for column, values in stats.items():
        print(f"\n{column}:")
        for stat, value in values.items():
            print(f"  {stat}: {value}")

    # Визуализация данных
    for column in df.columns:
        plt.figure(figsize=(12, 6))
        plt.subplot(1, 3, 1)
        sns.histplot(df[column], kde=True, bins=10)
        plt.title(f"Гистограмма {column}")

        plt.subplot(1, 3, 2)
        sns.boxplot(y=df[column])
        plt.title(f"Ящик с усами {column}")

        plt.subplot(1, 3, 3)
        sns.ecdfplot(df[column])
        plt.title(f"Функция распределения {column}")

        plt.tight_layout()
        plt.show()

    # Проверка гипотезы о нормальности распределения
    print("\nПроверка гипотезы о нормальности распределения:")
    for column in df.columns:
        print(f"\n{column}:")
        _, p_shapiro = shapiro(df[column])
        print(f"  Шапиро-Уилк: p-value = {p_shapiro}")
        _, p_dagostino = normaltest(df[column])
        print(f"  Д’Агостино-Пирсон: p-value = {p_dagostino}")
        anderson_result = anderson(df[column])
        print(f"  Андерсон-Дарлинг: statistic = {anderson_result.statistic}, критические значения = {anderson_result.critical_values}")
        _, p_kstest = kstest(df[column], 'norm', args=(df[column].mean(), df[column].std()))
        print(f"  Колмогоров-Смирнов: p-value = {p_kstest}")

# Анализ файла study_data_1.csv
print("Анализ файла study_data_1.csv")
analyze_data('study_data_1.csv')

# Анализ файла study_data_2.csv
print("\nАнализ файла study_data_2.csv")
analyze_data('study_data_2.csv')

# Исследование статистической зависимости
def analyze_relationship(file_path):
    df = pd.read_csv(file_path, sep=';', decimal=',')
    print(f"\nДанные из файла {file_path}:\n", df)

    # Диаграмма рассеяния
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x=df['Рост'], y=df['Вес'])
    plt.title("Диаграмма рассеяния")
    plt.xlabel("Рост")
    plt.ylabel("Вес")
    plt.show()

    # Линейная регрессия
    coeffs = np.polyfit(df['Рост'], df['Вес'], 1)
    print(f"Коэффициенты линейной регрессии: {coeffs}")
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x=df['Рост'], y=df['Вес'])
    plt.plot(df['Рост'], np.polyval(coeffs, df['Рост']), color='red', label='Линейная регрессия')
    plt.title("Диаграмма рассеяния с линейной регрессией")
    plt.xlabel("Рост")
    plt.ylabel("Вес")
    plt.legend()
    plt.show()

    # Коэффициент корреляции Пирсона
    correlation = df['Рост'].corr(df['Вес'])
    print(f"Коэффициент корреляции Пирсона: {correlation}")

# Анализ зависимости для study_data_1.csv
print("\nАнализ зависимости для study_data_1.csv")
analyze_relationship('study_data_1.csv')

# Анализ зависимости для study_data_2.csv
print("\nАнализ зависимости для study_data_2.csv")
analyze_relationship('study_data_2.csv')