import random
import string

def gen_pwd(length):
    if length < 8 :
        length = 8
    pw = []
    characters = string.ascii_letters + string.digits + '~!@#$%^&*()_+.'
    while len(pw) < length:
        pw.append(random.choice(characters))
    if any(char.islower() for char in pw) and any(char.isupper() for char in pw) and any(char.isdigit() for char in pw) and any(char in '~!@#$%^&*()_+.' for char in pw):
        return ''.join(pw)
    else:
        return gen_pwd(length)