# noinspection PyShadowingBuiltins,PyUnusedLocal

# In this code we are implementing a system that adds two numbers together
# Constraints: 
# x (first integer): positive integer between 0 and 100 [in this case I assumed inclusive of 0 and 100]
# y (secoind integer): positive integer between 0 and 100 [in this case I assumed inclusive of 0 and 100]


def compute(x, y):
    # Check if both x and y are integers
    if not isinstance(x,int) or not isinstance(y,int):
        # If not raise a TypeError
        raise TypeError(f"Expected integer values, but received x={x} (type: {type(x).__name__}) and y={y} (type: {type(y).__name__})")
    # Check if x is between the allowed range of 0 and 100
    elif x < 0 or x > 100:
        # If not raise a ValueError
        raise ValueError(f"Your FIRST integer input was x={x}, this is NOT between 0 and 100 (inclusive)")
    # Check if x is between the allowed range of 0 and 100
    elif y < 0 or y > 100:
        # If not raise a ValueError
        raise ValueError(f"Your SECOND integer input was y={y}, this is NOT between 0 and 100 (inclusive)")
    # Else return the sum of the two inputted values
    else: 
        return x + y


