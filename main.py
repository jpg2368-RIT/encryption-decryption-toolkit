from LFSRs import *
from text_ciphers import *
from math_things import *
from DES import *
from AES import *
from tests import time_exec


def hw1():
    print(find_mod_inverse(7, 26))
    print(affine_decrypt("zuqtqgsytqvrsdqztwvaoyajramjazi", 7, 22))

def hw2():
    # for k in [11, 12, 13]:
    #     print(f"5^-1 in mod {k} = {find_mod_inverse(5, k)}")
    
    #Q2
    # for i in [[3,2, ], [7,2], [3, 10], [7, 100]]:
    #     j, k = i[0], i[1]
    #     print(f"{j}^{k} = {(j**k) % 13} mod 13")
    
    #Q4
    # lf1 = LFSR(initstate=[1, 1, 1, 1], fpoly=[4, 3, 2, 1])
    # lf1.info()
    # lfsr_table(lf1)
    # lf1.Viz(title="x^4 + x^3 + x^2 + x + 1 with all 1s", show_labels=True)
    # print("")

    # lf12 = LFSR(initstate=[1, 0, 0, 0], fpoly=[4, 3, 2, 1])
    # lf12.info()
    # lfsr_table(lf12)
    # lf12.Viz(title="x^4 + x^3 + x^2 + x + 1 with one 1", show_labels=True)
    # print("")

    # lf2 = LFSR(initstate=[1, 1, 1, 1], fpoly=[4, 1])
    # lf2.info()
    # lfsr_table(lf2)
    # lf2.Viz(title="x^4 + x + 1 with all 1s", show_labels=True)
    # print("")

    # lf22 = LFSR(initstate=[1, 0, 0, 0], fpoly=[4, 1])
    # lf22.info()
    # lfsr_table(lf22)
    # lf22.Viz(title="x^4 + x + 1 with one 1", show_labels=True)
    # print("")

    # lf3 = LFSR(initstate=[1, 1, 1, 1, 1], fpoly=[5, 3, 2])
    # lf3.info()
    # lfsr_table(lf3)
    # lf3.Viz(title="x^5 + x^3 + x^2 + 1 with all 1s", show_labels=True)
    # print("")

    # lf32 = LFSR(initstate=[1, 0, 0, 0, 0], fpoly=[5, 3, 2])
    # lf32.info()
    # lfsr_table(lf32)
    # lf32.Viz(title="x^5 + x^3 + x^2 + 1 with one 1", show_labels=True)
    # print("")

    #Q5?
    # x = "1001001001101101100100100110"
    # y = "1011110000110001001010110001"
    # res = ""
    # for i in range(len(x)):
    #     res += str(int(x[i]) ^ int(y[i]))
    # res = str(res)
    # print(res)
    # l5 = LFSR(initstate=[0, 0, 1], fpoly=[3, 1])
    # lfsr_table(l5, len(x))
    # l5.Viz()
    
    #Q6
    # for n in [4, 5, 9, 26]:
    #     print(f"{n}:")
    #     print(f"\t%phi({n}) = {euler_totient(n)}")
    #     rel_primes = []
    #     for i in range(n):
    #         if gcd(n, i) == 1:
    #             rel_primes.append(i)
    #     print(f"\tRelative primes of {n}: {rel_primes}\n")


    #Q7
    # for n in [[102, 351], [576, 342], [427, 321]]:
    #     i, j = n[0], n[1]
    #     print(f"gcd({i}, {j}) = {gcd(i, j)}") 

    # print("")
    # for n in [[102, 351], [576, 342], [427, 321]]:
    #     i, j = n[0], n[1]
    #     print(gcd_show(i, j))
    #     print("-"*30)
    #     print("")

    #Q8
    # for iter in [928, 929, 932, 933, 934, 935, 936]:
    #     print(f"For {iter}:")
    #     print(euler_totient_temp(iter, True))
    #     print("-"*40)
    pass

def hw3():
    #print(do_round("0"*32, "0"*32, "0"*64))
    pass

def wkst_temp():
    print(f"5^65 mod 7 = {(5**65)%7}")
    print(f"phi of 140, 141, 142 = {euler_totient(140)}, {euler_totient(141)}, {euler_totient(142)}")
    for n in range(16):
        b = pad_to(bin(n)[2:], 4)
        try:
            init = []
            for i in b:
                init.append(int(i))
            l = LFSR(initstate=init, fpoly=[4, 3, 1])
            l.runFullPeriod()
            l.info()
            print("-"*50)
        except:
            continue

def exam1():
    # print(find_mod_inverse(7,14))
    # print(find_mod_inverse(9,14))
    
    # print(do_permutation("01001001010000111110100101000111", f_Perm))
    
    # x1 = "000000"
    # x2 = "101010"
    # print(pad_to(bin(int(do_S(x1, 5),2) ^ int(do_S(x2,5),2))[2:],4)) #idk
    # print(pad_to(do_S(bin(int(x1,2) ^ int(x2,2))[2:], 5),4)) #idk
    
    #print(euler_totient(224, True))
    
    # print(affine_decrypt("QVYJPUIL", 9, 11))
    # print(find_mod_inverse(9, 26))

    # l = LFSR(initstate=[1,0,0,0,0], fpoly=[5, 4])
    # l.info()
    # l.runFullPeriod()
    # l.info()
    # l.Viz()
    # print(f"s6={l.seq[6]}, s9={l.seq[9]}, s12={l.seq[12]}")

    # print(f"Keyspace = {euler_totient(200) * 200}")

    # print(f"gcd(1072,224) = {gcd_show(1072,224)}")
    pass

