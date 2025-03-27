"""
Validators Module
"""

def int_validator(arg, value, min_val=None, max_val=None, min_msg=None, max_msg=None):
    """
    :param arg:
    :param value:
    :param min_val:
    :param max_val:
    :return:
    """

    if not isinstance(value, int):
        raise TypeError(f'{arg} must be int')

    if min_val is not None and value < min_val:
        if min_msg is not None:
            raise ValueError(min_msg)
        else:
            raise ValueError(f'{value} should be <>> {min_val}')

    if max_val is not None and value > max_val:
        if max_msg is not None:
            raise ValueError(max_msg)
        else:
            raise ValueError(f'{value} should not be > {max_val}')




