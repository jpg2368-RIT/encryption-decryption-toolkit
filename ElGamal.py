from math_things import *
from DHKE import *

def possible_masking_keys():
    """
    Finds all possibloe masking keys, K_m
    """

def brute_force_e():
    """
    Brute forces exponent from a ciphertext
    """
    
def find_masking_keys(p, beta) -> list:
    """
    Compute all possible masking keys for ElGamal encryption.
    
    :param p: Prime modulus
    :param beta: Generator value
    :return: List of masking keys
    """
    masking_keys = []
    for k in range(1, p):  # k ranges from 1 to p-1
        masking_key = pow(beta, k, p)  # Compute beta^k mod p
        masking_keys.append(masking_key)
    return masking_keys

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

def compute_masking_key(rec_pub_key: int, ephemeral_key: int, ring: int):
    """
    Computes the masking key, k_m where k_m = beta^i%p

    :param rec_pub_key: The public key of the receiver (beta value)
    :param ephemeral_key: The ephemeral key (k_1)
    :param ring: The ring (p value)
    :return k_M: The masking key
    """
    return pow(rec_pub_key, ephemeral_key, ring)

def ElGamal_encrypt(plaintext: int, i: int, ring: int, alpha: int, receiver_pub_key: int) -> tuple[int]:
    """
    Encrypts with ElGamal where y = x*k_m mod p

    :param plaintext: The plaintext
    :param i: The one-time key (i value)
    :param ring: The ring (p value)
    :param alpha: The alpha value
    :param receiver_pub_key: The public key of the receiver (beta value)
    :return ciphertext: A tuple containing (k-1, k_2), the ciphertext
    """
    # Step 1: Compute the ephemeral public key k_1
    k_1 = compute_ephemeral_key(alpha, i, ring)  # k_1 = alpha^i mod p
    
    # Step 2: Compute the masking key k_m = (receiver's public key)^ephemeral_key mod p
    k_m = compute_masking_key(receiver_pub_key, k_1, ring)  # k_m = beta^i mod p
    
    # Step 3: Compute the ciphertext component k_2 = plaintext * k_m mod p
    k_2 = (plaintext * k_m) % ring  # k_2 = x * k_m mod p
    
    # Return the ciphertext as a tuple (k_1, k_2)
    return (k_1, k_2)
    

def ElGamal_decrypt(ciphertext: int, common_key: int, ring: int) -> int:
    """
    Decrypts with ElGamal where x = y*(k_m)^-1 mod p

    :param ciphertext: The ciphertext
    :param common_key: The common key
    :param ring: The ring
    :return plaintext: The plaintext
    """
    plaintext = ciphertext * sp.mod_inverse(common_key, ring) % ring
    return plaintext


def main():
    x = 26
    p = 29
    alpha = 2
    d = 12
    priv_key = compute_priv_key(alpha, d, p)
    i = 5
    pub_key = compute_pub_key(priv_key, p, alpha)
    # mask_key = 
    ct = ElGamal_encrypt(26, 5, 29, 2, 7)
    print(ct)


if __name__ == "__main__":
    main()