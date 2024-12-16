import math
import threading
from queue import Queue  # безопасная очередь (в нее писать/читать в многопоточном режиме)
import timeit
import os

def is_prime_number(n: int) -> bool:
    """Возвращает истину, если число простое, иначе ложь."""
    if n < 2:
        return False
    if n == 2 or n == 5:
        return True
    if n % 2 == 0:
        return False

    sqrt_n = int(math.sqrt(n))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True


def multi_thread_naive(n: int) -> list:
    ''' плохой пример - выводим простые числа. чем больше аргумент тем больше потоков - плохо'''
    threads = []
    results = Queue()  # В многопоточных лучше очереди

    def worker(i):
        if is_prime_number(i):
            results.put(i)

    for i in range(1, n + 1):
        # Thread - многопоточный - сами запускаем и останавливаем
        thread = threading.Thread(target=worker, args=(i,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()  # используется для ожидания завершения конкретного потока

    return sorted((results.queue))


# Пример использования
print('плохой метод:')
primes = multi_thread_naive(10)
print(primes)


def multi_thread_better(n: int, max_threads: int) -> list:
    '''лучше метод! Ограничиваем кол-во потоков и переиспользуем'''
    results = Queue()
    tasks = Queue()  # очередь задач тчобы выполнять их в потоке

    def worker():
        '''заьбирает данные из очереди. 1 итерация - 1 задача'''
        while 1:
            i = tasks.get()  # put - кладем в очредеь а  get - забираем

            # остановка потока (заполнена очередь и далее в нее данные не поступают)
            if i is None:  # в начале она пустая но  это не None
                break

            if is_prime_number(i):
                results.put(i)

            tasks.task_done()   # Уведомление о завершении задачи

    threads = []  # potoki
    for _ in range(max_threads):  # _ не нужно значение данного аргумента просто хотим сделать фор сколько потоков
        thread = threading.Thread(target=worker)
        threads.append(thread)
        thread.start()

    for i in range(1, n + 1):
        tasks.put(i)  # очередь заполнена

    tasks.join()  # ждем когда в очереди задачи закончаться

    # все цифры закончены - потоки отработали - кладем  None на все потоки..
    for _ in range(max_threads):
        tasks.put(None)

    for thread in threads:
        thread.join()  # используется для ожидания завершения конкретного потока

    return sorted((results.queue))

print('хороший метод:')
max_thread = os.cpu_count()
print(f'max_thread: {max_thread}')
primes = multi_thread_better(10, max_thread)
print(primes)
