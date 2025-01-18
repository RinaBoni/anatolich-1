
# Лабораторная 1

setwd("C:/study/anatolich-1/R_labs/R_lab1/Workdir")

# Задание 4
# Создание таблицы данных
data <- data.frame(
  Фамилия = c("Иванов", "Петрова", "Сидорова", "Потерянная"),
  Возраст = c(21, 25, 22, NA),
  Пол = c("М", "Ж", "Ж", "Ж"),
  stringsAsFactors = FALSE
)
cat("\nтаблица\n")
# Вывод таблицы данных
print(data)
cat("\n")

# Задание 5

cat("\nа) второй столбец, пользуясь номером столбца;\n")
print(data[[2]])

cat("\nб) вторую строку, пользуясь номером строки;\n")
print(data[2, ])

cat("\nв) второй столбец, пользуясь его именем;\n")
print(data$Возраст)

cat("\nг) столбцы со второго по третий;\n")
print(data[ , 2:3])

cat("\nд) строки со второй по третью;\n")
print(data[2:3, ])

cat("\nе) возраст Сидоровой.\n")
print(data[data$Фамилия == "Сидорова", "Возраст"])
cat("\n")

# Задание 6

cat("\nОчистите таблицу от строк, содержащих NA\n")
cleaned_data <- data[complete.cases(data), ]
print(cleaned_data)

# Задание 7
#Экспортируйте очищенную таблицу данных в текстовый файл
write.table(data, file = "cleaned_data.txt", row.names = FALSE, col.names = TRUE, sep = "\t", quote = FALSE)

# Задание 8
#Экспортируйте очищенную таблицу данных в csv-файл
write.csv(cleaned_data, file = "cleaned_data.csv", row.names = FALSE)
write.table(cleaned_data, file = "cleaned_data_semicolon.csv", row.names = FALSE, col.names = TRUE, sep = ";", quote = FALSE)



