# select = input("would you like to encrypt or decrypt?")
# message = input("what is your message?")
# shift_score = input("what is your shift score?")


# def encrypt():
#     encrypted_message = []
#     for char in message:
#         encrypted_message.append(chr(ord(char)+int(shift_score)))
#     return ''.join(encrypted_message)


# def decrypt():
#     decrypted_message = []
#     for char in message:
#         decrypted_message.append(chr(ord(char)-int(shift_score)))
#     return ''.join(decrypted_message)


# if select == 'encrypt' or select == 'e' or select == 'en':
#     print(encrypt())
# elif select == 'decrypt' or select == 'd' or select == 'de':
#     print(decrypt())
# else:
#     print("error")


def main():
    while True:
        select = input("would you like to encrypt or decrypt?")
        message = input("what is your message?")
        shift_score = input("what is your shift score?")

        def encrypt():
            encrypted_message = []
            for char in message:
                encrypted_message.append(chr(ord(char)+int(shift_score)))
            return ''.join(encrypted_message)

        def decrypt():
            decrypted_message = []
            for char in message:
                decrypted_message.append(chr(ord(char)-int(shift_score)))
            return ''.join(decrypted_message)

        if select == 'encrypt' or select == 'e' or select == 'en':
            print(encrypt())
        elif select == 'decrypt' or select == 'd' or select == 'de':
            print(decrypt())
        else:
            print("error")

        cont = input("type yes if you want to continue")
        if cont.lower() in ['no', 'n']:
            break


main()
