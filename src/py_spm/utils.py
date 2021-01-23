import numpy as np


def empty_to_none(var):
    return None if isinstance(var, np.ndarray) and var.size == 0 else var
