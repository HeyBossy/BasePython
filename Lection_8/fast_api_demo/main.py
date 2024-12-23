# Импортируем необходимые модули и классы
from __future__ import annotations  # Позволяет использовать аннотации типов, которые будут оценены позже
from contextlib import asynccontextmanager  # Асинхронный контекстный менеджер для управления ресурсами
import typing as t  # Импортируем модуль typing для работы с типами

from fastapi import FastAPI, HTTPException, Depends  # Импортируем FastAPI и исключения
from pydantic import BaseModel, Field  # Импортируем базовый класс для моделей и поле для валидации
import sqlalchemy as sa  # Импортируем SQLAlchemy для работы с базами данных
from sqlalchemy.ext.asyncio import (create_async_engine,
    async_sessionmaker, AsyncSession)
# Импортируем асинхронные функции SQLAlchemy
from doska_obyavleni import Base, Category  # Импортируем базовый класс и модель Category из модуля doska_obyavleni

# Создаем асинхронный движок для работы с SQLite
engine = create_async_engine('sqlite+aiosqlite:///./ad-board.sqlite')  # Указываем URL базы данных SQLite
async_session = async_sessionmaker(bind=engine, expire_on_commit=False)  # Создаем асинхронный сессионный менеджер

async def get_session():
    async with async_session() as session:
        yield session
@asynccontextmanager
async def lifespan(app: FastAPI):
    """Асинхронный контекстный менеджер для создания всех таблиц в базе данных"""
    async with engine.begin() as conn:  # Начинаем асинхронную транзакцию
        await conn.run_sync(Base.metadata.create_all)  # Создаем все таблицы из метаданных
    yield  # Возвращаем управление после создания таблиц
    await engine.dispose()  # Освобождаем ресурсы при завершении работы приложения


# Создаем экземпляр приложения FastAPI с заданным контекстом жизни
app = FastAPI(lifespan=lifespan)  # Инициализация приложения


@app.get('/categories')
async def read_all_categories(
        session: AsyncSession = Depends(get_session())):
    """Прочитать данные из БД и вернуть список категорий"""
    # нужна сессия чтоы прочитать данные
    stmt = sa.select(Category)  # Формируем SQL-запрос для выбора всех категорий
    result = await session.scalars(stmt)  # Выполняем запрос и получаем скаляры (значения)
    return result.all()  # Возвращаем все результаты


class CategoryIn(BaseModel):
    """Модель для входных данных категории"""
    title: str = Field(min_length=1, max_length=100)  # Поле title с минимальной и максимальной длиной


class CategoryOut(CategoryIn):
    """Модель для выходных данных категории (с ID)"""
    id: int  # Поле id для идентификации категории


@app.post('/categories', response_model=CategoryOut, status_code=201)
async def create_category(payload: CategoryIn) -> Category:
    """Создание новой категории"""
    category = Category(title=payload.title)  # Создаем новый объект категории на основе входных данных
    async with async_session() as session:  # Открываем асинхронную сессию
        session.add(category)  # Добавляем новую категорию в сессию
        await session.commit()  # Сохраняем изменения в базе данных
    return category  # Возвращаем созданную категорию
