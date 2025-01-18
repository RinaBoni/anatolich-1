

setwd("C:/study/anatolich-1/R_labs/R_lab5/Workdir")

# Лабораторная 5

# Проверка существования файла
if (file.exists("ks.xlsx")) {
  
  
  # Чтение данных из файла ks.xlsx
  data <- read_excel("ks.xlsx")
  
  # Извлечение выборок X и Y
  x <- data$X
  y <- data$Y
  
  # Выполнение теста Колмогорова-Смирнова для всех альтернативных гипотез
  ks_test_two_sided <- ks.test(x, y, alternative = "two.sided")
  ks_test_less <- ks.test(x, y, alternative = "less")
  ks_test_greater <- ks.test(x, y, alternative = "greater")
  
  # Вывод результатов тестов
  cat("Результаты теста Колмогорова-Смирнова:\n")
  cat("Альтернатива 'two.sided':\n")
  cat("Статистика D =", ks_test_two_sided$statistic, ", p-значение =", ks_test_two_sided$p.value, "\n\n")
  
  cat("Альтернатива 'less':\n")
  cat("Статистика D =", ks_test_less$statistic, ", p-значение =", ks_test_less$p.value, "\n\n")
  
  cat("Альтернатива 'greater':\n")
  cat("Статистика D =", ks_test_greater$statistic, ", p-значение =", ks_test_greater$p.value, "\n\n")
  
  # Построение эмпирических кумулятивных функций распределения (ECDF)
  ecdf_x <- ecdf(x)
  ecdf_y <- ecdf(y)
  
  # Построение графика
  plot(ecdf_x, col = "blue", main = "Эмпирические кумулятивные функции распределения",
       xlab = "Значения", ylab = "ECDF", lwd = 2)
  lines(ecdf_y, col = "red", lwd = 2)
  
  # Добавление легенды
  legend("bottomright", legend = c("X", "Y"), col = c("blue", "red"), lwd = 2)
  
  
} else {
  cat("Файл 'ks.xlsx' не найден по указанному пути.\n")
}