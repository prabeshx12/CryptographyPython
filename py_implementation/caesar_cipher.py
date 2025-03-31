# Caesar Cipher

# Plain text can be anything but cipher will only change the letters only. Other it will leave as it is.
upper_case_alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def letter_to_num(alphabet):
    return upper_case_alphabets.index(alphabet.upper())


def num_to_letter(number, state):
    number %= 26
    if state == 0:
        return upper_case_alphabets[number]
    elif state == 1:
        return upper_case_alphabets.lower()[number]


def caesar_cipher_encrypt(message):
    ciphered_text = ''
    for a in message:
        if not a.isalpha():
            ciphered_text += a
        else:
            if a.upper() == a:
                state = 0
            else:
                state = 1

            ciphered_text += num_to_letter(letter_to_num(a) + 3, state)

    return ciphered_text


def caesar_cipher_decrypt(message):
    deciphered_text = ''
    for a in message:
        if not a.isalpha():
            deciphered_text += a
        else:
            if a.upper() == a:
                state = 0
            else:
                state = 1
            deciphered_text += num_to_letter(letter_to_num(a) - 3, state)

    return deciphered_text


plain_text = input("Enter your message: ")
print(caesar_cipher_encrypt(plain_text))

