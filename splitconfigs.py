"""
Functions to split Namespace sections into configs.
"""


def apply_config(active_config_number: int):
    """
    Mark function that it uses a specific config number.
    """
    def inner(f):
        f.active_config_number = active_config_number
        return f
    return inner
