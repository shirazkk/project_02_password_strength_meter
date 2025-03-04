import re
def check_password_strenth(password):
    score = 0
   
    if len(password)>=8:
        score+=1
    else:
        print("❌ Password should be at least 8 characters long.")

    if re.search(r"[A-Z]", password):
        score+=1
    else:
        print("�� Password should contain at least one uppercase letter.")

    if re.search(r"[a-z]", password):
        score+=1
    else:
        print("❌ Password should contain at least one lowercase letter.")
    
    if re.search(r"\d", password):
        score+=1
    else:
        print("�� Password should contain at least one number (0-9).")
    if  re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score+=1
    else:
        print("❌ Password should contain at least one special character.")

    return score
    
    

while True:        
    user_password = input("Please enter your password: ")
    strength =check_password_strenth(user_password)

    # Strength Rating
    if strength >= 4:
        print("✅ Strong Password!")
        break
    elif strength == 3:
        print("⚠️ Moderate Password - Consider adding more security features.")
    else:
        print("❌ Weak Password - Improve it using the suggestions above.")
    