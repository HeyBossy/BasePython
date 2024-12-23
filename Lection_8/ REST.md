# Что такое REST?

**Веб-сервис** - это веб-приложение, предоставляющее ресурсы или функции через API, предназначенный для
взаимодействия между компьютерами

**Сервер API** - использует стандартные протоколы (HTTP/HTTPS) и форматы данных (JSON, XML)

Поэтому **клиент** и **сервер** могут быть реализованы на любом языке программирования

**REpresentational** **State Transfer** (передача состояния представления) - стиль архитектуры ПО для
распределенных систем (например, World Wide Web), который
может быть использован для построения веб-
сервисов

Термин REST был введен в 2000 году Роем Филдингом, а сама архитектура описывается шестью
ограничениями

ГЛАГОЛОВ В ЮРЛЕ В РЕСТЕ НЕТ!!

# Методы протокола HTTP
• GET - запрашивает содержимое ресурса

• HEAD - запрашивает ресурс, но возвращает только заголовок

• POST - отправка данных запроса указанному ресурсу

• PUT - заменяет указанный ресурс данными запроса

• DELETE - удаляет указанный ресурс

• OPTIONS - используется для описания параметров соединения с ресурсом (CORS)

• PATCH - используется для частичного изменения ресурса, для описания изменений в документе используется
формат JSON Patch

| Глагол | Коллекция                   | Элемент                       |
|--------|-----------------------------|-------------------------------|
| GET    | Получить все элементы       | Получить один элемент         |
| POST   | Добавить новый элемент      | -                             |
| PUT    | -                           | Заменить указанный элемент    |
| DELETE | Удалить все элементы        | Удалить один элемент          |

**тело запроса клиента всегда  JSON!**

# Что такое FastAPI и REST?
**FastAPI** — это современный веб-фреймворк для создания API на языке программирования Python. Он был разработан для упрощения и ускорения процесса разработки, обеспечивая высокую производительность и удобство использования. 

**REST (Representational State Transfer)** — это архитектурный стиль, который используется для создания веб-сервисов (как должен выглядеть сервис). Он основывается на использовании стандартных HTTP методов (таких как GET, POST, PUT, DELETE) для выполнения операций над ресурсами, представленными в виде URL.

Как они связаны?

    FastAPI как инструмент для REST: FastAPI позволяет разработчикам легко создавать RESTful API. Это значит, что вы можете использовать FastAPI для создания веб-приложений, которые следуют принципам REST, позволяя клиентам взаимодействовать с вашим приложением через стандартные HTTP запросы.
    HTTP методы: В REST используются различные HTTP методы:
        GET: Получить данные (например, список категорий).
        POST: Создать новый ресурс (например, добавить новую категорию).
        PUT: Обновить существующий ресурс.
        DELETE: Удалить ресурс.

Преимущества FastAPI

    Высокая производительность: FastAPI использует асинхронные функции, что позволяет обрабатывать множество запросов одновременно.
    Автоматическая документация: FastAPI автоматически генерирует интерактивную документацию для вашего API, что упрощает тестирование и понимание вашего приложения.
    Валидация данных: FastAPI проверяет входные данные на соответствие заданным типам и схемам, что уменьшает количество ошибок и повышает надежность приложения.

Пример использования


```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/categories")
async def read_categories():
    return [{"id": 1, "title": "Книги"}, {"id": 2, "title": "Электроника"}]

@app.post("/categories")
async def create_category(title: str):
    return {"id": 3, "title": title}
```
В этом примере:

    GET /categories возвращает список категорий.
    POST /categories создает новую категорию.

Заключение
FastAPI — это мощный инструмент для создания RESTful API на Python. Он сочетает в себе высокую производительность с простотой использования и автоматической документацией, что делает его отличным выбором для разработчиков.
 
**API** - взаимодествие с сервисом. Сервис просто отдает данные.