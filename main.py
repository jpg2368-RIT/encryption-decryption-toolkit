from LFSRs import *
from text_ciphers import *
from math_things import *
from DES import *
from AES import *
from RSA import *
from DHKE import *
from ElGamal import *
from hashing import *
# import hashlib
from tests import time_exec

def do_q(q_num: int, q_func: callable) -> None:
    """
    Does a question

    :param q_num: The question number
    :param q_func: The function to do for the question
    """
    print(f"Quesion {q_num}:")
    q_func()
    print("-"*100,"\n")

def hw1() -> None:
    print(find_mod_inverse(7, 26))
    print(affine_decrypt("zuqtqgsytqvrsdqztwvaoyajramjazi", 7, 22))

def hw2() -> None:
    for k in [11, 12, 13]:
        print(f"5^-1 in mod {k} = {find_mod_inverse(5, k)}")
    
    #Q2
    def q2():
        for i in [[3,2, ], [7,2], [3, 10], [7, 100]]:
            j, k = i[0], i[1]
            print(f"{j}^{k} = {(j**k) % 13} mod 13")
    do_q(2,q2)
    
    #Q4
    def q4():
        lf1 = LFSR(initstate=[1, 1, 1, 1], fpoly=[4, 3, 2, 1])
        lf1.info()
        lfsr_table(lf1)
        lf1.Viz(title="x^4 + x^3 + x^2 + x + 1 with all 1s", show_labels=True)
        print("")

        lf12 = LFSR(initstate=[1, 0, 0, 0], fpoly=[4, 3, 2, 1])
        lf12.info()
        lfsr_table(lf12)
        lf12.Viz(title="x^4 + x^3 + x^2 + x + 1 with one 1", show_labels=True)
        print("")

        lf2 = LFSR(initstate=[1, 1, 1, 1], fpoly=[4, 1])
        lf2.info()
        lfsr_table(lf2)
        lf2.Viz(title="x^4 + x + 1 with all 1s", show_labels=True)
        print("")

        lf22 = LFSR(initstate=[1, 0, 0, 0], fpoly=[4, 1])
        lf22.info()
        lfsr_table(lf22)
        lf22.Viz(title="x^4 + x + 1 with one 1", show_labels=True)
        print("")

        lf3 = LFSR(initstate=[1, 1, 1, 1, 1], fpoly=[5, 3, 2])
        lf3.info()
        lfsr_table(lf3)
        lf3.Viz(title="x^5 + x^3 + x^2 + 1 with all 1s", show_labels=True)
        print("")

        lf32 = LFSR(initstate=[1, 0, 0, 0, 0], fpoly=[5, 3, 2])
        lf32.info()
        lfsr_table(lf32)
        lf32.Viz(title="x^5 + x^3 + x^2 + 1 with one 1", show_labels=True)
        print("")
    do_q(4,q4)

    #Q5?
    def q5():
        x = "1001001001101101100100100110"
        y = "1011110000110001001010110001"
        res = ""
        for i in range(len(x)):
            res += str(int(x[i]) ^ int(y[i]))
        res = str(res)
        print(res)
        l5 = LFSR(initstate=[0, 0, 1], fpoly=[3, 1])
        lfsr_table(l5, len(x))
        l5.Viz()
    do_q(5,q5)
    
    #Q6
    def q6():
        for n in [4, 5, 9, 26]:
            print(f"{n}:")
            print(f"\t%phi({n}) = {euler_totient(n)}")
            rel_primes = []
            for i in range(n):
                if gcd(n, i) == 1:
                    rel_primes.append(i)
            print(f"\tRelative primes of {n}: {rel_primes}\n")
    do_q(6,q6)


    #Q7
    def q7():
        for n in [[102, 351], [576, 342], [427, 321]]:
            i, j = n[0], n[1]
            print(f"gcd({i}, {j}) = {gcd(i, j)}") 

        print("")
        for n in [[102, 351], [576, 342], [427, 321]]:
            i, j = n[0], n[1]
            print(gcd(i, j, True))
            print("-"*30)
            print("")
    do_q(7,q7)

    #Q8
    def q8():
        for iter in [928, 929, 932, 933, 934, 935, 936]:
            print(f"For {iter}:")
            print(euler_totient_temp(iter, True))
            print("-"*40)
    do_q(8,q8)

