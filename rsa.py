import math


def totient_func(n):
    count = 0
    for a in range(1, n):
        if math.gcd(a, n) == 1:
            count += 1

    return count


def rsa_algo(message=1):  # here message is the message to be encrypted.
    # say we use p=3 and q=7 for our example.
    p = 3
    q = 7
    n = p * q
    tot_n = totient_func(n)
    e = 0
    d = 0
    num = 1
    # now we need to find e such that 1<e<tot_n and gcd(e, tot_n)=1.
    for a in range(2, tot_n):
        if math.gcd(a, tot_n) == 1:
            e = a
            break
    # also we need to find d such that dxe is congruent to 1 (mod tot_n).
    while 1:
        if (num * e) % tot_n == 1:
            d = num
            break
        num += 1

    encrypted_message = pow(message, e, n)
    decrypted_message = pow(encrypted_message, d, n)
    print(f"encryption key: {e}, decryption key: {d}")

    return encrypted_message, decrypted_message


encrypted_code, decrypted_code = rsa_algo(message=4)
print(f"The encrypted and decrypted value is {encrypted_code} and {decrypted_code} respectively.")