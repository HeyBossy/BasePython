# sudo apt install python3-venv
#python3 -m venv env - в убунту
#. ./env/bin/activate - в убунту
#  pip install sqlalchemy -  скл алхимия

import sqlalchemy as sa
from sqlalchemy.orm import (DeclarativeBase,
     Mapped,
     mapped_column,
    sessionmaker)

from sqlalchemy import String, Text

# базовый класс для наследования БД
class Base(DeclarativeBase):
	    pass

# обязательно наследование Base
class Product(Base):
    __tablename__ = 'product' # имя БД __имя БД__

     # колонки (обязательно писать  аннотации!!Mapped)
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(500)) # 500 символов
    description: Mapped[str] = mapped_column(Text)
    price: Mapped[float]

print('=====================================')
print('Смотрим схему\n')
print(repr(Product.__table__)) #смотрим класс и колонки


#Engine — управляет подключением к базе данных и выполняет SQL-запросы.
# делаем диалект sqlite
#echo=True - смотрим все запросы в консоле к серверу
#Фактическое соединение с сервером происходит только в момент выполнения запроса
engine = sa.create_engine('sqlite://', echo=True)

#Этот метод проверяет, какие таблицы определены в метаданных
# (то есть в классах, которые наследуют от Base),
# и создает их в базе данных, если они еще не существуют.
print('================================')
print('Смотрим Метадату \n')
Base.metadata.create_all(engine)

print('================================')
print('Создаем объект на основе бд и заплняем данные \n')
cpu = Product(
    # айди автоматом генерируется но он None
    title='i7 7700k',
    description='Intel CPU',
    price=29290.99,
)
print(cpu)

print('================================')
print('Создаем сессию \n')
# чтобы делать любые действия с БД
Session = sessionmaker(bind=engine)

with Session() as session: # контексный менеджер - чтобы закрыть сессию
    session.add(cpu) # эти новые сущности добавить в бд
    session.commit() # сохранить изменения в сессии

print('================================')
print('Смотрим стркои по праймери кей \n')
with Session() as session:
    print(session.get(Product, 666)) # None - нет этого ключа
    print(session.get(Product, 1))

print('================================')
print('Смотрим  селект\n')
with Session() as session:
     stmt = sa.select(Product).where(Product.description == 'Intel CPU')
     results = session.scalars(stmt) # выполнить выражение stmt и вернуть результаты в виде скаляров
     print(results.all()) # возвращает список всех сущностей
