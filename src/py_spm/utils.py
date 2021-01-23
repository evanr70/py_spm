import numpy as np


def empty_to_none(var):
    return None if isinstance(var, np.ndarray) and var.size == 0 else var


def check_lowered_string(array, search_term):
    return np.char.find(np.char.lower(array), search_term) != -1
