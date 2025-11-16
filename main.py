# This is the simple application our agents will test.
# It has one working function and one broken function.

def add(a, b):
    """A function that works correctly."""
    return a + b

def buggy_subtract(a, b):
    """A function with a deliberate bug."""
    # The bug is here! It should be a - b.
    return a + b