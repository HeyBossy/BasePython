# здесь все пайдентик модели
from pydantic import BaseModel, Field  # Импортируем базовый класс для моделей и поле для валидации

'''
 В этом файле определяются схемы данных, используемые в приложении. Зачем нужен:

    Валидация данных: С помощью Pydantic создаются модели (схемы), которые помогают валидировать данные, приходящие в запросах и отправляемые в ответах.
    Документирование API: FastAPI автоматически генерирует документацию на основе определенных схем, что делает API более понятным для пользователей.
'''
class CategoryIn(BaseModel):
    """Пользователь вводит данные."""
    title: str = Field(min_length=1, max_length=100)  # Поле title с минимальной и максимальной длиной

class CategoryOut(CategoryIn):
    """Пользователь получит в резльутате гет. Другой айди потому что пользователь
    может затереть айдишник (пользователь не может их менять! но другой айди может)"""
    id: int  # Поле id для идентификации категории