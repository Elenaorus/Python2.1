import os

string = "C:/Elena/Desktop/GreekBrains/Python/HomeWork/Task1.py"

def fun(f_path: str) -> tuple:
    path, filename = os.path.split(f_path)
    name, extension = filename.split('.')
    return path, name, extension

print(f'Исходная строка: {string} \nКортеж из пути: {fun(string)}')
