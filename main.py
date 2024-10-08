from LFSRs import *
from text_ciphers import *
from math_things import *
from DES import *


def hw1():
    print(find_mod_inverse(7, 26))
    print(affine_decrypt("zuqtqgsytqvrsdqztwvaoyajramjazi", 7, 22))
    pass

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

    print(f"gcd(1072,224) = {gcd_show(1072,224)}")



def main():
    # hw1()
    # hw2()
    # hw3()
    #wkst_temp()
    exam1()



if __name__ == "__main__":
    main()