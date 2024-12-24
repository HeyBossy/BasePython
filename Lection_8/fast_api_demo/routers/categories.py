from fastapi import APIRouter, HTTPException, Depends, Response  # Импортируем необходимые классы из FastAPI
from sqlalchemy.ext.asyncio import AsyncSession  # Импортируем AsyncSession
import sqlalchemy as sa  # Импортируем SQLAlchemy для выполнения запросов
from ..dependencies import SessiobDep, get_session # Импортируем созданную зависимость для работы с сессией
from ..schemes import CategoryIn, CategoryOut  # Импортируем схемы для валидации данных
from ..doska_obyavleni import Category  # Импортируем модель Category

'''
Роутеры в FastAPI служат для организации и структурирования вашего кода, что делает его более удобным для разработки и поддержки. Вот несколько ключевых причин, почему стоит использовать роутеры:

    Разделение логики: Роутеры позволяют разделить обработку запросов на разные части приложения. Например, вы можете создать отдельные роутеры для пользователей, товаров, заказов и других сущностей. Это делает код более организованным и легким для понимания.
    Упрощение структуры: Использование роутеров помогает избежать перегруженности основного файла приложения. Вместо того чтобы помещать все маршруты в один файл, вы можете создать несколько файлов с роутерами и подключить их к основному приложению.
    Повторное использование: Роутеры можно легко переиспользовать в разных частях приложения или даже в разных проектах. Вы можете создать общий роутер для API и подключать его к разным приложениям.
    Поддержка версионирования API: С помощью роутеров можно легко управлять версиями вашего API. Например, вы можете создать один роутер для версии 1 (/api/v1/...) и другой для версии 2 (/api/v2/...).
    Группировка маршрутов: Роутеры позволяют группировать маршруты по определенным критериям, например, по функциональности или по типу ресурсов. Это упрощает навигацию по коду и делает его более структурированным.

Этот файл содержит роутер для обработки запросов, связанных с категориями. Зачем нужен:

'''

# APIRouter - чтобы сделать маршрутизацию
router = APIRouter(prefix='/categories')
@router.get('/')
async def read_all_categories(session: AsyncSession = Depends(get_session)):
    """Прочитать данные из БД и вернуть список категорий."""
    stmt = sa.select(Category)  # Формируем SQL-запрос для выбора всех категорий
    result = await session.scalars(stmt)  # Выполняем запрос и получаем скаляры (значения)
    return result.all()  # Возвращаем все результаты

@router.post('/', response_model=CategoryOut, status_code=201)
async def create_category(payload: CategoryIn, session: SessiobDep) -> Category:
    """Создание новой категории."""
    category = Category(title=payload.title)  # Создаем новый объект категории на основе входных данных
    session.add(category)
    await session.commit()
    return category  # Возвращаем созданную категорию

@router.get('/categories/{category_id}', response_model=CategoryOut) #фигурных скобках придумываем имя параметрка
async def read_category(categiry_id: int,
                        session: SessiobDep):
    """Читаем категорию по айди"""
    category =  await session.get(Category, categiry_id)
    if category is None:
       raise HTTPException(404, f'Category with ID {categiry_id} not found') #not found
    return category


@router.delete('/{category_id}', response_model=CategoryOut)
async def delete_category(category_id: int, session: SessiobDep):
    """Удаляет категорию по указанному ID."""

    category = await session.get(Category, category_id)

    if category is None:
        # Если категория не найдена, выбрасываем исключение
        raise HTTPException(status_code=404, detail=f'Category with ID {category_id} not found')  # not found

    await session.delete(category)  # Удаляем объект категории, а не класс
    await session.commit()  # Сохраняем изменения в базе данных
    print(f'Succes deleting id = {category_id}')  # Возвращаем удалённую категорию (можно вернуть просто сообщение)
    return Response(status_code=204)
