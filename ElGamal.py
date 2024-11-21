from math_things import *
from DHKE import *

def force_decrypt(ciphertexts: list[list[int] | tuple[int]] | tuple[list[int] | tuple[int]], alpha, p: int, possible_masking_keys: list| tuple, decoding_func: callable = ascii) -> list:
    """
    Decrypts a list or tuple of ciphertexts with handling for corrupted data labeled by None

    :param ciphertexts: The iterable object of ciphertexts (k_1, k_2)
    :param alpha: The alpha value
    :param p: The ring (p value)
    :param possible_masking_keys: A list of all possible masking keys so that a brute force attack can be done
    :param decoding_func: The function to decode the plaintext, ASCII by default
    :return plaintexts: A list of the decrypted and decoded 
    """

    plaintext = []

    for ct in ciphertexts:
        k_1, k_2 = ct
        if None not in ct:
            # find d
            for d in range(1, p):
                if pow(alpha, d, p) == k_1:
                    priv_key = d
                    break
                
            # compute k_m
            k_m = pow(k_1, priv_key, p)

            #decrypt
            x = k_2 * sp.mod_inverse(k_m, p) % p
            plaintext.append([x])
        else:
            # find all possible outputs
            possible = []
            for k_m in possible_masking_keys:
                x = k_2 * sp.mod_inverse(k_m, p) % p
                possible.append(x)
            plaintext.append(possible)
    
    if decoding_func is None:
        return plaintext
    
    decoded = []
    for pt in plaintext:
        vals = []
        for val in pt:
            try:
                vals.append(decoding_func(val))
            except:
                vals.append(None)
        decoded.append(vals)
    return decoded
                
    
def find_masking_keys(p, beta) -> list:
    """
    Compute all possible masking keys for ElGamal encryption.
    
    :param p: Prime modulus
    :param beta: Generator value
    :return: Set of all possible masking keys
    """
    masking_keys = set()
    for k in range(1, p):
        masking_key = pow(beta, k, p)
        masking_keys.add(masking_key)
    return sorted(masking_keys)

def compute_masking_key(alpha, exponent, ring):
    k_m = alpha**exponent%ring
    return k_m

def compute_ephemeral_key(alpha: int, i: int, ring: int) -> int:
    """
    Computes the ephemeral key k_e from alpha^i%ring

    :param alpha: The alpha value
    :param i: The i value
    :param ring: The p value
    :return k_1: The ephemeral key
    """
    return pow(alpha, i, ring)

def compute_masking_key(rec_pub_key: int, i: int, ring: int):
    """
    Computes the masking key, k_m where k_m = beta^i%p

    :param rec_pub_key: The public key of the receiver (beta value)
    :param i: The i value
    :param ring: The ring (p value)
    :return k_M: The masking key
    """
    return pow(rec_pub_key, i, ring)

def ElGamal_encrypt(plaintext: int, i: int, ring: int, alpha: int, receiver_pub_key: int) -> tuple[int]:
    """
    Encrypts with ElGamal where y = x*k_m mod p

    :param plaintext: The plaintext
    :param i: The one-time key (i value)
    :param ring: The ring (p value)
    :param alpha: The alpha value
    :param receiver_pub_key: The public key of the receiver (beta value)
    :return ciphertext: A tuple containing (k_1, k_2), the ciphertext
    """
    # Step 1: Compute the ephemeral public key k_1
    k_1 = compute_ephemeral_key(alpha, i, ring)  # k_1 = alpha^i mod p
    
    # Step 2: Compute the masking key k_m = (receiver's public key)^ephemeral_key mod p
    k_m = compute_masking_key(receiver_pub_key, i, ring)  # k_m = beta^i mod p
    
    # Step 3: Compute the ciphertext component k_2 = plaintext * k_m mod p
    k_2 = (plaintext * k_m) % ring  # k_2 = x * k_m mod p
    
    # Return the ciphertext as a tuple (k_1, k_2)
    return (k_1, k_2)

def ElGamal_decrypt(ciphertext: list[int] | tuple[int], priv_key: int, ring: int) -> int:
    """
    Decrypts with ElGamal where x = y*(k_m)^-1 mod p

    :param ciphertext: A tuple of the ciphertext (k_1, k_2)
    :param priv_key: The receiver's private key (d value)
    :param ring: The ring (p value)
    :return plaintext: The plaintext
    """
    # Step 1: Extract k_1 and k_2 from the ciphertext
    k_1, k_2 = ciphertext

    # Step 2: Compute the masking key k_m = k_1^priv_key mod p
    k_m = pow(k_1, priv_key, ring)  # k_m = (k_1^d) mod p

    # Step 3: Compute the modular inverse of k_m
    k_m_inv = sp.mod_inverse(k_m, ring)

    # Step 4: Decrypt the plaintext x = k_2 * k_m^-1 mod p
    plaintext = (k_2 * k_m_inv) % ring

    return plaintext

def main():
    # x = 26
    # p = 29
    # alpha = 2
    # d = 12
    # priv_key = compute_priv_key(alpha, d, p)
    # i = 5
    # pub_key = compute_pub_key(priv_key, p, alpha)
    # # mask_key = 
    # ct = ElGamal_encrypt(26, 5, 29, 2, 7)
    # pt = ElGamal_decrypt(ct, d, p)
    # print(ct)
    # print(pt)
    pass

if __name__ == "__main__":
    main()