from math_things import *
from AES_tables import *

NUM_ROUNDS = 10
x = sp.symbols("x")
AES_POLY = sp.Poly(x**8 + x**4 + x**3 + x + 1, domain=sp.GF(2**8))

def pad_to(instr: str, length: int) -> str:
    """
    Pads a string to a certain length. Will return the original bits if length >= len(bin)

    :param instr: The input  string
    :param length: The length to pad to
    :return padded_str: The padded bits
    """

    if len(instr) < length:
        # if LOGGING:
        #     log(f"{bin=} padded to {("0" * (length-len(bin)) + bin)}")
        return "0" * (length-len(instr)) + instr
    else:
        return instr 

def do_s_box(data_byte: str):
    """
    Does the S-Box

    :param byte: The byte for the sbox. Expects 0xXY
    :return mod_byte: The multiplicative inverse of the byte with the AES polynomial
    """
    b1 = int(data_byte[0], 16)
    b2 = int(data_byte[1], 16)
    return f"{AES_INV_TAB[b1][b2]:x}".zfill(2)

def byte_sub(bytes_full: int) -> str:
    """
    Does the byte substitution layer in an AES round

    :param bytes_full: The bytes in a list after their
    """
    bytes_full = f"{bytes_full:x}"
    bytes_full = bytes_full.zfill(64)
    bytes_split = split_bits(bytes_full, per_group=2)
    for i, byte in enumerate(bytes_split):
        bytes_split[i] = do_s_box(byte)
    out_bytes = "".join(n for n in bytes_split)
    return out_bytes

def g_func(input_bytes: int, round: int):
    """
    Does the AES g function

    :param input_bytes: The input bytes
    :param round: The current round number
    :return out: The output hex value of the g function
    """
    input_bytes_str = f"{input_bytes:x}".zfill(8)
    input_bytes_split = split_bits(input_bytes_str, num_groups=4)
    for b in range(len(input_bytes_split)):
        input_bytes_split[b] = do_s_box(input_bytes_split[b+1%4])
    input_bytes_split[0] += G_FUNC_ROUND_COEFFS[round]
    out = "".join(b for b in input_bytes_split).zfill(8)
    return int(out, 16)

def compute_keys(init_key: int) -> list[int]:
    """
    Computes all of the round keys for AES

    :param init_key: The initial key
    :return round_keys: A list of the round keys for encryption of AES
    """
    init_key_str = f"{init_key:x}".zfill(4)
    init_split = split_bits(init_key_str, num_groups=4)
    round_keys = []
    w0, w1, w2, w3 = int(init_split[0], 16), int(init_split[1], 16), int(init_split[2], 16), int(init_split[3, 16])
    round_keys.append(init_split)
    for _ in range(NUM_ROUNDS):
        w4 = w0 ^ g_func(w3)
        w5 = w4 ^ w1
        w6 = w5 ^ w2
        w7 = w6 ^ w3
        round_keys.append([w4, w5, w6, w7])
        w0, w1, w2, w3 = w4, w5, w6, w7
    return round_keys

def do_round(n: int):
    pass

def shift_rows(bytes: bytearray):
    pass

def mix_column(col: list[int], inv: bool = False):
    """
    Does the mix column part of AES

    :param col: The column to do it on
    :param inv: If should do the inverse mix col or not, false by default
    :return res: The resulting column
    """
    res = []
    for row in MIX_COL_CONST if not inv else INV_MIX_COL_CONST:
        vals = []
        for i, num in enumerate(row):
            vals.append(hex_poly_mult(col[i][0], num))
        res.append([vals[0] ^ vals[1] ^ vals[2] ^ vals[3]])
    return res

def key_addition(data_bytes: str, key_bytes: str) -> str:
    """
    Does the key addition step (bytes xor key)

    :param bytes: The data bytes
    :param key_bytes: The key bytes
    """
    return str(int(data_bytes, 16) ^ int(key_bytes, 16)).zfill(64)

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
    else:
        num_groups = len(bits)//per_group

    for group_num in range(num_groups):
        groups.append(bits[(group_num*per_group):((group_num+1)*per_group)])

    if keep_extra and num_groups*per_group != len(bits):
        num_extra = len(bits) % per_group
        groups.append(bits[-num_extra:])

    return groups

def AES_128_encrypt(plaintext: str):
    ciphertext = ""
    
    # split into 128 bit blocks
    blocks = split_bits(plaintext, per_group=128, keep_extra=True)
    blocks[-1] = str(blocks[-1]).zfill(128)
    
    # compute keys
    keys = compute_keys()

    for block in blocks:
        data_bytes = block
        # do key addition
        data_bytes = key_addition(data_bytes, keys[0])

        # do rounds
        for round in range(10):
            data_bytes = byte_sub(data_bytes) # S-box
            data_bytes = shift_rows()
            data_bytes = mix_column() if round != NUM_ROUNDS-1 else data_bytes
            data_bytes = key_addition(data_bytes, keys[round+1])
        ciphertext += data_bytes