def hw3() -> None:
    print(do_round("0"*32, "0"*32, "0"*64))

def wkst4() -> None:
    def q2():
        print(f"5^65 mod 7 = {(5**65)%7}")
    do_q(2,q2)

    def q4():
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
    do_q(3,q3)

def exam1() -> None:
    print(find_mod_inverse(7,14))
    print(find_mod_inverse(9,14))
    
    print(do_permutation("01001001010000111110100101000111", f_Perm))
    
    x1 = "000000"
    x2 = "101010"
    print(pad_to(bin(int(do_S(x1, 5),2) ^ int(do_S(x2,5),2))[2:],4)) #idk
    print(pad_to(do_S(bin(int(x1,2) ^ int(x2,2))[2:], 5),4)) #idk
    
    print(euler_totient(224, True))
    
    print(affine_decrypt("QVYJPUIL", 9, 11))
    print(find_mod_inverse(9, 26))

    l = LFSR(initstate=[1,0,0,0,0], fpoly=[5, 4])
    l.info()
    l.runFullPeriod()
    l.info()
    l.Viz()
    print(f"s6={l.seq[6]}, s9={l.seq[9]}, s12={l.seq[12]}")

    print(f"Keyspace = {euler_totient(200) * 200}")

    print(f"gcd(1072,224) = {gcd(1072,224, True)}")

def hw4() -> None:
    #Q1
    def q1():
        for n in (1033, 1034, 1035, 1036):
            print(f"25 mod {n} = {mod_inv(25, n)}")
            display_table(ext_euclid_algo(25, n)[0], list("abqr"), format="latex")
            display_table(ext_euclid_algo(25, n)[1], ["x", "y", "x\'", "y\'"], format="latex")
            print("")
    do_q(1, q1)

    # Q2
    def q2():
        print(f"EEA(7111111, 123456) = {mod_inv(7111111, 123456, True)}") # comupte
        print(find_mod_inverse(7111111, 123456)) # check with brute force
    do_q(2,q2)

    #Q3
    def q3():
        for n in (31, 32, 33):
            orders = []
            for a in range(n):
                orders.append((a, order(a, n)))
            print(tabulate(orders, headers=["a", f"order(a mod {n})"], tablefmt="latex"))
            print(f"{'-'*40}\n")
    do_q(3,q3)

    # Q4
    def q4():
        print(prim_elements_in(109)[:2])
        print(prim_elements_in(113)[-2:])
    do_q(4,q4)

    # Q5
    def q5():
        x = sp.symbols("x")
        field = sp.GF(2)
        p1 = sp.Poly(x**3 + x + 1, x, domain=field)
        p2 = sp.Poly(x**3 + x**2 + 1, x, domain=field)
        modp = sp.Poly(x**4 + x + 1, x, domain=field)
        print(((p1*p2)%modp).as_expr())
    do_q(5,q5)

    # Q6
    def q6():
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
    do_q(6,q6)
    
