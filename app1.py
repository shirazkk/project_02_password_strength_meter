import re

def PasswordStrengthMeter(password):
    score = 0
    messages = []

    if len(password) >=8:
      score+=1
    else:
        messages.append("🔴 Password should be at least 8 characters long.")

    if re.search(r'[A-Z]',password):
        score += 1
    else:
        messages.append("🔴 Password should contain at least one uppercase letter.")

    if re.search(r'[a,z]',password):
        score += 1
    else:
        messages.append("🔴 Password should contain at least one lowercase letter.")

    if re.search(r'\d',password):
        score += 1
    else:
        messages.append("🔴 Password should contain at least one digit.")

    if re.search(r'[!@#$%^&*(),.?":{}|<>]',password):
        score += 1
    else:
        messages.append("🔴 Password should contain at least one special character.")

    return score, messages

