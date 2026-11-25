import numpy as np


def make_hours():
    """Создаёт список часов от 0 до 21 с шагом 3."""
    hours = np.arange(0, 22, 3)
    return hours.tolist()