def compute_pub_key(priv_key: int, p: int, alpha: int) -> int:
    A = alpha**priv_key%p
    return A

def compute_common_key(priv_key: int, other_pub_key: int, p: int) -> int:
    B = other_pub_key**priv_key%p
    return B

def check_common_keys(priv1:int, pub1:int, priv2:int, pub2:int, p:int) -> bool:
    return compute_common_key(priv1, pub2, p) == compute_common_key(priv2, pub1, p)

def compute_priv_key(alpha, d, ring):
    priv_key = pow(alpha, d, ring)
    return priv_key

def encrypt(p: int, alpha: int, priv_key:int) -> int:
    # compute public key
    pub_key = compute_pub_key(pub_key, p, alpha)
    pass

def decrypt():
    pass