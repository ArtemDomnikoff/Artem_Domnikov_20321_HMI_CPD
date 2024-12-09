import { PrismaClient } from "@prisma/client";
import NewsCard from "@components/NewCard";

const prisma = new PrismaClient();

export default async function HomePage() {
  const news = await prisma.news.findMany({ orderBy: { date: "desc" } });

  return (
    <div className="container mx-auto px-4 py-8">
      <h2 className="text-2xl font-bold mb-6">Новости</h2>
      <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-6">
        {news.map((item) => (
          <NewsCard 
            id={item.id} 
            title={item.title} 
            imageUrl={item.imageUrl || ''} 
            date={item.date} 
            description={item.description}
            />
        ))}
      </div>
    </div>
  );
}
