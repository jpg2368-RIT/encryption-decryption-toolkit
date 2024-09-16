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

def main():
    # print(find_mod_inverse(7, 26))
    # print(affine_decrypt("zuqtqgsytqvrsdqztwvaoyajramjazi", 7, 22))

    lf1 = LFSR(initstate=[1, 1, 1, 1], fpoly=[4, 3, 2, 1])
    lf1.info()
    lfsr_table(lf1)
    lf1.Viz(title="x^4 + x^3 + x^2 + x + 1 with all 1s")
    print("")

    lf12 = LFSR(initstate=[1, 0, 0, 0], fpoly=[4, 3, 2, 1])
    lf12.info()
    lfsr_table(lf12)
    lf12.Viz(title="x^4 + x^3 + x^2 + x + 1 with all 1s")
    print("")

    lf2 = LFSR(initstate=[1, 1, 1, 1], fpoly=[4, 1])
    lf2.info()
    lfsr_table(lf2)
    lf2.Viz()
    print("")

    lf22 = LFSR(initstate=[1, 0, 0, 0], fpoly=[4, 1])
    lf22.info()
    lfsr_table(lf22)
    lf22.Viz()
    print("")

    lf3 = LFSR(initstate=[1, 1, 1, 1, 1], fpoly=[5, 3, 2])
    lf3.info()
    lfsr_table(lf3)
    lf3.Viz()
    print("")

    lf32 = LFSR(initstate=[1, 0, 0, 0, 0], fpoly=[5, 3, 2])
    lf32.info()
    lfsr_table(lf32)
    lf32.Viz()
    print("")

    lf = LFSR(initstate=[], fpoly=[])
    lf.info()


    # for k in [5, 12, 13]:
    #     print(f"5^-1 in mod {k} = {find_mod_inverse(5, k)}")


    # for n in [[102, 351], [576, 342], [427, 321]]:
    #     i, j = n[0], n[1]
    #     print(f"gcd({i}, {j}) = {gcd(i, j)}")    

if __name__ == "__main__":
    main()