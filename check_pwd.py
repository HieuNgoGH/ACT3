def check_pwd(pwd):
    if len(pwd) < 8:
        return False
    if len(pwd) > 20:
        return False
    return True