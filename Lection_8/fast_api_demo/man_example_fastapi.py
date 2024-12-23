# python -m venv env - создать виртуальное окружение


# .\env\Scripts\activate - Активирует виртуальное окружение `env` (работает на Windows).
# source env/bin/activate - убунту актвиация

# deactivate -  выключить

# pip install "fastapi[standard]" - установить фастапи (всегда с  venv)

# fastapi dev main.py - запустить сервак (dev -  в режиме разработки запускать)

# http://127.0.0.1:8000/docs - документация нашего фастапи там видны методы!
from __future__ import annotations
import typing as t

from fastapi import FastAPI, HTTPException
from pydantic import \
    BaseModel  # типо dataclass для описания данных но круче может автоматом вызывать ошибки если тип данных не верный + с фастапи работает

app = FastAPI()  # наше приложение


class Note(BaseModel):
    # Определяем модель данных `Note`:
    # - `id`: уникальный идентификатор заметки (целое число).
    # - `text`: текст заметки (строка).
    # Pydantic автоматически проверяет и валидирует входные данные, соответствующие этим полям.
    id: int
    text: str


def generate_fake_data(n):
    '''  Возвращаем пару `(id, note - заметка)`.'''
    for i in range(1, n + 1):  # Создаём диапазон от 1 до n включительно.
        note = Note(id=i, text=f'Note #{i}')
        # Создаём объект `Note` с уникальным `id` и текстом `Note #i`.
        yield note.id, note


fake_db_data = dict(generate_fake_data(5))  # Генерируем фейковую базу данных на 5 записей
# и преобразуем данные из генератора в словарь,
# где ключ — это `id`, а значение — текст с `Note

# точка - endpoint  в фастапи(функция)
@app.get('/')  # Маршрут для HTTP GET-запроса по адресу `/`.
def read_all_notes() -> t.List[Note]:
    '''Функция возвращает список всех заметок из базы данных.'''
    return list(fake_db_data.values())  # Извлекаем все значения (объекты `Note`) из словаря и преобразуем их в список.


# Когда вы сделаете запрос к URL, например http://127.0.0.1:8000/5,
# значение 5 будет передано в функцию read_note как аргумент
# note_id.
@app.get('/{note_id}')  # Маршрут для HTTP GET-запроса с параметром `note_id`, например `/3`.
def read_note(note_id: int) -> Note:
    # Функция принимает параметр `note_id` (идентификатор заметки) и возвращает соответствующую заметку.
    '''
    curl 127.0.0.1:8000/3 - Вернёт заметку с id=3.
    Если указать, например, 10, и такой заметки нет (до 5 создавали), будет ошибка 404.
    '''
    if note_id not in fake_db_data:
        # Если `note_id` нет в базе данных:
        raise HTTPException(404,
                            f'Note with id {note_id} not found')  # Возбуждаем исключение HTTP 404 (Not Found) с сообщением об ошибке.
    return fake_db_data[note_id]  # Если заметка найдена, возвращаем её.


#передать данные на сервер
@app.post('/')
def create_note(payload: Note) -> Note: # данные тело запроса (объект джсон)
    fake_db_data[payload.id] = payload
    return payload

