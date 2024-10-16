from DES_tables import *

def log(s: str):
    with open("log.log", "a") as file:
        file.write(f"{s}\n")

def split_bits(bits: str, per_group: int = -1, num_groups: int = -1, keep_extra: bool = False) -> list:
    """
    Splits the input bits into even groups based on either the number per group, or the number of groups. ONLY ONE OF EITHER 'number_per_group' OR 'number_of_groups' MAY BE ENTERED. Will discard any extra at the end by default.

    :param bits: The bits to be split
    :param per_group: The number of bits in each group
    :param num_groups: The number of groups to split the bits into
    :return groups: The split groups of bits
    """

    if not ((num_groups == -1) ^ (per_group == -1)):
        raise ValueError("Must only enter either number_per_group or number_of_groups, not neither or both.")
    
    groups = []
    if num_groups != -1:
        per_group = len(bits)//num_groups
        if LOGGING:
            log(f"{per_group=}")
    else:
        num_groups = len(bits)//per_group
        if LOGGING:
            log(f"{num_groups=}")

    for group_num in range(num_groups):
        groups.append(bits[(group_num*per_group):((group_num+1)*per_group)])
        if LOGGING:
            log(f"Added group {(bits[(group_num*per_group):((group_num+1)*per_group)])}")

    if keep_extra and num_groups*per_group != len(bits):
        num_extra = len(bits) % per_group
        groups.append(bits[-num_extra:])

    if LOGGING:
        log(f"{groups=}")
    return groups

def expand(bits: str) -> str:
    """
    Does the expansion. Expects 36 bits in and will return 48 bits.

    :param bits: The bits to expand
    :return r_exp: The expanded bits
    """
    if len(bits) != 32:
        raise(ValueError(f"Input bits are wrong length. Expected 32, got {len(bits)}"))
    
    bits_exp = ""
    for i in range(len(E)):
        bits_exp += bits[E[i]-1]
    
    if LOGGING:
        log(f"{bits=} expanded to {bits_exp=}")

    return bits_exp

def pad_to(bin: str, length: int) -> str:
    """
    Pads a binary number to a certain length. Will return the original bits if length >= len(bin)

    :param bin: The input binary string
    :param length: The length to pad to
    :return bin: The padded bits
    """

    if len(bin) < length:
        # if LOGGING:
        #     log(f"{bin=} padded to {("0" * (length-len(bin)) + bin)}")
        return "0" * (length-len(bin)) + bin
    else:
        return bin      

def do_S(bits: str, sbox_num: int):
    """
    Does the SBox substitution. First and last bit choose row, middle bits choose col, look up in SBox for desired round

    :param bits: The input bits
    :param sbox_num: The SBox number to use
    :return padded_out: The padded out bits (len = 4)
    """

    row = int(f"{bits[0]}{bits[-1]}", 2)
    col = int(bits[1:-1], 2)
    out = SBOX[sbox_num][row][col]
    if LOGGING:
        log(f"S_{sbox_num+1}[{row}][{col}] = {out}")
    out = bin(out)[2:]
    padded_out = pad_to(out, 4)
    return padded_out

def do_permutation(bits: str, perm_box: tuple):
    """
    Does a permutation with the input bits

    :param bits: The bits to do the permutation on
    :param perm_box: Which permutation box to use
    :return out: The permutated bits
    """
    
    out = ""
    for i in range(len(perm_box)):
        out += bits[perm_box[i]-1]
    if LOGGING:
        log(f"{bits=} permuted to {out=}")
    return out

def f_function(r: str, key: str):
    """
    Does the f function. Expands, xor with key, SBox substitution, f permutation

    :param r: The bits to fo the function on
    :param key: The key
    :return r: The bits modified by the f function
    """
    # do expansion
    r = expand(r)

    # do xor with key
    r = pad_to(bin(int(r, 2) ^ int(key, 2))[2:], 48)

    if LOGGING:
        log(f"New R = {r}")

    #split into 8 chunks of 6 bits
    r_split = split_bits(r, per_group=6)
    
    # sbox sub on each
    r = ""
    for box_num in range(len(r_split)):
        r += do_S(r_split[box_num], box_num)
        
    # do permutation
    r = do_permutation(r, f_Perm)

    return r

def do_round(l: str, r: str, key: str):
    """
    Does a round of the encryption
    
    :param l: The left half of the bits
    :param r: The right half of the bits
    :param key: The key for the round
    :return r, l_mod: The swapped L and R halves of the bits after modifications
    """

    # do f with R
    r_mod = f_function(l, key)

    # L xor f
    l_mod = pad_to(bin(int(r, 2) ^ int(r_mod, 2))[2:], 32)

    # swap L and R and return
    return (r, l_mod)

def shift_by(bits: str, num: int):
    """
    Shifts bits to the left by the number provided

    :param bits: The bits to shift
    :param num: The number to shift to the left by
    :return: The shifted bits
    """

    if LOGGING:
        log(f"Shifted {bits} to {bits[num:] + bits[:num]}")
    return bits[num:] + bits[:num]

def compute_keys(key: str) -> list:
    """
    Computes the keys for each round of DES

    :param key: The initial key
    :return keys: The list of keys for each round of DES
    """
    keys = []
    init_key_mod = do_permutation(key, PC1)
    C, D = init_key_mod[:28], init_key_mod[28:]
    for i in range(16):
        # do shift
        to_shift = 2
        if i in (0, 1, 8, 15):
            to_shift = 1
        C, D = shift_by(C, to_shift), shift_by(D, to_shift)
        
        # do permutation and add to keys
        keys.append(do_permutation(f"{C}{D}", PC2))
        if LOGGING:
            log(f"Key {i+1} computed as {keys[-1]}")
    return keys

#TODO Fix DES_encrypt
def DES_encrypt(plaintext: str, key: str) -> str:
    ciphertext = ""
    # break into 64 bit chunks and pad
    chunks = split_bits(plaintext, per_group=64)
    chunks[-1] = pad_to(chunks[-1], 64)

    # encrypt each chunk
    for chunk in chunks:
        # do init permutation
        chunk_mod = do_permutation(chunk, IP)

        # compute keys for each round
        key = pad_to(key, 64)
        keys = compute_keys(key)

        # split into L and R
        L, R = chunk_mod[:32], chunk_mod[32:]

        # do 16 rounds
        for round in range(16):
            L, R = do_round(L, R, keys[round])

        # final permutation
        chunk_mod = do_permutation(f"{L}{R}", IP_inv)

        ciphertext += chunk_mod
    return ciphertext

#TODO DES_decrypt
def DES_decrypt(ciphertext, keystream):
    plaintext = ""
    return plaintext

LOGGING = False
# to_encrypt = "0111010001101000011010010111001100100000011010010111001100100000011000010010000001110100011001010111001101110100" # "this is a test"
# key_to_use = "01110100011010000110010100100000011010110110010101111001" # "the key"
# print(DES_encrypt(to_encrypt, key_to_use))
# # should output 01000111011000010001011110000001011100101010100111111100011111111110101011101111011001000001001110100010001011010101011111100011