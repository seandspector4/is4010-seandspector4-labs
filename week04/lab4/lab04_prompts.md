# Problem 1
You have two very large lists of product IDs from two different suppliers. You need to find out which product IDs are present in both lists so you know which products you can source from either supplier. The order of the final list does not matter.
Use a set data structure
Why Sets Are Best for This Problem
Sets are the optimal choice for this use case because:

Intersection Operation - Python sets have a built-in .intersection() method that's specifically designed for this:

Python
common_ids = supplier1_ids & supplier2_ids  # Using & operator
# or
common_ids = supplier1_ids.intersection(supplier2_ids)
O(1) Average Lookup Time - Set membership testing is O(1) on average, vs O(n) for lists, making it very efficient with large datasets

Automatic Deduplication - Sets automatically remove duplicates if your supplier lists have any

Performance - Converting lists to sets and finding intersection is much faster than nested loops or list comprehensions with large data

Example Implementation
Python
# Load your data
supplier1_ids = set(load_supplier1_data())  # Convert to set
supplier2_ids = set(load_supplier2_data())  # Convert to set

# Find common IDs
common_ids = supplier1_ids & supplier2_ids

# Or if you want to keep it as a list
common_ids_list = list(supplier1_ids & supplier2_ids)
Performance Comparison
For two lists with millions of items:

Set intersection: O(n + m) - Linear time complexity
Nested loops: O(n × m) - Quadratic time complexity
List .count() in loop: O(n × m) - Quadratic time complexity
Alternative (if you need to preserve data with IDs)
If you need to keep associated data with each product ID, consider using dictionaries:

Python
supplier1_products = {id: details for id, details in supplier1_data}
supplier2_products = {id: details for id, details in supplier2_data}

# Find common IDs
common_ids = supplier1_products.keys() & supplier2_products.keys()

# Get combined data for common products
combined = {id: (supplier1_products[id], supplier2_products[id]) 
            for id in common_ids}
Bottom line: For your specific problem, sets are the clear winner - they're fast, simple, and built exactly for this kind of operation.

# Problem 2
Your application loads a list of user profiles from a database. Each user has a unique username, an age, and an email address. You frequently need to look up a user's complete profile by their username. Performance is critical. You are a python developer tasked with finding the best data structure for this problem. What do you decide?

Based on your problem of frequently looking up user profiles by username with critical performance requirements, here's my recommendation:

## Use a **dictionary** data structure

### Why Dictionaries Are Best for This Problem

**Dictionaries are the optimal choice** because:

1. **O(1) Average Lookup Time** - Dictionary key lookup is O(1) on average, making it extremely fast even with millions of users:
   ```python
   user_profile = users_dict[username]  # Instant access
   ```

2. **Natural Key-Value Mapping** - Usernames are unique identifiers, which map perfectly to dictionary keys, and user data (age, email) naturally becomes the value

3. **Flexibility** - You can store the entire profile as a nested dictionary or custom object:
   ```python
   users_dict = {
       "alice": {"age": 28, "email": "alice@example.com"},
       "bob": {"age": 35, "email": "bob@example.com"}
   }
   ```

4. **Real-World Performance** - For critical performance applications, O(1) lookup time is crucial compared to O(n) for lists

### Example Implementation

```python
# Load from database and build dictionary
def load_user_profiles(db_connection):
    users_dict = {}
    for username, age, email in db_connection.query("SELECT username, age, email FROM users"):
        users_dict[username] = {
            "age": age,
            "email": email
        }
    return users_dict

# Lookup is instant
users = load_user_profiles(db)
user_profile = users["alice"]  # O(1) operation
print(f"Age: {user_profile['age']}, Email: {user_profile['email']}")
```

### Alternative: Using a Custom Class (More Structured)

For better code organization and type safety:

