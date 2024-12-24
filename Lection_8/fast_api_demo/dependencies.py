from fastapi import FastAPI, HTTPException, Depends, Response  # Импортируем FastAPI и исключения, а также Depends для внедрения зависимостей
from sqlalchemy.ext.asyncio import ( AsyncSession)

try:
    from typing import Annotated
except ImportError:
    from typing_extensions import Annotated

from .core.database import async_session
'''
Описание: Этот файл содержит функции для внедрения зависимостей, которые могут использоваться в различных обработчиках маршрутов. Зачем нужен:

    Получение сессии базы данных: Определяется функция get_session(), которая открывает асинхронную сессию для работы с базой данных.
    Упрощение кода: Использование зависимости позволяет избежать дублирования кода и упрощает управление ресурсами.

'''
async def get_session() -> AsyncSession:
    """Функция для получения асинхронной сессии базы данных."""
    async with async_session() as session:  # Открываем асинхронную сессию
        yield session  # Возвращаем сессию для использования в обработчиках

SessiobDep = Annotated[AsyncSession, Depends(get_session)] #создали одну готовую аннтоцию чтобы не прописывать заново создание асинхронную сессии
