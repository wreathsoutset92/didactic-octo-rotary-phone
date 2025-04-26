import re

def check_strength(password):
    strength = 0
    if len(password) >= 8: strength += 1
    if re.search(r'[A-Z]', password): strength += 1
    if re.search(r'[a-z]', password): strength += 1
    if re.search(r'[0-9]', password): strength += 1
    if re.search(r'[@$!%*?&]', password): strength += 1

    if strength <= 2:
        return "❌ Weak"
    elif strength == 3 or strength == 4:
        return "✅ Moderate"
    else:
        return "💪 Strong"

pw = input("🔑 Enter your password: ")
print(check_strength(pw))