def hw4():
    #Q1
    # for n in (1033, 1034, 1035, 1036):
    #     print(f"25 mod {n} = {mod_inv(25, n)}")
    #     display_table(ext_euclid_algo(25, n)[0], list("abqr"), format="latex")
    #     display_table(ext_euclid_algo(25, n)[1], ["x", "y", "x\'", "y\'"], format="latex")
    #     print("")

    # Q2
    # print(f"EEA(7111111, 123456) = {mod_inv(7111111, 123456, True)}") # comupte
    # print(find_mod_inverse(7111111, 123456)) # check with brute force

    #Q3
    # for n in (31, 32, 33):
    #     orders = []
    #     for a in range(n):
    #         orders.append((a, order(a, n)))
    #     print(tabulate(orders, headers=["a", f"order(a mod {n})"], tablefmt="latex"))
    #     print(f"{'-'*40}\n")

    # Q4
    # print(prim_elements_in(109)[:2])
    # print(prim_elements_in(113)[-2:])

    # Q5
    # x = sp.symbols("x")
    # field = sp.GF(2)
    # p1 = sp.Poly(x**3 + x + 1, x, domain=field)
    # p2 = sp.Poly(x**3 + x**2 + 1, x, domain=field)
    # modp = sp.Poly(x**4 + x + 1, x, domain=field)
    # print(((p1*p2)%modp).as_expr())

    # Q6
    irr_polys = []
    x = sp.symbols("x")
    for a3 in [0, 1]:
        for a2 in [0, 1]:
            for a1 in [0, 1]:
                for a0 in [0, 1]:
                    poly = sp.Poly(x**4 + a3*x**3 + a2*x**2 + a1*x + a0, x, domain=sp.GF(2))
                    if len(sp.factor_list(poly)[1]) ==  1:
                        irr_polys.append(str(poly.as_expr()).replace("**", "^"))

    print("All irreducible polynomials of degree 4:")
    for p in irr_polys:
        print(f"\t{p}")
    
def hw5():
    # Q1
    # field = sp.GF(2)
    # x = sp.symbols("x")
    # p1 = sp.Poly(x**4 + x + 1, x, domain=field)
    # p2 = sp.Poly(x**7 + x**6 + x**3 + x**2, domain=field)
    # aes_poly = sp.Poly(x**8 + x**4 + x**3 + x + 1, x, domain=field)
    # p2_inv = sp.invert(p2, aes_poly)

    # print(f"Result in GF(2^8) = {poly_to_expr(sp.rem(p1 * p2_inv, aes_poly))}")
    
    # Q2
    # x = sp.symbols('x')
    # field = sp.GF(2)
    # aes_poly = sp.Poly(x**8 + x**4 + x**3 + x + 1, x, domain=field)
    # p1 = sp.Poly(x**7 + x**6 + x + 1, x, domain=field)  # 1100 0011
    # p2 = sp.Poly(x**5 + x**4 + x + 1, x, domain=field)  # 0011 0011

    # product = sp.rem(p1 * p2, aes_poly)
    # print(f"Product in GF(256): {poly_to_expr(product)}")
    
    # Q3
    # poly = hex_to_poly(0x72)
    # ipoly = hex_to_poly(0x11b)
    # res = poly_inv(poly, ipoly, show_table=True)
    # print(f"Inverse of {poly.as_expr()} with P(x) = {ipoly.as_expr()} = {res.as_expr()} = {poly_to_hex(res)}".replace("**", "^"))


    # Q4
    # for n in [0x29, 0xf3]:
    #     print(f"sbox(0x{n:x}) = 0x{do_s_box(f'{n:x}')}")

    # Q5
    # print(f"0x1E * 0x37 mod 0x11B = {hex_poly_mult(0x1E, 0x37)}")

    # Q6
    # col = [[0x87], [0x6E], [0x46], [0xA6]]
    # mc = mix_column(col)
    # for n in mc:
    #     n[0] = hex(n[0])
    # imc = mix_column(col, inv=True)
    # for n in imc:
    #     n[0] = hex(n[0])
    # print(f"Result of mix_col = {mc}")
    # print(f"Result of inv_mix_col = {imc}")

    pass

def exam2():
    # Q2
    print(hex(hex_poly_mult(0xDD, 0xF9)))

    # Q4
    print(mod_inv(999, 101, True)) # wrong?
    print(sp.mod_inverse(999,101))

    # Q5
    print(order(4, 37))

    # Q10
    print(f"Num of prim elements in GF(23): {len(prim_elements_in(23))}")

    # Q13
    inv_col = mix_column([[0xFF], [0x94], [0x9c], [0x6E]], True)
    for i in range(len(inv_col)):
        inv_col[i][0] = hex(inv_col[i][0])
    print(f"{inv_col=}")

    # Q17
    x = sp.symbols("x")
    p = sp.Poly(x + 1, x, domain=sp.GF(2))
    irrp = sp.Poly(x**3 + x + 1, x, domain=sp.GF(2))
    res = poly_inv(p, irrp, True)
    print(f"poly_inv = {res.as_expr()}")

def hw6():
    # Q4
    # print(f"39^39 mod 773 = {sq_mod_table(39, 39, 773, format="latex")}")

    # Q5
    print(f"1234567^23456789 mod 3333337 = {sq_mod_table(1234567, 23456789, 3333337, format='latex')}")

def main():
    # hw1()
    # hw2()
    # hw3()
    #wkst_temp()
    # exam1()
    # hw4()
    # hw5()
    # exam2()
    # hw6()
    pass

if __name__ == "__main__":
    main()