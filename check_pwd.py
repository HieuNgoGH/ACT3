def check_pwd(pwd):
    if len(pwd) < 8:
        return False
    if len(pwd) > 20:
        return False
    lower_count = 0
    upper_count = 0
    for letter in pwd:
        if letter.islower():
            lower_count += 1
        if letter.isupper():
            upper_count += 1
    if lower_count == 0 or upper_count == 0:
        return False
    return True