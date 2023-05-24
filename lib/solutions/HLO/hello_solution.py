

# noinspection PyUnusedLocal
# friend_name = unicode string

# In this function we are getting the user to implement a friend's name and saying hello to them and the world
def hello(friend_name):
    # Check the input is a string
    if not isinstance(friend_name,str):
        raise TypeError(f"Expected string value, but received friend_name={friend_name} (type: {type(friend_name).__name__})")
    # Say hello to the inputted string
    else:
        return f"Hello {friend_name}! Welcome and say hello to the world!"

