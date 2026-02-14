import math

def password_strength_checker(password):
    if len(password) < 8:
        return "Weak"
    elif len(password) < 12:
        return "Moderate"
    else :
        return "Strong"
    
password = input("Enter your password: ")    
print("Pass strenth:", password_strength_checker(password) )