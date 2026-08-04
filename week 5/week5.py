# Week 5 - Functions and Password Validator
# Moderate participant sample

def has_minimum_length(password):
    # Check if the password has at least 8 characters
    return len(password) >= 8


def has_digit(password):
    # Check if the password contains at least one digit
    for character in password:
        if character.isdigit():
            return True
    return False


def has_uppercase(password):
    # Check if the password contains at least one uppercase letter
    for character in password:
        if character.isupper():
            return True
    return False


def has_lowercase(password):
    # Check if the password contains at least one lowercase letter
    for character in password:
        if character.islower():
            return True
    return False


password = input("Enter password: ")

failed_rules = []

if not has_minimum_length(password):
    failed_rules.append("Password must have at least 8 characters.")

if not has_digit(password):
    failed_rules.append("Password must contain at least one digit.")

if not has_uppercase(password):
    failed_rules.append("Password must contain at least one uppercase letter.")

if not has_lowercase(password):
    failed_rules.append("Password must contain at least one lowercase letter.")

if len(failed_rules) == 0:
    print("Password is valid.")
else:
    print("Password is invalid.")
    print("Failed rules:")
    for rule in failed_rules:
        print("-", rule)
