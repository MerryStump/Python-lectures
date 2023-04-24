login = input('Please enter your login: ')

password = input('Please enter your password: ')
password_confirmation = input('Please confirm your password: ')

if len(password) >= 8 and any(char.isdigit() for char in password) and any(char.isalpha() for char in password) and password == password_confirmation:
    print('Your password is accepted')
else:
    print('Your password does not meet the requirements.')