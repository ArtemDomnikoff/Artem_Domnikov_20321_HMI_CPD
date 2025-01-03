import { PrismaClient } from "@prisma/client";

const prisma = new PrismaClient();


export default async function NewsDetailsPage({params} : {params:any}) {
  await params; // Извлечение id из params
  // Получение данных из базы
  const newsItem = await prisma.news.findUnique({
    where: { id: parseInt(params.id, 10) }, // Преобразование id в число
  });


  // Если новость не найдена
  if (!newsItem) {
    return <div className="container mx-auto px-4 py-8">Новость не найдена</div>;
  }

  // Отображение данных
  return (
    <div className="container mx-auto px-4 py-8">
      <h1 className="w- flex-none mb-6 text-3xl leading-none text-slate-900">{newsItem.title}</h1>
      <h3 className="flex-auto text-lg font-medium text-slate-700">{newsItem.description}</h3>
      <div>
        {newsItem.imageUrl && (
        <img
          src={newsItem.imageUrl}
          alt={newsItem.title}
          className="w-full h-auto rounded mb-6"
        />
      )}
      </div>
      <p className="text-sm text-gray-500">
        Опубликовано: {new Date(newsItem.date).toLocaleDateString()}
      </p>
    </div>
  );
}
