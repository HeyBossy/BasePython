В FastAPI **точка** (или **эндпойнт**) — это URL-адрес, по которому ваше приложение принимает запросы и отправляет ответы. Проще говоря, это адрес, по которому пользователи или другие приложения могут взаимодействовать с вашим API.

### Основные моменты о точках в FastAPI:

1. **Определение**: Точка — это часть URL, которая указывает на определённый ресурс или действие в вашем приложении. Например, в URL `http://example.com/items/1` точка будет `/items/1`.

2. **Методы HTTP**: Каждая точка может обрабатывать различные HTTP-методы, такие как `GET`, `POST`, `PUT`, `DELETE` и другие. Например:
   - `@app.get("/items/{item_id}")` — это точка, которая обрабатывает запросы на получение информации о конкретном элементе.
   - `@app.post("/items/")` — это точка для создания нового элемента.

3. **Декораторы**: В FastAPI точки определяются с помощью декораторов, которые указывают, какой метод HTTP будет использоваться для данной точки. Например:
   ```python
   @app.get("/users/")
   async def read_users():
       return [{"username": "user1"}, {"username": "user2"}]
   ```

4. **Асинхронные функции**: FastAPI позволяет определять функции-обработчики запросов как асинхронные (с использованием `async def`), что позволяет обрабатывать запросы более эффективно.

5. **Параметры и валидация**: Вы можете добавлять параметры к точкам, которые FastAPI автоматически валидирует. Например:
   ```python
   @app.get("/items/{item_id}")
   async def read_item(item_id: int):
       return {"item_id": item_id}
   ```

### Пример

Вот простой пример приложения FastAPI с несколькими точками:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

@app.post("/items/")
async def create_item(item: dict):
    return {"item": item}
```

### Заключение

Таким образом, **точка** в FastAPI — это ключевой элемент вашего API, который определяет, как обрабатывать запросы и какие данные возвращать. Понимание того, как работают точки, помогает создавать эффективные и удобные API для пользователей и других приложений.

Citations:
[1] https://thecode.media/pishem-svoy-pervyy-api-c-pomoschyu-fastapi/
[2] https://fastapi.tiangolo.com/ru/tutorial/first-steps/
[3] https://pythonru.com/biblioteki/znakomstvo-s-fastapi
[4] https://www.piter.com/blog/fastapi-veb-razrabotka-na-python
[5] https://fastapi.tiangolo.com/ru/tutorial/path-params-numeric-validations/
[6] https://habr.com/ru/articles/799337/
[7] https://300.ya.ru/v_ZJ4iVoIS