```python
from dataclasses import dataclass

@dataclass
class UserProfile:
    username: str
    age: int
    email: str

# Build dictionary with custom objects
users_dict = {
    user.username: user 
    for user in load_users_from_db()
}

# Lookup with type hints and IDE support
user: UserProfile = users_dict["alice"]
print(f"Age: {user.age}, Email: {user.email}")
```

### Performance Comparison

For a database with 1 million users:
- **Dictionary lookup: O(1)** - Microseconds, constant time
- **List search: O(n)** - Could take seconds with linear search
- **List with `.find()`: O(n)** - Still requires scanning through users

### Example: Why This Matters

```python
# ❌ Inefficient (O(n) lookup)
users_list = [(username, age, email), ...]
user = next((u for u in users_list if u[0] == "alice"), None)

# ✅ Efficient (O(1) lookup)
users_dict = {username: {"age": age, "email": email}, ...}
user = users_dict.get("alice")
```

**Bottom line:** **Dictionaries are the clear winner** for this use case - they provide instant O(1) lookups which is critical for performance-sensitive applications. The unique username naturally serves as the dictionary key, and all profile data becomes the value.

# Problem 3
You are given a list of integers representing sensor readings. You need to produce a report that contains only the even-numbered readings, and they must be presented in the exact same order they were received. As a python developer, you are tasked with finding the best data structure for this. What do you recommend?

Based on your problem of filtering even-numbered sensor readings while preserving their original order, here's my recommendation:

## Use a **list** data structure

### Why Lists Are Best for This Problem

**Lists are the optimal choice** because:

1. **Preserves Order** - Lists maintain insertion order (guaranteed in Python 3.7+), which is essential for your requirement of keeping readings in the exact same order they were received

2. **Simple and Efficient Filtering** - List comprehensions provide clean, Pythonic syntax for filtering:
   ```python
   even_readings = [reading for reading in sensor_readings if reading % 2 == 0]
   ```

3. **Sequential Access** - Since you need to output a report in order, lists are naturally suited for iteration and presentation

4. **Performance** - List comprehensions are highly optimized in Python and run in O(n) time, which is optimal for this filtering operation

### Example Implementation

```python
# Original sensor readings in order
sensor_readings = [23, 42, 15, 88, 36, 7, 50, 19, 64]

# Filter for even readings - preserves order
even_readings = [reading for reading in sensor_readings if reading % 2 == 0]

print(even_readings)  # Output: [42, 88, 36, 50, 64]
```

### Alternative: Using `filter()` Function

If you prefer a functional approach:

```python
even_readings = list(filter(lambda x: x % 2 == 0, sensor_readings))
```

### Why NOT Other Data Structures

- **Sets** - ❌ Would lose the original order of readings
- **Dictionaries** - ❌ Unnecessary overhead; you don't need key-value mapping
- **Tuples** - ❌ Immutable; not practical for building a filtered collection

### Real-World Example with Report Generation

```python
def generate_sensor_report(sensor_readings):
    # Filter even readings, preserving order
    even_readings = [reading for reading in sensor_readings if reading % 2 == 0]
    
    # Generate report
    report = {
        "total_readings": len(sensor_readings),
        "even_readings_count": len(even_readings),
        "even_readings": even_readings,  # In original order
        "timestamp": datetime.now()
    }
    return report

# Usage
readings = [23, 42, 15, 88, 36, 7, 50, 19, 64]
report = generate_sensor_report(readings)
print(report)
# Output: {
#   'total_readings': 9,
#   'even_readings_count': 5,
#   'even_readings': [42, 88, 36, 50, 64],
#   'timestamp': ...
# }
```

### Performance

- **Time Complexity: O(n)** - Must examine every reading once to filter
- **Space Complexity: O(k)** - Where k is the number of even readings
- This is optimal since you must check every element at least once

**Bottom line:** **Lists are the clear winner** for this use case - they preserve the critical requirement of maintaining original order while providing clean, efficient filtering syntax. List comprehensions are the Pythonic way to solve this problem.
