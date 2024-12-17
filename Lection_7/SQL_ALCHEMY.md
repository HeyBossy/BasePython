# Архитектура алхимии 
**SQLAlchemy** — это мощная библиотека для Python, предназначенная для работы с реляционными базами данных.

Основные характеристики SQLAlchemy

**ORM (Object-Relational Mapping):** траснялиця строк и столбцов БД в объекты питона

**Поддержка различных СУБД:** SQLAlchemy поддерживает множество реляционных баз данных, включая PostgreSQL, MySQL, SQLite, Oracle и Microsoft SQL Server. Это позволяет легко переключаться между различными СУБД без изменения кода приложения.
Два основных компонента:
- **SQLAlchemy ORM:** Этот компонент предоставляет высокоуровневый интерфейс для работы с базами данных через объекты и модели. Запросы формируются на языке Python.
- **SQLAlchemy Core:** Это низкоуровневый API, который позволяет работать напрямую с SQL. Он предоставляет более детальный контроль над запросами и структурой базы данных.

**Engine** — это центральный компонент, который управляет подключением к базе данных и выполняет SQL-запросы. Движок обеспечивает взаимодействие между вашим приложением на Python и реляционной базой данных, позволяя вам выполнять операции с данными
# Database Urls

Общий синтаксис:

```dialect+driver://username:password@host:port/database```

**SQLite** —  Бд в файле. Это легкая, встроенная реляционная система управления базами данных (СУБД)


    Диалекты: Типы баз данных, поддерживаемые SQLAlchemy.
    Драйвер: Библиотека, используемая для подключения к конкретной базе данных.
    URL: Строка подключения, содержащая информацию о том, как подключиться к базе данных.
    Пояснение: Описание каждого элемента в таблице и его значение.


| Диалекты    | Драйвер     | URL                                   | Пояснение                                              |
|-------------|-------------|---------------------------------------|-------------------------------------------------------|
| sqlite      | sqlite3    | sqlite:////tmp/foo.db                | Подключение к базе данных SQLite, где `foo.db` — имя файла базы данных. |
|             |             | sqlite://                            | URL для подключения к временной базе данных в памяти. |
|-------------|-------------|---------------------------------------|-------------------------------------------------------|
| mysql       | MySQLdb     | mysql://user:pswd@host:port/dbname  | Подключение к базе данных MySQL. `user` — имя пользователя, `pswd` — пароль, `host` — адрес сервера, `port` — порт, `dbname` — имя базы данных. |
|-------------|-------------|---------------------------------------|-------------------------------------------------------|
| postgresql  | psycopg2    | postgresql://user:pswd@host:port/dbname | Подключение к базе данных PostgreSQL. Параметры аналогичны MySQL. |
|-------------|-------------|---------------------------------------|-------------------------------------------------------|
| oracle      | cx_oracle   | oracle://user:pswd@host:port/dbname  | Подключение к базе данных Oracle. Параметры аналогичны предыдущим драйверам. |
|-------------|-------------|---------------------------------------|-------------------------------------------------------|
| mssql       | pyodbc      | mssql://user:pswd@host:port/dbname   | Подключение к Microsoft SQL Server. Параметры аналогичны предыдущим драйверам. |

# Engine | Соединение

``create_engine()`` - возвращает экземпляр Engine, который представляет основной интерфейс к базе данных, адаптированный согласно указанному диалекту, и обрабатывает детали базы данных и используемого DB-API

Фактическое соединение с сервером происходит только в момент выполнения запроса

	from sqlalchemy import create_engine
	 
	# Связывает пул и диалект вместе,
	# обеспечивая источник подключения и поведения базы данных
	engine = create_engine('sqlite://', echo=True)
	 
	# MySQL с драйвером pymysql
	engine = create_engine('mysql+pymysql://root:toor@localhost/demo', echo=True)

# Классический стиль

Для описания структуры базы данных, используют 3 основных класса:

    sqlalchemy.schema.Table - таблица
    sqlalchemy.schema.Column - поле таблицы
    sqlalchemy.schema.MetaData - список таблиц (метаданные)

А также типы полей описанные в модуле sqlalchemy.types
from sqlalchemy import MetaData, Table, Column, Integer, String, Text, Float
	 
	metadata = MetaData()
	 
	product = Table('product', metadata,
	    Column('id', Integer, primary_key=True),
	    Column('title', String(500), nullable=False),
	    Column('description', Text, nullable=False),
	    Column('price', Float, nullable=False),
	)

**первичный ключ**   - уникальный айди по которому получаем строку.

nullable - колонка не хранит None (если False)
# Декларативный стиль
Это типо ОРМ (строки и столбцы в объекты)

Каждый класс, представляющий таблицу в БД, должен наследоваться от базового класса:

	from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
	 
	class Base(DeclarativeBase):
	    pass

