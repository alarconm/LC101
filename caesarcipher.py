def rot13(mess):
    """encrypt a message by shifting each letter 13 characters to its right"""

    mess = mess.lower()
    encrypted = ''

    for i in range(len(mess)):

        encrypted += chr(ord(mess[i])+13)

    return encrypted


print(rot13('abcde'))
print(rot13('nopqr'))
