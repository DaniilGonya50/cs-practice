import numpy as np


hours = np.arange(0, 22, 3)
line = np.linspace(0, 1, 5)
zeroz = np.zeros(6, dtype=int)
unknown_table = np.full((2, 3), -1)
identity = np.eye(3)
print(f'hours - {hours}')
print(f'shape - {hours.shape}')
print(f'ndim - {hours.ndim}')
print(f'size - {hours.size}')
print(f'dtype - {hours.dtype}')

print(f'Третий элемент - {hours[2]}')
print(f'Последний элемент - {hours[-1]}')
print(f'Индексы 2-5 - {hours[2:6]}')
print(f'Каждый второй - {hours[::2]}')
print(f'Наоборот - {hours[::-1]}')
print()


temperatures = np.array([
    [12, 14, 13, 15],
    [11, 13, 16, 17],
    [10, 12, 15, 18],
])

print(f'temperatures: {temperatures}')
print(f'Форма: {temperatures.shape}')
print(f'Число измерений: {temperatures.ndim}')
print(f'Число элементов: {temperatures.size}')

print(f'Значение из второй строки и третьего столбца: {temperatures[1, 2]}')
print(f'Первая строка: {temperatures[0]}')
print(f'Последний столбец: {temperatures[:, -1]}')
print(f'Первые две строки без первого столбца: {temperatures[:2, 1:]}')
print(f'Центральный фрагмент 2х2: {temperatures[0:2, 1:3]}')
print()

matrix = np.arange(1,26).reshape(5,5)
print(f'Матрица {matrix}')
print(f'Первые три строки: {matrix[:3]}')
print(f'shape: {matrix[:3].shape}')

print(f'Последние две строки: {matrix[-2:]}')
print(f'shape: {matrix[-2:].shape}')

print(f'Первые два столбца: {matrix[:, :2]}')
print(f'shape: {matrix[:, :2].shape}')

print(f'Фрагмент (строки 1-3, столбцы 2-4): {matrix[1:4, 2:5]}')
print(f'shape: {matrix[1:4, 2:5].shape}')

print(f'Угловой блок 2х2 в правом нижнем углу: {matrix[-2:, -2:]}')
print(f'shape: {matrix[-2:, -2:].shape}')

changed_hours = hours.copy()
changed_hours[2:5] = 99
changed_hours[1::2] = -1
print("changed_hours:", changed_hours)
print("hours (исходный):", hours)
print()

changed_matrix = matrix.copy()
changed_matrix[1] = 0
changed_matrix[:, -1] = -1
changed_matrix[1:4, 1:4] = 100
print("changed_matrix:", changed_matrix)
print("matrix (исходная):", matrix)
print()

numbers = np.arange(0, 12)
table = numbers.reshape(3, 4)
transposed = table.T

print("numbers:", numbers)
print("shape numbers:", numbers.shape)
print()
print("table:\n", table)
print("shape table:", table.shape)
print()
print("transposed:\n", transposed)
print("shape transposed:", transposed.shape)
print()
