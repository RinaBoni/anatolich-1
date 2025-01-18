
# Лабораторная 3

setwd("C:/study/anatolich-1/R_labs/R_lab3/Workdir")

# Задание 5

# Установка графического окна для 3 графиков
par(mfrow = c(3, 2))  # 3 строки, 2 столбца

# 1. Генерация равномерно распределенных чисел
uniform_data <- runif(100, min = 0, max = 1)

# Гистограмма для равномерного распределения
hist(uniform_data, main = "Гистограмма равномерного распределения", xlab = "Значения", col = "lightblue", border = "black")

# Ящик с усами для равномерного распределения
boxplot(uniform_data, horizontal = TRUE, main = "Ящик с усами\nравномерного распределения", col = "lightgreen")

# 2. Генерация нормально распределенных чисел
normal_data <- rnorm(100, mean = 0, sd = 1)  # Среднее 0, стандартное отклонение 1

# Гистограмма для нормального распределения
hist(normal_data, main = "Гистограмма нормального распределения", xlab = "Значения", col = "lightcoral", border = "black")

# Ящик с усами для нормального распределения
boxplot(normal_data, horizontal = TRUE, main = "Ящик с усами\nнормального распределения", col = "lightyellow")

# 3. Генерация чисел, распределенных по закону хи-квадрат
chi_square_data <- rchisq(100, df = 5)  # 5 степеней свободы

# Гистограмма для хи-квадрат распределения
hist(chi_square_data, main = "Гистограмма хи-квадрат распределения", xlab = "Значения", col = "lightpink", border = "black")

# Ящик с усами для хи-квадрат распределения
boxplot(chi_square_data, horizontal = TRUE, main = "Ящик с усами\nхи-квадрат распределения", col = "lightblue")