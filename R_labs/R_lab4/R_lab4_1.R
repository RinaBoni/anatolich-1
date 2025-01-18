
# Лабораторная 4

setwd("C:/study/anatolich-1/R_labs/R_lab4/Workdir")


# Задание 1

# Проверка существования файла
if (file.exists("данные.xlsx")) {
  # Загрузка данных
  data <- read_excel("данные.xlsx", sheet = "Стьюдент1")
  
  # Выборка
  x <- data$X
  
  # Проверка гипотезы H0: µ = 8
  cat("Проверка гипотезы H0: µ = 8\n")
  cat("Двусторонняя альтернатива:\n")
  print(t.test(x, mu = 8, alternative = "two.sided"))
  
  cat("Односторонняя альтернатива (µ < 8):\n")
  print(t.test(x, mu = 8, alternative = "less"))
  
  cat("Односторонняя альтернатива (µ > 8):\n")
  print(t.test(x, mu = 8, alternative = "greater"))
  
  # Проверка гипотезы H0: µ = 6
  cat("\nПроверка гипотезы H0: µ = 6\n")
  cat("Двусторонняя альтернатива:\n")
  print(t.test(x, mu = 6, alternative = "two.sided"))
  
  cat("Односторонняя альтернатива (µ < 6):\n")
  print(t.test(x, mu = 6, alternative = "less"))
  
  cat("Односторонняя альтернатива (µ > 6):\n")
  print(t.test(x, mu = 6, alternative = "greater"))
  
  
} else {
  cat("Файл 'данные.xlsx' не найден по указанному пути.\n")
}