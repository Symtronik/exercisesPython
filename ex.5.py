# 5. Write a Python program that accepts the user's first and ' \
# 'last name and prints them in reverse order with a space between them.

name = input('Your name: ')
name = name.capitalize()
surname = input('Your surname: ')
surname = surname.capitalize()
print(f'Hi {surname} {name}')
