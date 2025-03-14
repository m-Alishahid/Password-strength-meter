import re

def check_password_strength(password):
    score = 0
    feedback = []
    




    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")
    





    # Upper & Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")
    



    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9).")
    



    # Special Character Check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*).")
    




    # Strength Rating
    if score == 4:
        print("✅ Strong Password! Your password is secure.")
    elif score == 3:
        print("⚠️ Moderate Password - Consider adding more security features.")
        print("Suggestions:")
        for tip in feedback:
            print("-", tip)
    else:
        print("❌ Weak Password - Improve it using the suggestions below.")
        for tip in feedback:
            print("-", tip)





# Get user input
password = input("Enter your password: ")
check_password_strength(password)


# prepared by Ali Shahid 