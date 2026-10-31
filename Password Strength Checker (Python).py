import re

def check_password_strength(password):
    score = 0
    feedback = []

    # Length check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("• Password should be at least 8 characters long.")

    # Uppercase check
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("• Add at least one uppercase letter.")

    # Lowercase check
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("• Add at least one lowercase letter.")

    # Number check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("• Add at least one number.")

    # Special character check
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("• Add at least one special character (!@#$%^&* etc.).")

    # Rating evaluation
    if score == 5:
        rating = "Strong 🟢"
    elif 3 <= score < 5:
        rating = "Moderate 🟡"
    else:
        rating = "Weak 🔴"

    return rating, feedback

if __name__ == "__main__":
    print("=== Secure Password Strength Checker ===")
    pwd = input("Enter a password to test: ")
    rating, suggestions = check_password_strength(pwd)
    
    print(f"\nRating: {rating}")
    if suggestions:
        print("Suggestions to improve:")
        for tip in suggestions:
            print(tip)
    else:
        print("Great job! Your password is very secure.")
