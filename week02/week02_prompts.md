# Lab 02: Prompt Engineering Solutions



```python
##Problem 1: Debugging
def sum_of_evens(numbers):
    """Calculate the sum of all even numbers in a list.

    Parameters
    ----------
    numbers : list of int
    A list of integers.

    Returns
    -------
    int
        The sum of all even numbers in the list.
    """
    """
    total = 0
    for num in numbers:
        if num % 2 == 1: #This line has a bug!

            total += num
        return total
"""
    
    #The code above is meant to calculate the sum of all even numbers in a list, but there is a bug on line 21. You are a senior Python developer tasked with fixing this bug. Give an explanation on how you would debug this.

    """Fixed code"""
    def sum_of_evens(numbers):

    total = 0
    for num in numbers:
        if num % 2 == 0:  # fixed: check for even numbers
            total += num
    return total

##Problem 2: Refactoring
def get_names_of_adults(users):
    """Given a list of user dictionaries, return a list of names of users who are 18 years old or older.

    Parameters
    ----------
    users : list of dict
        A list of user dictionaries, each containing 'name' and 'age' keys.

    Returns
    -------
    list of str
        Names of users who are 18 or older.
    """
    """
    results = []
    for i in range(len(users)):
        if users[i]['age'] >= 18:
            results.append(users[i]['name'])
            return results
    """

    #The code above is meant to return a list of names of users who are 18 years old or older, but it is not written in an optimal way. You are a senior Python developer tasked with refactoring the code to improve readability and efficiency through improvements like list comprehensions, better iteration patterns, and clearer variable names. Provide the refactored code along with an explanation of the changes.

    """Fixed code"""

    def get_names_of_adults(users):
    """Return the names of users who are 18 or older.

    Parameters
    ----------
    users : Iterable[dict]
        An iterable of user dictionaries. Each user dict is expected to have
        at least the keys 'name' and 'age'. Extra keys are ignored.

    Returns
    -------
    list[str]
        A list of names for users whose age is >= 18, preserving the input order.

    Notes
    -----
    - Users without a numeric 'age' or without a 'name' key are ignored.
    - This implementation uses a list comprehension for clarity and efficiency.
    """
    # List comprehension with simple validation: ensure we have a dict, a numeric age,
    # and a 'name' key before including the name.
    return [
        user["name"]
        for user in users
        if isinstance(user, dict)
        and ("name" in user)
        and isinstance(user.get("age"), (int, float))
        and user["age"] >= 18
    ]


# If you prefer to accept whole-number floats like 18.0 as valid ages and
# to treat non-dict inputs (e.g., SimpleNamespace) more flexibly, you can
# adapt the checks accordingly.
#
# Example generator-based alternative (yields names lazily):
# def iter_names_of_adults(users):
#     for user in users:
#         try:
#             age = user.get("age")
#         except AttributeError:
#             continue
#         if isinstance(age, (int, float)) and age >= 18 and "name" in user:
#             yield user["name"]

##Problem 3: Documentation
"""
def calculate_area(length, width):
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive numbers.")
        return length * width
        """
        #The code above works correctly to calculate the area of a rectangle, but it lacks the proper documentation. You are a senior Python developer tasked with adding the proper documentation in NumPy-style format. It is important to remember that the function raises a ValueError for invalid inputs. Provide the updated code with the proper documentation.

    """Fixed code"""
    
        def calculate_area(length, width):
    """Calculate the area of a rectangle.

    Parameters
    ----------
    length : int or float
        The length of the rectangle. Must be a positive number (> 0).
    width : int or float
        The width of the rectangle. Must be a positive number (> 0).

    Returns
    -------
    float
        The area of the rectangle computed as ``length * width``.

    Raises
    ------
    ValueError
        If either `length` or `width` is less than or equal to zero.

    Examples
    --------
    >>> calculate_area(3, 4)
    12
    >>> calculate_area(2.5, 4)
    10.0
    >>> calculate_area(0, 5)
    Traceback (most recent call last):
        ...
    ValueError: Length and width must be positive numbers.
    """
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive numbers.")
    return length * width