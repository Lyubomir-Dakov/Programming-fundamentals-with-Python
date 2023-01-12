usernames = input().split(', ')

for username in usernames:
    if 3 <= len(username) <= 16:
        not_valid = False
        for symbol in username:
            if symbol.isalpha() or symbol.isdigit() or symbol == '-' or symbol == '_':
                not_valid = False
            else:
                not_valid = True
                break
        if not not_valid:
            print(username)

