from DES_tables import *

def expand(r):
    r_exp = ""
    for i in range(len(E)):
        r_exp += r[i]
    return r_exp

def do_S(bits, sbox_num):
    row = int(f"{bits[0]}{bits[-1]}", 2)
    col = int(bits[1:-1], 2)
    out = SBOX[sbox_num][row][col]
    out = bin(out)[2:]
    if len(out) < 4:
        out = "0" * (4-len(out)) + out
    return out


def f_function(r, key):
    # do expansion
    r = expand(r)

    # do xor with key
    r = bin(r) ^ bin(key)

    #split into 8 chunks of 6 bits
    r_split = [r[0:6], r[6:12], r[12:18], r[18:24], r[24:30], r[30:36], r[36:42], r[42:48]]
    # sbox sub on each
    r = ""
    for box_num in range(len(r_split)):
        r += do_S(r_split[box_num], box_num)
        
    #permutation
    pass

def do_round(L, R):
    # do f with R

    # L xor f
    
    # swap L and R and return
    return R, L

def DES_encrypt(plaintext, key):
    ciphertext = ""
    # break into 64 bit chunks and pad


    # do init permutation
    IP = None

    # do 

    # split into L and R
    L = IP[:32], R = IP[32:]

    # do 16 rounds
    for round in range(16):
        L, R = do_round(L, R)
    return ciphertext

def DES_decrypt(ciphertext, keystream):
    plaintext = ""
    return plaintext