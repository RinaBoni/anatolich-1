
# Лабораторная 3

setwd("C:/study/anatolich-1/R_labs/R_lab3/Workdir")

# Задание 3

# Сохранение в формате .jpg
jpeg(file = "clock_face.jpg", width = 800, height = 800)

# Настройка графики
plot(1, type = "n", xlab = "", ylab = "", xlim = c(-1.5, 1.5), ylim = c(-1.5, 1.5), axes = FALSE, xaxs = "i", yaxs = "i")
symbols(0, 0, circles = 1, inches = FALSE, add = TRUE, bg = "lightblue")

# Добавление меток часов
for (i in 1:12) {
  angle <- (i / 12) * 2 * pi
  x <- cos(angle)
  y <- sin(angle)
  text(x * 1.1, y * 1.1, labels = i, cex = 2, col = "black")
}

# Закрытие графического устройства
dev.off()

# Сохранение в формате .pdf с русскоязычными шрифтами
pdf(file = "clock_face.pdf", family = "NimbusSan", encoding = "CP1251.enc", width = 8, height = 8)

# Настройка графики
plot(1, type = "n", xlab = "", ylab = "", xlim = c(-1.5, 1.5), ylim = c(-1.5, 1.5), axes = FALSE, xaxs = "i", yaxs = "i")
symbols(0, 0, circles = 1, inches = FALSE, add = TRUE, bg = "lightblue")

# Добавление меток часов
for (i in 1:12) {
  angle <- (i / 12) * 2 * pi
  x <- cos(angle)
  y <- sin(angle)
  text(x * 1.1, y * 1.1, labels = i, cex = 2, col = "black")
}

# Закрытие графического устройства
dev.off()

# Встраивание шрифтов в PDF
#embedFonts("clock_face.pdf")