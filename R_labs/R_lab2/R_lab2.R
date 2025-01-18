
# Лабораторная 2

setwd("C:/study/anatolich-1/R_labs/R_lab2/Workdir")

# Проверка существования файла
if (file.exists("data.csv")) {
  # Чтение данных
  data <- read.table("data.csv", header = TRUE, sep = ";")
  
  
  
  
  # Задание 2
  
  # Очистка данных от NA
  cl_data <- na.omit(data)
  
  # Определение количества строк в исходной и очищенной таблицах
  col_all <- nrow(data)
  col_cleaned <- nrow(cl_data)
  
  # Вывод результатов
  cat("\n")
  cat("Количество строк в исходной таблице:", col_all, "\n")
  cat("Количество строк в очищенной таблице:", col_cleaned, "\n")
  
  
  
  
  # Задание 3
  
  # Сортировка очищенной таблицы
  sorted_data <- cl_data[order(cl_data$Пол, -cl_data$Математика), ]
  
  # Вывод отсортированной таблицы
  cat("\n")
  print(sorted_data)
  cat("\n")
  
  
  
  
  
  # Задание 4
  
  # Подсчет количества мужчин и женщин
  sex_count <- table(cl_data$Пол)
  
  # Вывод результатов
  cat("\n")
  cat("Количество мужчин:", sex_count["М"], "\n")
  cat("Количество женщин:", sex_count["Ж"], "\n")
  
  
  
  
  
  # Задание 5
  
  # Извлечение данных из столбца Математика
  math_points <- cl_data$Математика
  
  # Вычисление статистических характеристик
  math_points_mean <- mean(math_points)
  math_points_var <- var(math_points)
  math_points_sd <- sd(math_points)
  math_points_quantile <- quantile(math_points)
  
  # Вывод результатов
  cat("\n")
  cat("Среднее выборочное:", math_points_mean, "\n")
  cat("Выборочная дисперсия:", math_points_var, "\n")
  cat("Среднеквадратическое отклонение:", math_points_sd, "\n")
  cat("Квартили:", math_points_quantile, "\n")
  
  # Построение гистограммы
  hist(math_points, main = "Гистограмма баллов по математике", xlab = "Баллы", ylab = "Частота", col = "lightblue", border = "black")
  
  
  
  
  
  # Задание 6
  
 
  
  # Определение количества наблюдений
  n <- length(math_points)
  
  # Расчет количества интервалов по формуле Стэрджесса
  k <- 1 + floor(log2(n))
  
  # Создание интервалов
  intervals <- seq(min(math_points), max(math_points), length.out = k + 1)
  
  # Подсчет частот
  freq <- hist(math_points, breaks = intervals, plot = FALSE)$counts
  
  # Вывод результатов
  cat("\n")
  cat("Количество интервалов:", k, "\n")
  cat("Интервалы:", intervals, "\n")
  cat("Частоты:", freq, "\n")
  
} else {
  cat("Файл 'data.csv' не найден по указанному пути.\n")
}