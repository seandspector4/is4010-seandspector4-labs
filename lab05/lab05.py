def calculate_average_age(users):
    try:
        if not users:
            raise ValueError('User list is empty.')
        total_age = sum(user['age'] for user in users)
        average_age = total_age / len(users)
        return average_age
    except (KeyError, TypeError) as e:
        print(f'Error: {e}')  # Log the error
        return None


def get_active_user_emails(users):
    try:
        active_emails = [user['email'] for user in users if user.get('active')]
        if not active_emails:
            raise ValueError('No active users found.')
        return active_emails
    except KeyError as e:
        print(f'Error: {e}')  # Log the error
        return []


# Mock user data
users = [
    {'name': 'Alice', 'age': 30, 'email': 'alice@example.com', 'active': True},
    {'name': 'Bob', 'age': 24, 'email': 'bob@example.com', 'active': False},
    {'name': 'Charlie', 'age': 29, 'email': 'charlie@example.com', 'active': True},
]

if __name__ == '__main__':
    avg_age = calculate_average_age(users)
    if avg_age is not None:
        print(f'The average age of users is: {avg_age}')

    active_emails = get_active_user_emails(users)
    print(f'Active user emails: {active_emails}')
