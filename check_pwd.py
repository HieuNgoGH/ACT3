def check_pwd(pwd):
    if len(pwd) < 8:
        return False
    if len(pwd) > 20:
        return False
    digit_count = 0
    lower_count = 0
    upper_count = 0
    symbols = "~`!@#$%^&*()_+-="
    symbol_count = 0
    for letter in pwd:
        if letter.isdigit():
            digit_count += 1
        if letter.islower():
            lower_count += 1
        if letter.isupper():
            upper_count += 1
        for character in symbols:
            if letter == character:
                symbol_count += 1
    if lower_count == 0 or upper_count == 0 or symbol_count == 0 or digit_count == 0 or digit_count == len(pwd):
        return False
    return True
