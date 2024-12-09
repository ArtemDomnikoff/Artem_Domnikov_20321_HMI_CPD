import Link from "next/link";

interface NewsCardProps {
  id: number;
  title: string;
  imageUrl?: string;
  date: Date;
  description: string;
}

const NewsCard: React.FC<NewsCardProps> = ({ id, title, imageUrl, date , description}) => (
  <div className="bg-white rounded-lg shadow-md overflow-hidden hover:shadow-lg transition-shadow duration-200">
        {imageUrl && <img src={imageUrl} alt={title} className="w-full h-48 object-cover" />}
        <div className="p-4">
        <Link href={`/news/${id}`}>
          <h3 className="text-xl font-semibold text-gray-800 mb-2">{title}</h3>
        </Link>
        <p className="text-gray-400 text-xs mb-4">{new Date(date).toLocaleDateString()}</p>
        </div>
      
  </div>
);

export default NewsCard;
