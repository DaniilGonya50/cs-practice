import numpy as np


def make_hours():
    """Создаёт список часов от 0 до 21 с шагом 3."""
    hours = np.arange(0, 22, 3)
    return hours.tolist()


def vector_report(values):
    """Возвращает информацию о векторе."""
    arr = np.array(values, dtype=float)

    return {
        "third": float(arr[2]),
        "last": float(arr[-1]),
        "middle": arr[2:6].tolist(),
        "every_second": arr[::2].tolist(),
        "reversed": arr[::-1].tolist()
    }


def change_vector(values):
    """Изменяет вектор, не затрагивая исходный список."""
    arr = np.array(values, dtype=float).copy()

    arr[2:5] = 99
    arr[::2] = -1

    return arr.tolist()


def cap_above(values, limit):
    """Заменяет значения больше limit на limit."""
    arr = np.array(values, dtype=float).copy()

    mask = arr > limit
    arr[mask] = limit

    return arr.tolist()


def celsius_to_fahrenheit(values):
    """Переводит температуры из Цельсия в Фаренгейт."""
    arr = np.array(values, dtype=float)

    fahrenheit = arr * 9 / 5 + 32

    return fahrenheit.tolist()
