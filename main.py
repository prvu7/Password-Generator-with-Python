import numbers
import random

def gen_random_digit():
    """
    Generate a random digit.
    """
    return str(random.randint(0, 9))

def gen_uppercase_letter():
    """
    Generate a random uppercase letter.
    """
    return chr(random.randint(65, 90))

def gen_lowercase_letter():
    """
    Generate a random lowercase letter.
    """
    return chr(random.randint(97, 122))

def gen_random_special_char():
    """
    Generate a random special character.
    """
    special_chars = "!@#$%^&*()_-+=[]{}|;'<>,.?/"
    return random.choice(special_chars)

def gen_random_password(length, use_digits=True, use_uppercase=True, use_lowercase=True, use_special=True):
    """
    Generate a random password of a given length, using specified character types.
    param lenght: Lenght of the password.
    param use_digits: Include digits if true.
    param use_uppercase: Include uppercase letters if true.
    param use_lowercase: Include lowercase letters if true.
    param use_special: Include special characters if true.
    return: Randomly generated password.
    """
    if not isinstance(length, numbers.Integral) or length <= 0:
        raise ValueError("Length must be a positive integer.")
    
    if not (use_digits or use_uppercase or use_lowercase or use_special):
        raise ValueError("At least one character type must be selected.")
    
    generators = [] # List of functions
    if use_digits:
        generators.append(gen_random_digit)
    if use_uppercase:
        generators.append(gen_uppercase_letter)
    if use_lowercase:
        generators.append(gen_lowercase_letter)
    if use_special:
        generators.append(gen_random_special_char)

    password = []
    for _ in range(length):
        choosed_function = random.choice(generators)
        password.append(choosed_function())

    return ''.join(password)