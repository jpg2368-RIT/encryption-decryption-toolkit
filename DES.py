from DES_tables import *

def split_bits(bits: str, number_per_group: int = -1, number_of_groups: int = -1, keep_extra: bool = False) -> list:
    """
    Splits the input bits into even groups based on either the number per group, or the number of groups. ONLY ONE OF EITHER 'number_per_group' OR 'number_of_groups' MAY BE ENTERED. Will discard any extra at the end by default.

    :param bits: The bits to be split
    :param number_per_group: The number of bits in each group
    :param number_of_groups: The number of groups to split the bits into
    :return groups: The split groups of bits
    """

    #TODO implement keep_extra

    if (number_of_groups==-1 ^ number_per_group==-1):
        raise("Must only enter either number_per_group or number_of_groups, not neither, not both.")
    
    if number_of_groups != -1:
        groups = []
        per_group = len(bits)//number_of_groups
        for group_num in range(number_of_groups):
            groups.append(bits[(group_num*per_group):((group_num+1)*per_group)])
        return groups
    else:
        groups = []
        number_of_groups = len(bits)//number_per_group
        for group_num in range(number_of_groups):
            groups.append(bits[(group_num*number_per_group):((group_num+1)*number_per_group)])
        return groups

def expand(r: str) -> str:
    """
    Does the expansion. Expects 36 bits in and will return 48 bits.

    :param r: The bits to expand
    :return r_exp: The expanded bits
    """

    r_exp = ""
    for i in range(len(E)):
        r_exp += r[i]
    return r_exp

def pad_to(bin: str, length: int) -> str:
    """
    Pads a binary number to a certain length. Will return the original bits if length >= len(bin)

    :param bin: The input binary string
    :param length: The length to pad to
    :return bin: The padded bits
    """

    if len(bin) < length:
        return "0" * (4-len(bin)) + bin
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
    out = bin(out)[2:]
    padded_out = pad_to(out, 4)
    return padded_out

def do_Permutation(bits: str, perm_box: tuple):
    """
    Does a permutation with the input bits

    :param bits: The bits to do the permutation on
    :param perm_box: Which permutation box to use
    :return out: The permutated bits
    """
    
    out = ""
    for i in range(len(perm_box)):
        out += bits[perm_box[i]-1]
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

    #split into 8 chunks of 6 bits
    r_split = split_by_num_groups(r, 6)
    
    # sbox sub on each
    r = ""
    for box_num in range(len(r_split)):
        r += do_S(r_split[box_num], box_num)
        
    # do permutation
    r = do_Permutation(r, f_Perm)

    return r

def do_round(L: str, R: str, key: str):
    """
    Does a round of the encryption
    
    :param L: The left half of the bits
    :param R: The right half of the bits
    :param key: The key for the round
    :return R, l_mod: The swapped L and R halves of the bits after modifications
    """

    # do f with R
    r_mod = f_function(R, key)

    # L xor f
    l_mod = bin(int(L) ^ int(r_mod))[2:]

    # swap L and R and return
    return (R, l_mod)

def DES_encrypt(plaintext: str, key: str) -> str:
    ciphertext = ""
    # TODO break into 64 bit chunks and pad
    chunks = split_by_num_in_group(plaintext, 64)
    chunks[-1] = pad_to(chunks[-1], 64)

    # encrypt each chunk
    for chunk in chunks:
        # do init permutation
        chunk_mod = do_Permutation(chunk, IP)

        # TODO get keys for each round
        keys = []

        # split into L and R
        L = IP[:32], R = IP[32:]

        # do 16 rounds
        for round in range(16):
            L, R = do_round(L, R, keys[round])

        # final permutation
        chunk_mod = do_Permutation(chunk_mod, IP_inv)

        ciphertext += chunk_mod
    return ciphertext

def DES_decrypt(ciphertext, keystream):
    plaintext = ""
    return plaintext