def hw5() -> None:
    # Q1
    def q1():
        field = sp.GF(2)
        x = sp.symbols("x")
        p1 = sp.Poly(x**4 + x + 1, x, domain=field)
        p2 = sp.Poly(x**7 + x**6 + x**3 + x**2, domain=field)
        aes_poly = sp.Poly(x**8 + x**4 + x**3 + x + 1, x, domain=field)
        p2_inv = sp.invert(p2, aes_poly)

        print(f"Result in GF(2^8) = {poly_to_expr(sp.rem(p1 * p2_inv, aes_poly))}")
    do_q(1, q1)
    
    # Q2
    def q2():
        x = sp.symbols('x')
        field = sp.GF(2)
        aes_poly = sp.Poly(x**8 + x**4 + x**3 + x + 1, x, domain=field)
        p1 = sp.Poly(x**7 + x**6 + x + 1, x, domain=field)  # 1100 0011
        p2 = sp.Poly(x**5 + x**4 + x + 1, x, domain=field)  # 0011 0011

        product = sp.rem(p1 * p2, aes_poly)
        print(f"Product in GF(256): {poly_to_expr(product)}")
    do_q(2, q2)
    
    # Q3
    def q3():
        poly = hex_to_poly(0x72)
        ipoly = hex_to_poly(0x11b)
        res = poly_inv(poly, ipoly, show_table=True)
        print(f"Inverse of {poly.as_expr()} with P(x) = {ipoly.as_expr()} = {res.as_expr()} = {poly_to_hex(res)}".replace("**", "^"))
    do_q(3,q3)


    # Q4
    def q4():
        for n in [0x29, 0xf3]:
            print(f"sbox(0x{n:x}) = 0x{do_s_box(f'{n:x}')}")
    do_q(4,q4)

    # Q5
    def q5():
        print(f"0x1E * 0x37 mod 0x11B = {hex_poly_mult(0x1E, 0x37)}")
    do_q(5,q5)

    # Q6
    def q6():
        col = [[0x87], [0x6E], [0x46], [0xA6]]
        mc = mix_column(col)
        for n in mc:
            n[0] = hex(n[0])
        imc = mix_column(col, inv=True)
        for n in imc:
            n[0] = hex(n[0])
        print(f"Result of mix_col = {mc}")
        print(f"Result of inv_mix_col = {imc}")
    do_q(6,q6)

def exam2() -> None:
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

def hw6() -> None:
    # Q2
    def q2():
        for m in [8, 10]:
            print(f"{m}:")
            for a in range(m):
                g = gcd(a,m)
                try:
                    mi = sp.mod_inverse(a, m)
                except:
                    mi = "\\text{DNE}"
                e = a**euler_totient(m)%m
                # print(f"\t\\item gcd({a}, {m}) = {g}, ${a}^[-1] \\mod {m} = {mi},\\ {a}^[-1] \\equiv {a}^[\\phi({m})] \\equiv {a}^[{euler_totient(m)}] \\equiv {a**euler_totient(m)} \\equiv {e} \mod {m}  \\implies$ Euler Function {"works" if e == 1 else "does not work"}".replace("[", "{").replace("]", "}"))    
                print(f"\t\\item gcd({a}, {m}) = {g},\\ ${a}^[-1] \\equiv {a}^[\\phi({m})] \\equiv {a}^[{euler_totient(m)}] \\equiv {a**euler_totient(m)} \\equiv {e} \\mod {m}  \\implies$ Euler Function {"holds" if e == 1 else "does not hold"}".replace("[", "{").replace("]", "}"))    
    do_q(2, q2)

    # Q3
    def q3():
        print(euler_totient(26))
    do_q(3, q3)

    # Q4
    def q4():
        print(f"39^39 mod 773 = {sq_mult_table(39, 39, 773, format="latex")}")
    do_q(4, q4)

    # Q5
    def q5():
        print(f"1234567^23456789 mod 3333337 = {sq_mult_table(1234567, 23456789, 3333337, format='latex')}")
    do_q(5,q5)

