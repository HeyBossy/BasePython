"""Создадим доску объяалений с продожами (БД) через алхимию"""

from __future__ import annotations
from datetime import datetime

import sqlalchemy as sa
from sqlalchemy.orm import (relationship,
                            DeclarativeBase, Mapped, mapped_column)


# базовый класс
class Base(DeclarativeBase):
    pass


class Category(Base):
    """Категории объявления - таблица"""
    __tablename__ = 'category'  # имя таблицы в БД

    id: Mapped[int] = mapped_column(primary_key=True)  # праймери кей
    title: Mapped[str] = mapped_column(sa.String(100))

    # sql  двусторонние связи таблицами: Mapped[БД связанная] = relationship[обратная категория=колонка связанная]
    ads: Mapped[list[Ad]] = relationship(
        back_populates='category'
    ) # у объявления одна категория, а у категории список объявлений хранится


class Ad(Base):
    """Объявления на доске о продаже-таблица. Указываем категорию по объявлению"""
    __tablename__ = 'ad'

    id: Mapped[int] = mapped_column(primary_key=True)  # праймери кей
    title: Mapped[str] = mapped_column(sa.String(255))
    text: Mapped[str] = mapped_column(sa.Text())
    price: Mapped[float]
    addres: Mapped[str] = mapped_column(sa.Text(), default='')  # значение по умолчанию

    # внешние ключи
    id_category: Mapped[int] = mapped_column(
        sa.ForeignKey(
            'category.id'))  # onepdate -  если обновитс у Ad то и у катгеории обновится)  # внешний ключ (джойнимся по праймери кей  в таблице категории)
    user_id: Mapped[int] = mapped_column(
        sa.ForeignKey('user.id'))  # смотрим к какому пользователю принадлжеит

    # sql Alchemy relationship - двустороняя связь с таблицами
    category: Mapped[Category] = relationship(
        back_populates='ads') # у объявления одна категория, а у категории список объявлений хранится
    user: Mapped[User] = relationship(back_populates='ads') # у пользователя несколько объявлений


class User(Base):
    """Пользователи добавляют объявления"""
    __tablename__ = 'user'

    id: Mapped[int] = mapped_column(primary_key=True)  # праймери кей
    email: Mapped[str] = mapped_column(sa.String(100), unique=True)  # уникальная колонка
    is_admin: Mapped[bool] = mapped_column(default=False)  # суперпользователь
    display_name: Mapped[str] = mapped_column(sa.String(255),
                                              default='')
    password: Mapped[str] = mapped_column(sa.String(100))
    # sql Alchemy relationship - двустороняя связь с таблицами
    ads: Mapped[list[Ad]] = relationship(
        back_populates='user'
    )
