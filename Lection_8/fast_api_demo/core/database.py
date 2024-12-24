'''
тот файл отвечает за настройку подключения к базе данных. Зачем нужен:

    Создание движка базы данных: Определяется асинхронный движок SQLAlchemy для работы с SQLite.
    Создание сессионного менеджера: Определяется асинхронный сессионный менеджер, который позволяет выполнять запросы к базе данных.

'''
from sqlalchemy.ext.asyncio import (create_async_engine,
    async_sessionmaker)  # Импортируем асинхронные функции SQLAlchemy

# Создаем асинхронный движок для работы с SQLite
engine = create_async_engine('sqlite+aiosqlite:///./ad-board.sqlite')  # Указываем URL базы данных SQLite
async_session = async_sessionmaker(bind=engine, expire_on_commit=False)  # Создаем асинхронный сессионный менеджер чтобы делать запросы
