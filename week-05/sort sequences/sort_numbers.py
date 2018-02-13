from datastubs import NUMBER_LIST


def reverse_numerical_order():
    """
    Sort the list of numbers but in reverse order
    """
    return sorted(NUMBER_LIST, reverse=True)


def numerical_order():
    """
    Sort the list of numbers in numerical order
    """
    return sorted(NUMBER_LIST)

def as_absolute_value():
    """
    The absolute value of a number `n` is its value
    regardless of positive or negative sign
    """
    # fill it out
    return sorted(NUMBER_LIST, key=abs)

def as_inverse_number():
    
    def foo(x):
        return 1/x
    return sorted(NUMBER_LIST, key=foo)

