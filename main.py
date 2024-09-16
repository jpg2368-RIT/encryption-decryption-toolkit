from pylfsr import LFSR

from text_ciphers import *
from math_things import *


def lfsr_table(l: LFSR, n:int = -1) -> None:
    if n == -1:
        n = (2**len(l.state))-1
    print('count \t state \t\toutbit \t seq')
    print('-'*50)
    for _ in range(n):
        print(l.count,l.state, '', l.outbit,l.seq, sep='\t')
        l.next()
    print('-'*50)
    print('Output: ', l.seq)

def hw1():
    print(find_mod_inverse(7, 26))
    print(affine_decrypt("zuqtqgsytqvrsdqztwvaoyajramjazi", 7, 22))
    pass

def hw2():
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

    #Q5 TODO: finish this
    # x = "1001001001101101100100100110"
    # y = "1011110000110001001010110001"
    # res = ""
    # for i in range(len(x)):
    #     res += str(int(x[i]) ^ int(y[i]))
    # res = str(res)
    # print(res)
    # for i in range(2):
    #     for j in range(2):
    #         for k in range(2):
    #             on = [i, j, k]
    #             fp = []
    #             for n, c in enumerate(on):
    #                 if c == 1:
    #                     fp.append(3 - n)
    #             if fp != [] and len(fp)>1:
    #                 lf5 = LFSR(initstate=[0,0,1], fpoly=fp)
    #                 lf5.runKCycle(len(res))
    #                 if str(lf5.seq) == res:
    #                     print(f"Found coeffs: {lf5.fpoly}")
    
    
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

def main():
    # hw1()
    hw2()

    # for k in [5, 12, 13]:
    #     print(f"5^-1 in mod {k} = {find_mod_inverse(5, k)}")


   

if __name__ == "__main__":
    main()