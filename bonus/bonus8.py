user_input = input('Enter your password: ')
result = {}

# password should be 8 characters
if len(user_input) >= 8:
    result["length"] = True
else:
    result["length"] = False

# contain digit
digit = False
for i in user_input:
    if i.isdigit():
        digit = True

result["digit"] = digit

# contain uppercase
uppercase = False
for i in user_input:
    if i.isupper():
        uppercase = True

result["uppercase"] = uppercase

if all(result.values()):
    print('Strong password')
else:
    print('Week password')
