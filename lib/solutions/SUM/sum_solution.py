# noinspection PyShadowingBuiltins,PyUnusedLocal

# In this code we are implementing a system that adds two numbers together
# Constraints: 
# x (first integer): positive integer between 0 and 100
# y (secoind integer): positive integer between 0 and 100
def compute(x, y):
    # Check if both x and y are integers
    if not isinstance(x,int) or isinstance(y,int):
        # If not raise a TypeError
        raise TypeError("You have inputed a non-integer value!")
    # Check if x is between the allowed range of 0 and 100
    elif x < 0 or x > 100:
        # If not raise a ValueError
        raise ValueError("Your FIRST integer is NOT between 0 and 100.")
    # Check if x is between the allowed range of 0 and 100
    elif y < 0 or y > 100:
        # If not raise a ValueError
        raise ValueError("Your SECOND integer is NOT between 0 and 100.")
    # Else return the sum of the two inputted values
    else: 
        return x + y

