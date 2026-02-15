# Messy script to be refactored
"""
users = [
    {"name": "alice", "age": 30, "is_active": True, "email": "alice@example.com"},
    {"name": "bob", "age": 25, "is_active": False},
    {"name": "charlie", "age": 35, "is_active": True, "email": "charlie@example.com"},
    {"name": "david", "age": "unknown", "is_active": False}
]

# Calculate total age and count users for average
total_age = 0
user_count_for_age = 0
for user in users:
    if isinstance(user.get("age"), int):
        total_age += user["age"]
        user_count_for_age += 1
average_age = total_age / user_count_for_age
print(f"average user age: {average_age:.2f}")

# Get a list of all active user emails
active_user_emails = []
for user in users:
    if user.get("is_active") and user.get("email"):
        active_user_emails.append(user["email"])
print(f"active user emails: {active_user_emails}")
"""

#Refactored Code with clean organization and error handling
"""Lab 05: Functions and Error Handling

This module demonstrates clean code organization through function decomposition
and robust error handling for real-world data processing scenarios.
"""

users = [
    {"name": "alice", "age": 30, "is_active": True, "email": "alice@example.com"},
    {"name": "bob", "age": 25, "is_active": False},
    {"name": "charlie", "age": 35, "is_active": True, "email": "charlie@example.com"},
    {"name": "david", "age": "unknown", "is_active": False}
]


def calculate_average_age(users):
    """
    Calculate the average age of users with valid integer ages.
    
    This function iterates through a list of user dictionaries and computes
    the average age for users with valid integer age values. Non-integer ages
    (including strings and None values) are excluded from the calculation.
    
    Parameters
    ----------
    users : list of dict
        A list of user dictionaries. Each dictionary should contain an 'age' key
        with either an integer value or a non-integer value (which will be skipped).
    
    Returns
    -------
    float
        The average age of users with valid integer ages. Returns 0.0 if the
        input list is empty or if no users have valid integer ages.
    
    Notes
    -----
    - Uses isinstance() to validate age data types
    - Safely accesses dictionary keys using .get() method
    - Handles edge case of empty list by returning 0.0 instead of raising ZeroDivisionError
    - Invalid age values (strings, None, etc.) are silently skipped
    
    Examples
    --------
    >>> users = [
    ...     {"name": "alice", "age": 30},
    ...     {"name": "bob", "age": 25},
    ...     {"name": "charlie", "age": 35}
    ... ]
    >>> calculate_average_age(users)
    30.0
    
    >>> users = [{"name": "david", "age": "unknown"}]
    >>> calculate_average_age(users)
    0.0
    
    >>> calculate_average_age([])
    0.0
    """
    try:
        # Handle empty list edge case
        if not users:
            print("error: cannot calculate average age of an empty list.")
            return 0.0
        
        total_age = 0
        valid_age_count = 0
        
        # Iterate through users and sum only valid integer ages
        for user in users:
            age = user.get("age")
            if isinstance(age, int):
                total_age += age
                valid_age_count += 1
        
        # Handle case where no valid ages were found
        if valid_age_count == 0:
            print("error: no valid ages found in user list.")
            return 0.0
        
        # Calculate and return average
        return total_age / valid_age_count
        
    except (ZeroDivisionError, TypeError) as e:
        print(f"error: cannot calculate average age: {e}")
        return 0.0


def get_active_user_emails(users):
    """
    Retrieve email addresses from all active users in the list.
    
    This function filters the user list to find active users (where is_active
    is True) and returns their email addresses. Only users with both is_active=True
    and a non-empty email field are included in the result.
    
    Parameters
    ----------
    users : list of dict
        A list of user dictionaries. Each dictionary should potentially contain
        'is_active' and 'email' keys. Missing keys are treated as False/None
        and the user is excluded from results.
    
    Returns
    -------
    list of str
        A list of email addresses from active users. Returns an empty list if
        no active users with emails are found or if the input is empty.
    
    Notes
    -----
    - Uses .get() method for safe dictionary key access (returns None if missing)
    - Requires BOTH conditions to be true: is_active AND email exists
    - Silently skips users missing either 'is_active' or 'email' keys
    - Preserves the order of emails as they appear in the input list
    
    Examples
    --------
    >>> users = [
    ...     {"name": "alice", "is_active": True, "email": "alice@example.com"},
    ...     {"name": "bob", "is_active": False, "email": "bob@example.com"},
    ...     {"name": "charlie", "is_active": True, "email": "charlie@example.com"}
    ... ]
    >>> get_active_user_emails(users)
    ['alice@example.com', 'charlie@example.com']
    
    >>> users = [{"name": "bob", "is_active": False}]
    >>> get_active_user_emails(users)
    []
    
    >>> get_active_user_emails([])
    []
    """
    try:
        # Handle empty list edge case
        if not users:
            return []
        
        active_user_emails = []
        
        # Iterate through users and collect emails from active users only
        for user in users:
            is_active = user.get("is_active")
            email = user.get("email")
            
            # Both conditions must be true: user is active AND has an email
            if is_active and email:
                active_user_emails.append(email)
        
        return active_user_emails
        
    except (KeyError, TypeError, AttributeError) as e:
        print(f"error: cannot get active user emails: {e}")
        return []


if __name__ == '__main__':
    # Calculate and display average age
    avg_age = calculate_average_age(users)
    print(f"average user age: {avg_age:.2f}")
    
    # Get and display active user emails
    active_emails = get_active_user_emails(users)
    print(f"active user emails: {active_emails}")