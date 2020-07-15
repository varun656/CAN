from katan import KATAN

if __name__ == '__main__':
    #key = "0xFFFFFFFFFFFFFFFFFFFF"
    key = 0
    plaintext = 0xFFFFFFFFFFFFFFFF

    myKATAN = KATAN(key)

    print('The key is :')

    print('key =',hex(key))
    print('plain =', hex(plaintext))

    encrypted = myKATAN.enc(plaintext)
    print('encrypted =', hex(encrypted))
    decrypted = myKATAN.dec(encrypted)
    print('decrypted =', hex(decrypted))