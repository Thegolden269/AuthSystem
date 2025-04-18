import re

def validate_email(email):
    regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.match(regex, email):
        return True
    raise ValueError("Invalid email format")


def validate_password(password):
    regex = r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$'
    if re.match(regex, password):
        return True
    raise ValueError("Password must be at least 8 characters long and contain at least one letter and one number")


def validate_first_name(first_name):
    if len(first_name) < 2 or len(first_name) > 30:
        raise ValueError("First name must be between 2 and 30 characters long")
    if not re.match(r"^[a-zA-ZÀ-ÿ\-'\s]+$", first_name):
        raise ValueError("First name can only contain letters, hyphens, apostrophes and spaces")
    return True


def validate_last_name(last_name):
    if len(last_name) < 2 or len(last_name) > 30:
        raise ValueError("Last name must be between 2 and 30 characters long")
    if not re.match(r"^[a-zA-ZÀ-ÿ\-'\s]+$", last_name):
        raise ValueError("Last name can only contain letters, hyphens, apostrophes and spaces")
    return True