def hw7() -> None:
    # Q1
    def q1():
        def p1():
            p = 3
            q = 11
            x = 5
            d = 7
            n = p*q
            phi_n = euler_totient(n)
            # e = mod_inv(d, phi_n)
            e = sp.mod_inverse(d, phi_n)
            ct, _ = RSA_encrypt(x, p, q, e)
            print(f"\t{ct=}")
            pt = RSA_decrypt(ct, d, n)
            print(f"\t{pt=}")

        def p2():
            p = 5
            q = 11
            e = 3
            x = 9

            ct, pk = RSA_encrypt(x, p, q, e)
            d = pk
            n = p*q
            print(f"\t{ct=}")
            pt = RSA_decrypt(ct, d, n)
            print(f"\t{pt=}")

        print("part 1:")
        p1()
        print("part 2:")
        p2()
    do_q(1, q1)

    # Q2
    def q2():
        mods = [13, 17]
        crt([1,0], mods, True, latex_logging=True)
        crt([4,5], mods, True, latex_logging=True)
        crt([5,4], mods, True, latex_logging=True)
    do_q(2, q2)

    def q3():
        # part a
        exp = 1536
        print(f"{exp*np.log(2)=}")
        print(f"{2/(exp * np.log(2))=}")
        print(f"1/{exp*np.log(2)/2}")
        print("")

        exp = 2051
        print(f"{exp*np.log(2)=}")
        print(f"{2/(exp * np.log(2))=}")
        print(f"1/{exp*np.log(2)/2}")
    do_q(3, q3)

    def q4():
        for n in [17, 101, 1001]:
            bits = f"{2**n+1:b}"
            # print(f"2**n+1 = {bits}")
            print(f"2**{n} = {len(bits)} bits")
            print("")
    do_q(4, q4)

    # Q5
    def q5():
        chars = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        n = 3763
        e = 11
        cb = generate_RSA_codebook(chars, (n, e))
        print(cb)
        for ct in [2912, 2929, 3368, 153, 3222, 3335, 153, 1222]:
            print(f"{ct} -> {cb[ct]}")
    do_q(5, q5)

    # Q6
    def q6():
        n = 114381625757888867669235779976146612010218296721242362562561842935706935245733897830597123563958705058989075147599290026879543541
        e = 9007
        y = 24102230047908492921334561683677822772379364497905426326274048627460349574761254064237656827652272780749547791945400229075831407
        p = 3490529510847650949147849619903898133417764638493387843990820577
        q = 32769132993266709549961988190834461413177642967992942539798288533
        phi_n = (p-1) * (q-1)
        print(f"{phi_n=}")
        d = sp.mod_inverse(e, phi_n)
        print(f"{d=}")
        plaintext = RSA_decrypt(y, d, n)
        plaintext = str(plaintext)
        plaintext = ("0" + plaintext) if len(plaintext) % 2 != 0 else plaintext
        def convert(pt: str):
            def to_letter(num):
                A_NUM = ord("A")
                l = chr(A_NUM-1 + int(num))
                return l if l != "@" else " "
            ret = ""
            for n in split_bits(pt, per_group=2):
                ret += to_letter(n)
            return ret
        plaintext = convert(plaintext)
        print(f"{plaintext=}")
    do_q(6, q6)

def wkst7() -> None:
    #TODO finish worksheet code
    def q1():
        print(f"a) {math.log(4, 2) % 43 =}")
        print(f"b) {math.log(13, 5) % 43 =}")
        print(f"c) {math.log(2, 4) % 89 =}")
        print(f"d) {math.log(42, 21) % 89 =}")
    do_q(1, q1)

    def q2():
        Z = 31
    do_q(2, q2)

    def q3():
        pass
    do_q(3, q3)

def menu() -> None:
    """
    Prints the main menu
    """
    print("Main Menu")
    print("-"*20)
    print("1. Homework")
    print("2. Worksheet")
    print("3. Exam")
    print("4. Quit")
    print("-"*20)

def runner() -> None:
    """
    Runs the main menu. Will ask user for work type and number and will run the code associated with their selection.
    """
    qtype = None
    while True:
        menu()
        while True:
            try:
                qtype = int(input("Choice: "))
                if 1 <= qtype <= 4:
                    break
            except:
                pass
            print("Invalid input. Please try again.")
        if qtype == 4:
            print("Exiting...")
            return
        num = None
        while True:
            try:
                num = int(input(f"Enter {qtype_dict[qtype]} Number: "))
                break
            except:
                pass
            print("Invalid entry, try again.")
        print("-"*20)
        try:
            (hw_list if qtype==1 else wkst_list)[num-1]()
        except:
            pass
        input("Press enter to return to the main menu")
        print("-"*20)

qtype_dict = {1: "Homework", 2: "Worksheet", 3: "Exam"}
hw_list = [hw1, hw2, hw3, hw4, hw5, hw6, hw7]
wkst_list = [None, None, None, wkst4, None, None, wkst7]
exam_list =[exam1, exam2]

def main():
    runner()

if __name__ == "__main__":
    # if input("Interactive mode? (y/n): ").lower() == "y":
    #     print("Starting interactive mode...\n")
    #     while True:
    #         exec(input(">>> "), globals())
    # else:
    #     main()
    main()