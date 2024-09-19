from DES_S_boxes import *

def f_function(r, key):
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