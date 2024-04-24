#password generator code

import random
import string

#intializing the alphabets,digits and special characters

letters="abcdefghijklmnopqrstuvwxyz"
uppercase_letters=letters.lower()
digits="1234567890"
special_char= "()[]{},.:;-_/\\?+*#"

#taking desired length of password from the user
length=int(input("Enter length of the password:  "))

#knowing the requirements of the password from the user
uppercase = input("Do you require uppercase letters in your password? y/n:  ")
uppercase = uppercase.lower()
digit = input("Do you require digits in your password? y/n:  ")
digit = digit.lower()
special = input("Do you reqire special characters in your password? y/n:  ")
special = special.lower()

#applying the requirements
if uppercase == 'y':
    letters += uppercase_letters
if digit == 'y':
    letters += digits
if special == 'y':
    letters += special_char

if uppercase == 'y' and digit == 'y':
    letters = letters + uppercase_letters + digits
if uppercase == 'y' and special == 'y':
    letters = letters + uppercase_letters + special_char
if digit == 'y' and special == 'y':
    letters = letters + digits + special_char
if digit == 'y' and special == 'y' and uppercase == 'y':
    letters = letters + digits + special_char + uppercase_letters

#generating the password
password = "".join(random.sample(letters, length))
print(password)

