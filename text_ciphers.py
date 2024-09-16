from math_things import *

def shift(message, k) -> str:
    """
    Performs a shift cipher on a message

    :param message: The input message
    :param k: The amount to shift by
    :return shifted: The shifted message
    """
    shifted = ""
    for letter in message:
        if letter.isalpha():
            alph_base = ord('a') if letter.islower() else ord('A')
            shifted = (ord(letter) - alph_base + k) % 26 + alph_base
            shifted += chr(shifted)
        else:
            shifted += letter
    return shifted

def shift_decrypt_manual(ciphertext: str, k: int = 26) -> None:
    """
    Displays every shift of the input ciphertext for the user to find the one that seems correct

    :param ciphertext: The encrypted ciphertext
    :param k: The length of the alphabet to use. 26 for English by default
    """
    for k in range(26):
        print(f"Shift of {k}: \"{shift(ciphertext, k)}\"")

def affine_encrypt(plaintext: str, a: int, b: int, m: int = 26) -> str:
    """
    Encrypts a message with an aphine cipher. Preserves spaces and case.

    :param plaintext: The message to encrypt
    :param a: The a value
    :param b: The b value
    :param m: The length of the alphabet to use (26 for English by default)
    :return ciphertext: The encrypted ciphertext
    """
    ciphertext = ""
    for letter in plaintext:
        if letter == " ":
            ciphertext += " "
        else:
            alph_base = ord('a') if letter.islower() else ord('A')
            x = ord(letter)-alph_base
            ciphertext += chr(((a * x + b) % m) + alph_base)
    return ciphertext

def affine_decrypt(ciphertext: str, a: int, b: int, m: int = 26) -> str:
    """
    Encrypts a message with an aphine cipher. Preserves spaces and case.

    :param ciphertext: The message to decrypt
    :param a: The a value
    :param b: The b value
    :param m: The length of the alphabet to use (26 for English by default)
    :return plaintext: The decrypted message
    """
    plaintext = ""
    a_inv = find_mod_inverse(a, m)
    for letter in ciphertext:
        if letter == " ":
            plaintext += " "
        else:
            alph_base = ord('a') if letter.islower() else ord('A')
            y = ord(letter)-alph_base
            plaintext += chr(((a_inv * (y - b)) % m) + alph_base)
    return plaintext
