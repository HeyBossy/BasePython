import pathlib
from concurrent.futures import ThreadPoolExecutor
from queue import Queue
import os
from contextlib import suppress


class SearchFile:
    def __init__(self, directory: str, search_string: str):
        self.results_queue = Queue()
        self.directory = pathlib.Path(directory)
        self.search_string = search_string

    def search_in_file(self, file_path: str) -> None:
        """
        Поиск строки в файле и добавление результатов в очередь.
        """
        with suppress(FileNotFoundError, UnicodeDecodeError):
            with open(file_path, 'r', encoding='utf-8') as file:
                for line_num, line in enumerate(file, start=1):
                    if self.search_string.lower() in line.lower():
                        self.results_queue.put((line_num, file_path, line.strip()))

    def collect_files(self) -> list:
        """
        Собирает все файлы из директории и возвращает список путей.
        """
        return [file_path for file_path in self.directory.rglob('*') if file_path.is_file()]

    def start_search(self):
        """
        Запускает многопоточный поиск через ThreadPoolExecutor.
        """
        if not self.directory.is_dir():
            print("Путь не валидный.")
            return

        files = self.collect_files()
        print(f'Количество потоков: {os.cpu_count()}\n')
        with ThreadPoolExecutor(max_workers=os.cpu_count()) as executor:
            for file_path in files:
                executor.submit(self.search_in_file, file_path)

        # Выводим результаты
        while not self.results_queue.empty():
            line_num, file_path, line = self.results_queue.get()
            print(f"[{line_num}]: {file_path}\n  {line}")


if __name__ == "__main__":
    print("Введите путь к директории:")
    directory = input().strip()
    print("Введите искомую подстроку:")
    search_string = input().strip()

    searcher = SearchFile(directory, search_string)
    searcher.start_search()
