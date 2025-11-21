import re
import string
def check_password_strength(password):
    if not password:
        return 0, ["Please enter a password"]
    score = 0
    feedback = []
    length = len(password)
    if length >= 12:
        score += 25
        feedback.append("✓ Excellent length")
    elif length >= 8:
        score += 20
        feedback.append("✓ Good length")
    elif length >= 6:
        score += 10
        feedback.append("⚠ Fair length")
    else:
        feedback.append("✗ Too short")
    checks = [
        (r'[A-Z]', "uppercase letters", 15),
        (r'[a-z]', "lowercase letters", 15),
        (r'[0-9]', "numbers", 15),
        (r'[!@#$%^&*()_+\-=\[\]{};\':"\\|,.<>/?]', "special characters", 15)
    ]
    for pattern, description, points in checks:
        if re.search(pattern, password):
            score += points
            feedback.append(f"✓ Contains {description}")
        else:
            feedback.append(f"✗ No {description}")
    common_passwords = {'password', '123456', '12345678', 'qwerty', 'abc123'}
    if password.lower() in common_passwords:
        feedback.append("✗ Very common password")
    else:
        score += 10
        feedback.append("✓ Not a common password")
    if re.search(r'(123|abc|qwerty|aaaa)', password.lower()):
        feedback.append("✗ Contains common pattern")
    else:
        score += 5
        feedback.append("✓ No common patterns")
    return score, feedback
def get_strength_level(score):
    if score >= 90: return "🔒 Very Strong"
    elif score >= 70: return "🔐 Strong" 
    elif score >= 50: return "⚠️ Moderate"
    elif score >= 30: return "🔓 Weak"
    else: return "🚫 Very Weak"
def generate_strong_password(length=12):
    import secrets
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(secrets.choice(chars) for _ in range(length))
def main():
    print("🔐 PASSWORD STRENGTH CHECKER")
    print("=" * 30)
    while True:
        password = input("\nEnter password to check (or 'quit' to exit): ")
        if password.lower() == 'quit':
            break
        score, feedback = check_password_strength(password)
        strength = get_strength_level(score)
        print(f"\nStrength: {strength}")
        print(f"Score: {score}/100")
        print("\nAnalysis:")
        for item in feedback:
            print(f"  {item}")
        if score < 70:
            print(f"\n💡 Suggestion: Try: {generate_strong_password()}")
        print("\n" + "=" * 30)
if __name__ == "__main__":
    main()
