from math_things import *

def generate_keys(p, q, e):
    # choose 2 large primes, p and q. ex: p=3, q=11
    # compute n = p*q. ex: n = 33
    n = p*q
    # compute phi(n) = (p-1) * (q-1). ex: phi(33)=20
    phi_n = euler_totient(n)
    # select the public exponent e where e in [1, phi(n)-1] and gcd(e, phi(n)) = 1 (relatively prime). ex: e=3
    # compute private key d where d*e=1 mod phi(n) (use EEA). ex: d=7 mod 20
    d = mod_inv(e, phi_n)
    # return public key (n, e) and private key d
    return ((n, e), d)

def RSA_encrypt(plaintext: int, p:int, q:int, e:int):
    # generate keys
    pub_key, priv_key = generate_keys(p, q, e)

    # compute y = x^e mod n
    ciphertext = sq_mod_table(plaintext, e, pub_key[0], show_table=False)
    return ciphertext, priv_key

def RSA_decrypt(ciphertext, d, n):
    # x = y^d mod n
    plaintext = sq_mod_table(ciphertext, d, n, show_table=False)
    return plaintext

def main():
    p, q, e = 3, 11, 3
    n = p*q
    plaintext = 0x04
    print(f"{plaintext=:x}")
    ct, d = RSA_encrypt(0x04, p, q, e)
    print(f"{ct=}")
    pt = RSA_decrypt(ct, d, n)
    print(f"{pt=:x}")

if __name__ == "__main__":
    main()