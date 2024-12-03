from uuid import uuid4, UUID


class BankError(Exception):
    """Базовый класс для ошибок банка. Сюда мессенджи"""
    pass


class LowBalanceError(BankError):
    """Ошибка низкого баланса."""

    def __init__(self, bill, amount):
        self.bill = bill  # Сохраняем объект счета
        self.amount = amount  # Сохраняем сумму, которую нужно списать
        #init  BankError
        super().__init__(f'Низкий баланс для счета {bill.id}: {bill.balance} '
                         f'нужно {amount}')

class MissingBillsError(BankError):
    def __int__(self, bill_id):
        super.__init__(f'Счет с айди {bill_id} не найден')

class Bill:
    """Счет в банке."""

    def __init__(self, client, balance=0):
        if balance < 0:
            raise ValueError('Баланс не может быть отрицательным')
        self.id = uuid4()  # Уникальный идентификатор счёта
        self.client = client  # Клиент, которому принадлежит счёт
        self.balance = balance  # Баланс счёта

    def deposit(self, amount):
        """Зачисляем средства на счет."""
        if amount <= 0:
            raise ValueError('Депозит должен быть позитивным')  # Бросить исключение
        self.balance += amount  # Увеличиваем баланс

    def spisanie(self, amount):
        """Списываем средства со счета."""
        if amount <= 0:
            raise ValueError('Списание должно быть позитивным')  # Бросить исключение

        if self.balance < amount:
            raise LowBalanceError(self, amount)  # Передаём текущий счёт и сумму
        self.balance -= amount  # Уменьшаем баланс


class BankClient:
    """Клиент банка."""

    def __init__(self, client_id, firstname, lastname):
        self.client_id = client_id
        self.firstname = firstname
        self.lastname = lastname
        self.bills: dict[UUID, Bill] = {}  # Словарь из ID: счета

    def add_bill(self, bill: Bill):
        """Добавить счет клиента."""
        if self.has_bill(bill.id):  # Возвращает True или False
            raise ValueError(f'Счет {bill.id} с указанным ID уже есть у клиента')
        # bill.id -  id переменная класса Bill
        self.bills[bill.id] = bill

    def get_bill(self, bill_id: UUID) -> Bill:
        """По номеру счета найти сам счет."""
        if not self.has_bill(bill_id):  # Возвращает True или False
            raise ValueError(f'Счет {bill_id} с указанным ID не найден')
        return self.bills[bill_id]

    def has_bill(self, bill_id: UUID) -> bool:
        """По номеру счета узнать принадлежит ли он клиенту."""
        return bill_id in self.bills


class Bank:
    """Сам банк."""
    def __init__(self):
        # Словарь для хранения клиентов
        self.clients: dict[UUID, BankClient] = {}

    def create_client(self, firstname: str, lastname: str) -> BankClient:
        """Создаем клиента и добавляем его в банк."""
        new_client = BankClient(uuid4(), firstname, lastname)  # Создаём нового клиента
        self.clients[new_client.client_id] = new_client  # Сохраняем клиента в словаре
        return new_client  # Возвращаем созданного клиента

    def open_account(self, client: BankClient, balance: float = 0) -> Bill:
        """Открываем аккаунт для клиента с заданным балансом."""
        if client.client_id not in self.clients:
            raise ValueError(f'Клиент с ID {client.client_id} не найден.')

        new_bill = Bill(client=client, balance=balance)  # это экземпляр (объект) класса Bill, который содержит информацию о счёте, включая его уникальный идентификатор (id), клиента (client) и баланс (balance).
        client.add_bill(new_bill)  # Добавляем счёт клиенту
        return new_bill  # Возвращаем созданный счёт

    def find_bill_by_id(self, bill_id: UUID) -> Bill:
        """Найти номер счета в банке по его ID."""
        # self.clients - значения там это класс!
        for client in self.clients.values():  # Проходим по всем клиентам банка
            if client.has_bill(bill_id):  # Проверяем наличие счёта у клиента
                return client.get_bill(bill_id)  # Возвращаем найденный счёт

        raise MissingBillsError(bill_id)  # Если не нашли счёт, выбрасываем ошибку

    def transfer(self, sender_account: UUID, recipient_account: UUID, amount: float):
        """Переводим средства с одного счета на другой."""

        sender_bill = self.find_bill_by_id(sender_account)  # Находим счёт отправителя
        recipient_bill = self.find_bill_by_id(recipient_account)  # Находим счёт получателя

        sender_bill.spisanie(amount)  # Списываем сумму со счёта отправителя
        recipient_bill.deposit(amount)  # Зачисляем сумму на счёт получателя




if __name__ == "__main__":
    client = BankClient(client_id=1, firstname="Иван", lastname="Иванов")
    bill = Bill(client=client, balance=100)  # Создаём счёт с балансом 100
    client.add_bill(bill)  # Добавляем счёт клиенту (словарь)

    print(f'Баланс счета: {bill.balance}')  # Вывод: Баланс счета: 100

    try:
        bill.spisanie(150)  # Пытаемся списать больше, чем на счёте
    except LowBalanceError as e:
        print (e.bill, e.amount)  # Выводит сообщение об ошибке низкого баланса
