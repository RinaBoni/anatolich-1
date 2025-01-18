
# Лабораторная 3

setwd("C:/study/anatolich-1/R_labs/R_lab3/Workdir")

# Задание 1

# Установка параметров графика
par(bg = "black")  # Установка цвета фона
plot(NA, xlim = c(-6, 6), ylim = c(-1.5, 1.5), type = "n", axes = FALSE)  # Создание пустого графика

# Построение графика функции
x <- seq(-6, 6, by = 0.1)  # Генерация значений x
y <- sin(x)  # Вычисление значений y
lines(x, y, col = "yellow", lwd = 2)  # Добавление линии графика

# Настройка осей
axis(1, las = 1, cex.axis = 0.75, col.axis = "white")  # Ось X
axis(2, las = 1, cex.axis = 0.75, col.axis = "white")  # Ось Y
abline(h = 0, col = "white")  # Горизонтальная линия на уровне Y=0
abline(v = 0, col = "white")  # Вертикальная линия на уровне X=0

# Добавление заголовка
title(main = "График функции y = sin(x)", font.main = 3, family = "Segoe UI", col.main = "white")  # Заголовок курсивом
