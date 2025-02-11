import { PrismaClient } from '@prisma/client';

const prisma = new PrismaClient();

async function main() {
  // Пример данных для начального наполнения
  const news = [
    {
      title: "Корабелка на Конгрессе молодых ученых",
      date: new Date(),
      imageUrl: "https://ds1.smtu.ru/files/sitenews/2024/12/06/small/1132.jpg?token_static=90dbf5de7f95d5f41917778a1d5b849c",
      description: "СПбГМТУ на Конгрессе молодых ученых представил экзоскелет для судостроения и судоходства. Это совместная разработка Передовой инженерной школы Корабелки и компании Ekzo Solutions. Благодаря упругому каркасу, который расположен вдоль спины, и дугам над плечами экзоскелет разгружает опорно-двигательный аппарат рабочего, занятого тяжелым физическим трудом. Использование экзоскелета позволяет снизить травматизм, сохранить работоспособность персонала и повысить производительность труда. Эта разработка уже применяется на нескольких судостроительных предприятиях. \n \n В деловой программе Конгресса молодых ученых приняли участие профессор кафедры океанотехники и морских технологий СПбГМТУ Дмитрий Никущенко и преподаватель кафедры международного права Людмила Егорова."
    },
    {
      title: "Представитель СПбГМТУ принял участие в Арктической вечеринке",
      date: new Date(),
      imageUrl: "https://ds1.smtu.ru/files/sitenews/2024/12/06/small/1131.jpg?token_static=087a3ec4b00d29cf642e8bf4e17ead23",
      description: "Ассистент кафедры теории корабля СПбГМТУ Забава Устинова для участников мероприятия провела квиз «Ледоколы».\n Викторина включала три раунда, в каждом – восемь вопросов. Они касались атомного ледокольного флота и освоения Арктики. \n \n Также гости Арктической вечеринки посмотрели фильм «Ледокол знаний», посвященный проекту «Росатома». А затем молодые люди – участники экспедиций на Северный полюс – рассказали слушателям свои впечатления и воспоминания от этого путешествия. Проект «Ледокол знаний» дает возможность талантливым школьникам и студентам со всей страны отправиться в Арктику на атомном ледоколе «50 лет Победы». Несколько лет назад участником одной из таких экспедиций стала и преподаватель Корабелки Забава Устинова.\n \n В 2024 году отмечается юбилей атомного ледокольного флота России. 3 декабря 1959 года вступило в строй первое в мире атомное гражданское надводное судно – ледокол «Ленин»."
    },
    {
      title: "В Корабелке создали модель телеуправляемого подводного металлоискателя",
      date: new Date(),
      imageUrl: "https://ds1.smtu.ru/files/sitenews/2024/12/06/small/1130.jpg?token_static=332aad1263d82a4978dad898b8675111",
      description: "Команда молодых ученых и студентов во главе с магистрантом ПИШ и факультета морского приборостроения СПбГМТУ Иваном Донецковым разработали универсальный подводный аппарат для поиска и исследования металлоконструкций на поверхности дна и в слое грунта. \n \n Аппарат может применяться в таких сферах, как подводная археология для поиска объектов, имеющих культурную и историческую ценность. «Сканер», как дополнительное оборудование, может использоваться в строительстве подводных коммуникаций: для контроля прокладки трубопроводов и силовых кабелей, анализа состояние трубопроводов, кабелей, добывающих установок. Без модуля металлоискателя аппарат способен работать как подводный дрон и проводить визуальный контроль опор мостов и портовых сооружений. «Сканер» может работать в соленой и пресной воде, глубина его погружения до 30 метров \n \n Управление аппаратом ведется оператором с судна обеспечения. При погружении в воду и приближении к дну раскладывается и включается модуль металлоискателя. В этот момент у оператора на компьютере отображаются показания, по которым и можно определить, есть или нет на дне металлические объекты. О приближении к ним можно судить по интенсивности сигнала, который поступает оператору с модуля металлоискателя. На аппарат также крепится видеокамера для более полного анализа обстановки. Как говорит Иван Донецков, преимущества «Сканера» в том, что на него можно устанавливать дополнительные модули для исследования толщи воды. «На отечественном и зарубежном рынках отсутствуют образцы техники в области подводного точечного поиска металлоконструкций с помощью подводного аппарата с модулем металлоискателя. Ряд компании выпускают подводные дроны только с видеокамерой для визуального контроля или с дополнительным модулем манипулятора», – рассказал студент СПбГМТУ. \n \n Разработка уже прошла испытания в реальных условиях в акватории Финского залива, а также предварительное тестирование систем в лабораторных условиях."
    },
    {
      title: "Помощник Президента РФ Николай Патрушев посетил СПбГМТУ",
      date: new Date(),
      imageUrl: "https://ds1.smtu.ru/files/sitenews/2024/12/04/small/1127.jpg?token_static=aaa080627e8fb5772d4cf2ff7bdc8b18",
      description: "4 декабря Помощник Президента России, председатель Морской коллегии РФ Николай Патрушев посетил Морской технический университет. \n \n Николай Патрушев проинспектировал ход строительства учебных, спортивных и жилых объектов на территории кампуса Корабелки. Сейчас подходит к концу возведение научно-производственного корпуса и ледовой арены, а также идет строительство студенческого общежития. \n \n В мероприятии приняли участие губернатор Санкт-Петербурга Александр Беглов, председатель Комитета по науке и высшей школе Андрей Максимов, ректор СПбГМТУ Глеб Туричин. \n \n В ходе визита в Петербург Помощник Президента РФ Николай Патрушев посетил Крыловский государственный научный центр, Государственный университет морского и речного флота имени адмирала С.О. Макарова, Средне-Невский судостроительный завод."
    },
    {
      title: "Участники Программы подготовки инженеров-корабелов ОСК приступили к работе на Адмиралтейских верфях",
      date: new Date(),
      imageUrl: "https://ds1.smtu.ru/files/sitenews/2024/12/04/small/1126.jpg?token_static=81d88d7ddaa95f5ecb1406da9dde1606",
      description: "Предприятие ОСК «Адмиралтейские верфи» приняло на работу первых участников Программы подготовки инженеров-корабелов ОСК, которая реализуется на базе СПбГМТУ. \n \n К работе на Адмиралтейских верфях приступили 15 студентов Корабелки, сообщает пресс-служба АО «Адмиралтейские верфи». Все ребята – выпускники колледжей, имеющие профессию сварщика, сборщика корпусов металлических судов, электромонтера или слесаря-монтажника. \n \n Программа подготовки инженеров-корабелов ОСК рассчитана на три года. За это время выпускники средних специальных учебных заведений получат высшее образование в СПбГМТУ на факультете кораблестроения и океанотехники. Образовательный процесс чередуется с работой на предприятии. Во время обучения ребята получают стипендию 30 тысяч рублей и заработную плату в соответствии с занимаемой штатной единицей за время трудовой деятельности. \n \n  «Программа подготовки инженеров-корабелов ОСК является пилотной для Адмиралтейских верфей, но несмотря на это, мы уже можем сказать, что проект оказался весьма востребован среди выпускников учебных заведений. А значит, он обязательно будет иметь продолжение», – отмечает начальник управления по работе с персоналом АО «Адмиралтейские верфи» Марина Кулагина. \n \n В СПбГМТУ в 2024/2025 году прошел первый набор на Программу подготовки инженеров-корабелов ОСК. В бакалавриате Корабелки по направлению 26.03.02 «Кораблестроение, океанотехника и системотехника» обучается 48 студентов. Они закреплены  за тремя предприятиями ОСК: Адмиралтейскими верфями, Балтийским заводом и Северной верфью. \n \n"
    },
    {
      title: "Итоги Всероссийского Акселератора в сфере судостроения и судоремонта",
      date: new Date(),
      imageUrl: "https://ds1.smtu.ru/files/sitenews/2024/12/03/small/1125.jpg?token_static=2d8e4aa26d47ec868c30d8ea3bbac8f6",
      description: "Завершился финальный этап Всероссийского Акселератора в сфере судостроения и судоремонта. Это совместный проект Технопарка Санкт-Петербурга и Центра трансфера технологий СПбГМТУ. \n \n Цель проекта – модернизация и технологическая трансформация отечественного судостроения и судоремонта, обеспечение трансфера технологий, внедрение инновационных решений и выход отрасли на самый современный технический и технологический уровень. \n \n Для участия в Акселераторе было подано 82 заявки из 25 регионов России и Казахстана. Эксперты отобрали 14 проектов, которые после прохождения акселерационной программы были адаптированы к реальным нуждам судостроительных компаний. \n \n Финалисты Акселератора презентовали представителям отрасли первые результаты работы. Некоторые из решений уже приняты к реализации производителями. Например, два проекта относятся к разработке инновационных материалов, повышающих износоустойчивость судна, его экологичность и другие параметры. Также эти материалы применимы для стратегически важного проекта России – освоения Арктики. Заказчики заинтересовались проектом беспилотного надводного аппарата «Нарвал» для обеспечения высококачественных океанических и атмосферных наблюдений. Этот дрон парусного типа функционирует и перемещается посредством ветряной и солнечной энергии. Доля отечественных комплектующих в его составе – более 70 %. Практический интерес вызвала система, позволяющая операторам специальной техники удаленно управлять работами с помощью автоматизированного рабочего места. Актуальна также разработка, внедрение которой позволит создать универсальные транспортные суда для перевозки различных видов энергоносителей. \n \n Награждение финалистов Акселерационной программы прошло в рамках Международного форума-выставки «Российский промышленник». Приветствовал участников генеральный директор Технопарка Санкт-Петербурга Олег Якимов, награждал победителей – заместитель генерального директора Российского морского регистра судоходства Алексей Березин. В торжественной церемонии приняли участие представители судостроительных компаний, в том числе АО «ОСК», ПАО «СЗ «Северная верфь», АО «СПМБМ «Малахит», АО «Кронштадтский морской завод»."
    },
  ];

  // Вставка данных в таблицу News
  for (const item of news) {
    await prisma.news.create({
      data: item,
    });
  }

  console.log("Seeding завершён!");
}

main()
  .catch((e) => {
    console.error(e);
    process.exit(1);
  })
  .finally(async () => {
    await prisma.$disconnect();
  });
