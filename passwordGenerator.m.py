import random
import string
def generate_password(length):
    if length<4:
        print("password length should be at least 4 characters for good security.")
        return None
    lower=string.ascii_lowercase
    upper=string.ascii_uppercase
    digits=string.digits
    symbols=string.punctuation
    all_chars=lower+upper+digits+symbols
    password=random.choice(lower)+random.choice(upper)+random.choice(symbols)
    password+=''.join(random.choices(all_chars,k=length-4))
    password=''.join(random.sample(password,len(password)))
    return password
try:
    length=int(input("Enter the desired password length:"))
    generate_password=generate_password(length)
    if generate_password:
        print("Generate password:",generate_password)
except valueError:
        print("please enter a valid number.")
