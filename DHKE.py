def compute_pub_key(priv_key: int, p: int, alpha: int):
    A = alpha**priv_key%p
    return A

def compute_common_key(priv_key: int, other_pub_key: int, p: int):
    B = other_pub_key**priv_key%p
    return B

def check_common_keys(priv1:int, pub1:int, priv2:int, pub2:int, p:int):
    return compute_common_key(priv1, pub2, p) == compute_common_key(priv2, pub1, p)

def DHKE_encrypt(p: int, alpha: int, priv_key:int) -> int:
    # compute public key
    pub_key = compute_pub_key(pub_key, p, alpha)
    pass

def DHKE_decrypt():
    pass