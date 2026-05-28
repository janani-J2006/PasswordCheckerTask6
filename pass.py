import re

# Common weak passwords list
common_passwords = ["123456", "password", "12345678", "qwerty", "abc123"]

def check_password_strength(password):
    score = 0
    feedback = []

    # Length check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long")

    # Uppercase
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter")

    # Lowercase
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter")

    # Digits
    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Include at least one number")

    # Special characters
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("Include at least one special character")

    # Common password check
    if password.lower() in common_passwords:
        feedback.append("Password is too common")
        score = 1

    # Repeated characters check
    if re.search(r"(.)\1{2,}", password):
        feedback.append("Avoid repeated characters")

    # Strength classification
    if score <= 2:
        strength = "Weak"
    elif score == 3 or score == 4:
        strength = "Medium"
    else:
        strength = "Strong"

    return strength, feedback


# Run
password = input("Enter password: ")
strength, feedback = check_password_strength(password)

print("\nPassword Strength:", strength)

if feedback:
    print("Suggestions:")
    for f in feedback:
        print("-", f)
else:
    print("Strong password! No suggestions needed.")