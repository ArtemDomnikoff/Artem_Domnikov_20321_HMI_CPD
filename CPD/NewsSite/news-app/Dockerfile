# Используем официальный образ Node.js
FROM node:latest
# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем package.json и package-lock.json
COPY package*.json ./

COPY prisma ./prisma/
# Устанавливаем зависимости
RUN npm install

# Копируем все файлы проекта
COPY . .

# Собираем проект
RUN npm run build

# Откры порт для Next.js
EXPOSE 3000

# Запускаем приложение
CMD ["npm", "start"]