Для каждого класса, созданного с помощью декларативной системы, мы определим информацию о нашей таблице (метаданные таблицы):

	from sqlalchemy import String, Text
	 
    class Product(Base):
        __tablename__ = 'product' # имя БД __имя БД__
     
         # колонки
        id: Mapped[int] = mapped_column(primary_key=True)
        title: Mapped[str] = mapped_column(String(500))
        description: Mapped[str] = mapped_column(Text)
        price: Mapped[float]

Базовый класс Base, является более высокоуровневой абстракцией над sqlalchemy.schema.MetaData
# Метаданные

Объект, используемый SQLAlchemy для представления метаданных конкретной таблицы, в декларативной системе создается автоматически:

>>> Product.__table__
Table(
    'product', MetaData(),
    Column('id', Integer(), table=<product>, primary_key=True, nullable=False),
    Column('title', String(length=500), table=<product>, nullable=False),
    Column('description', Text(), table=<product>, nullable=False),
    Column('price', Float(), table=<product>, nullable=False),
    schema=None
)

Метаинформация о каждом классе-таблице хранится в атрибуте metadata базового класса Base

>>> Base.metadata
MetaData()

# Создание экземпляра

Создали Бд со схемой и теперь используем эту схему и создаем объекты и заполняем их данными

	cpu_7700k = Product(
	    title='i7 7700k',
	    description='Intel CPU',
	    price=29290.99,
	)
	 
	print('PK:', cpu_7700k.id)  # PK: None

Можно определить свой конструктор, если это необходимо 

# Создание сессии
любое взаимодествие через БД делается через сессию

Взаимодействие с БД осуществляется посредством объекта-сессии:

	from sqlalchemy.orm import sessionmaker
	 
	# 1. Определяем класс Session, который служит фабрикой для новых объектов сессий:
	Session = sessionmaker(bind=engine)
	 
	# 2. Используя ранее созданную фабрику, создаем новый экземпляр сессии
	with Session() as session:
	    session.add(cpu_7700k)
	    session.commit()

# Работа с экземпляром

    add(instance) - помещает объект в сессию, его состояние сохраняется в БД при следующей операции flush()
    add_all(instances) - поместить сразу много объектов в сессию
    delete(instance) - помечает объект как удаленный, удаление из БД выполнится после flush()

Объект может иметь следующие состояния:

    transient - только что создан и отсутствует в БД
    pending - добавлен в сессию, но отсутствует в БД
    persistent - присутствует в сессии и в БД
    deleted - помечен на удаление, но присутствует в БД
    detached - отсутствует в сессии

# Сохранение изменений в БД

- commit() - вносит изменения в БД и фиксирует транзакцию. Пока не закомитим в БД не будет изменений а в сессии может удалиться
- flush() - передает все ожидающие создания, обновления, удаления, операции в БД, которая поддерживает их как отложенные операции в транзакциях

# Транзакции
**Транзакция** — это логическая единица работы с базой данных, которая включает в себя одну или несколько операций. 

- begin() - начать транзакцию
- commit() - сохранить все изменения и зафиксировать транзакцию
- rollback() - отменить все изменения и откатить транзакцию


    with Session() as session:
	    session.begin()   
	    
        try:
	        ssd_drive = Product(title='SSD 1TB', description='Intel SSD', price=5999)
	        session.add(ssd_drive)
	    except:
	        session.rollback()
	        raise
	    else:
	        session.commit()

Можно сократить код с помощью менеджера контекста:

	with Session() as session, session.begin():
	    ssd_drive = Product(title='SSD 1TB', description='Intel SSD', price=5999)
	    session.add(ssd_drive)


# Выборка по первичному ключу

- .get(entity, ident) - возвращает сущность по первичному ключу, составной первичный ключ указывается как кортеж или словарь
- .get_one(entity, ident) - бросает исключение NoResultFound, если не найдено
```
	from sqlalchemy.exc import NoResultFound
	 
	# Возвращает None
	product = session.get(Product, 666)
	 
	try:
	    # Бросает исключение
	    product = session.get_one(Product, 666)
	except NoResultFound:
	    print('Product not found.')
```

# Выборка данных

- select(*entities) - представляет собой SQL выражение SELECT
- .execute(stmt) - выполнить выражение stmt и вернуть результат
 -    .scalars(stmt) - выполнить выражение stmt и вернуть результаты в виде скаляров
```
	from sqlalchemy import select
	 
	with Session() as session:
	    stmt = select(Product)
	    
	    for p in session.scalars(stmt):
	        print(f'{p.title} - {p.price}')
```
# Получение результатов

    .all() - возвращает список всех сущностей
    .first() - возвращает первую сущность, либо None, если пусто
    .one() - возвращает ровно одну сущность, бросает исключение NoResultFound если пусто, либо MultipleResultsFound если больше одной
    .one_or_none() - возвращает ровно одну сущность, либо None если пусто, либо бросает исключение MultipleResultsFound
    .scalar() - вызывает метод one() и в случае успеха возвращает первый столбец
	
# Identity Map

Гарантирует, что каждый объект загружается только один раз, сохраняя каждый загруженный объект в Map-е 	
	

	
	
	
	
	
	
	

