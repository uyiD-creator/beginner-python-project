# Password Strength Checker

print("Welcome to Password Checker!")
password = input("Enter a password to check: ")

length = len(password)
has_upper = False
has_lower = False
has_digit = False
has_special = False

special_characters = "!@#$%^&*()_+-=[]{};:'\",.<>?/|\\"

for char in password:
    if char.isupper():
        has_upper = True
    elif char.islower():
        has_lower = True
    elif char.isdigit():
        has_digit = True
    elif char in special_characters:
        has_special = True

# Check strength
if length < 6:
    print("Password too short. Try something longer.")
elif has_upper and has_lower and has_digit and has_special:
    print("Strong password ✅")
elif (has_lower or has_upper) and has_digit:
    print("Medium password ✅ (Try adding special characters)")
else:
    print("Weak password ❌ (Use mix of letters, numbers & symbols)")
