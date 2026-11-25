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
