

setwd("C:/study/anatolich-1/R_labs/R_lab6/Workdir")

# Лвбораторная 6
cat('aa')
# Проверка существования файла
if (file.exists("связи.csv")) {
  
  # Задание 1: Загрузка данных из файла связи.csv
  # Укажите путь к файлу связи.csv
  file_path <- "связи.csv"
  
  # Загрузка данных
  data <- read.table(file_path, header = TRUE, sep = ";")
  #data <- read_csv2(file_path, col_names = c("x", "y"))
  
  # Преобразование данных: разделение значений по запятой и преобразование в числовой формат
  data$x <- as.numeric(gsub(",", ".", data$x))
  data$y <- as.numeric(gsub(",", ".", data$y))
  
  # Удаление строк с NA (если есть)
  data <- na.omit(data)
  
  # Вывод данных для проверки
  print("Загруженные данные:")
  print(data)
  
  # Вычисление коэффициентов корреляции
  cor_pearson <- cor(data$x, data$y, method = "pearson")
  cor_spearman <- cor(data$x, data$y, method = "spearman")
  cor_kendall <- cor(data$x, data$y, method = "kendall")
  
  # Проверка значимости коэффициентов корреляции
  test_pearson <- cor.test(data$x, data$y, method = "pearson")
  test_spearman <- cor.test(data$x, data$y, method = "spearman")
  test_kendall <- cor.test(data$x, data$y, method = "kendall")
  
  # Вывод результатов
  cat("Коэффициенты корреляции:\n")
  cat("Пирсон:", cor_pearson, "\n")
  cat("Спирмен:", cor_spearman, "\n")
  cat("Кендалл:", cor_kendall, "\n\n")
  
  cat("Результаты проверки значимости:\n")
  cat("Пирсон:\n")
  print(test_pearson)
  cat("Спирмен:\n")
  print(test_spearman)
  cat("Кендалл:\n")
  print(test_kendall)
  
  # Задание 2: Построение линейной модели регрессии
  linmod <- lm(y ~ x, data = data)
  
  # Суммарная информация по модели
  summary_info <- summary(linmod)
  cat("\nСуммарная информация по модели:\n")
  print(summary_info)
  
  # Количество объектов в модели
  num_objects <- length(linmod)
  cat("\nКоличество объектов в модели:", num_objects, "\n")
  
  # Визуализация линейной модели
  plot(data$x, data$y, main = "Линейная модель регрессии", xlab = "x", ylab = "y", pch = 19, col = "blue")
  abline(linmod, col = "red", lwd = 2)
  
  
} else {
  cat("Файл 'связи.csv' не найден по указанному пути.\n")
}