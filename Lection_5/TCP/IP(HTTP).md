# Виртуальное окружение
**Виртуальное окружение** в Python позволяет изолировать зависимости проекта, чтобы избежать конфликтов между различными версиями библиотек. Это особенно полезно, если у вас есть несколько проектов, которые требуют разные версии одной и той же библиотеки.

## Основные моменты о виртуальном окружении:
- Изоляция зависимостей:

Виртуальное окружение создаёт отдельное пространство для каждой группы зависимостей. Это значит, что изменения в одном проекте не затронут другие проекты.

- Это не виртуальная машина:

Виртуальное окружение не является полноценной виртуальной машиной. Оно использует ваш локальный Python интерпретатор и систему для управления зависимостями.

- Отличие от Docker:

Docker создаёт изолированные контейнеры для всего окружения, включая операционную систему. Виртуальное окружение работает только с Python-зависимостями.

- Локальность:

Оно привязано к текущему компьютеру и файлам проекта. Это облегчает управление версиями библиотек.

## Как создать виртуальное окружение
Используйте команду:

```
python3 -m venv env
```
Здесь:

1. python3 — команда для использования Python 3.
2. -m venv — встроенный модуль для создания виртуальных окружений.
3. env — имя создаваемого окружения (можете задать любое имя, например, venv).
## Активация виртуального окружения
После создания окружения его нужно активировать. Это делается разными командами в зависимости от операционной системы:

Для Linux/MacOS:
````
source env/bin/activate
````
Для Windows:
```cmd
env\Scripts\activate
```
После активации вы увидите, что в начале командной строки появилось имя окружения, например:
```(env) user@computer:~$```

## Установка зависимостей
После активации вы можете устанавливать библиотеки, например:

```
pip install flask
```
Эти зависимости будут доступны только внутри текущего виртуального окружения.

## Деактивация виртуального окружения
Чтобы выйти из окружения, выполните команду:

```deactivate```