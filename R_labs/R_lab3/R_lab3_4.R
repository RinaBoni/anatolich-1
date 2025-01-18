
# Лабораторная 3

setwd("C:/study/anatolich-1/R_labs/R_lab3/Workdir")

# Задание 4

# Проверка существования файла
if (file.exists("data.csv")) {
  # Чтение данных
  data <- read.table("data.csv", header = TRUE, sep = ";")
  
  # Очистка данных от NA
  cl_data <- na.omit(data)
  
  # Проверка на наличие некорректных значений
  if (any(is.na(cl_data$Русский_язык))) {
    cat("В столбце 'Русский язык' есть некорректные значения.\n")
  } else {
    # Преобразование столбцов в числовой формат
    cl_data$Математика <- as.numeric(as.character(cl_data$Математика))
    cl_data$Русский_язык <- as.numeric(as.character(cl_data$Русский_язык))
    cl_data$Обществознание <- as.numeric(as.character(cl_data$Обществознание))
    
    # Установка графического окна для 3 гистограмм
    par(mfrow = c(3, 1))  # 3 строки, 1 столбец
    
    # Гистограмма по математике
    hist(cl_data$Математика, main = "Гистограмма оценок по математике", xlab = "Оценки", col = "lightblue", border = "black")
    
    # Гистограмма по русскому языку
    hist(cl_data$Русский_язык, main = "Гистограмма оценок по русскому языку", xlab = "Оценки", col = "lightgreen", border = "black")
    
    # Гистограмма по обществознанию
    hist(cl_data$Обществознание, main = "Гистограмма оценок по обществознанию", xlab = "Оценки", col = "lightcoral", border = "black")
  }
} else {
  cat("Файл 'data.csv' не найден по указанному пути.\n")
}