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

def compute_keys():
    pass

def do_round(n: int):
    pass

def shift_rows(bytes: bytearray):
    pass

def mix_column():
    pass

def key_addition(bytes: bytes, key_bytes: bytes) -> bytes:
    return bytes ^ key_bytes

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
    blocks[-1] = pad_to(blocks[-1], 128)
    
    # compute keys
    keys = compute_keys()

    for block in blocks:
        bytes = block
        # do key addition
        bytes = key_addition(bytes, keys[0])

        # do rounds
        for round in range(10):
            bytes = shift_rows()
            bytes = mix_column() if round != 9 else None
            bytes = key_addition(bytes, keys[round+1])
        ciphertext += bytes