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
