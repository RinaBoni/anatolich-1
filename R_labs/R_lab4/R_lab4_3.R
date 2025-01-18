
# Лабораторная 4

setwd("C:/study/anatolich-1/R_labs/R_lab4/Workdir")


# Задание 3

# Проверка существования файла
if (file.exists("данные.xlsx")) {
  # Загрузка данных
  data <- read_excel("данные.xlsx", sheet = "Стьюдент3")
  
  # Выборки
  x <- data$X
  y <- data$Y
  
  # Проверка гипотезы H0: µx = µy
  cat("Проверка гипотезы H0: µx = µy\n")
  cat("Двусторонняя альтернатива:\n")
  print(t.test(x, y, alternative = "two.sided", var.equal = FALSE))
  
  cat("Односторонняя альтернатива (µx < µy):\n")
  print(t.test(x, y, alternative = "less", var.equal = FALSE))
  
  cat("Односторонняя альтернатива (µx > µy):\n")
  print(t.test(x, y, alternative = "greater", var.equal = FALSE))
  
  
} else {
  cat("Файл 'данные.xlsx' не найден по указанному пути.\n")
}