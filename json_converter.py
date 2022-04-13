import json
import os

from typing import Any
from config import settings
from parser import parse_main

path_old = settings['path_old']
path_total = settings['path_total']


def write_json_file(obj: Any, path: str):
    """ Процедура записывает в файл 'path' любой object. В нашем случае будет записываться массив 'data'. """
    folder, _ = os.path.split(path)
    if folder:
        os.makedirs(folder, exist_ok=True)
    with open(path, mode="w", encoding="utf-8") as json_file:
        json.dump(obj, json_file, indent=4)
        print(f'File {path} has been written')


def read_json_file(path: str) -> dict[str, Any]:
    """ Функция читает файл 'path'. В нашем случае будет возвращать массив, записанный в файл 'path', однако может
    возвращаться и любой другой object, например словарь. """
    if not os.path.exists(path):
        return {}
    with open(path, encoding="utf-8") as json_file:
        return json.load(json_file)
