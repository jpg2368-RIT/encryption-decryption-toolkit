from pylfsr import LFSR

def lfsr_table(l: LFSR, n:int = -1) -> None:
    """
    Prints a table with the run of an LFSR

    :param l: The LFSR to use
    :param n: The amount of runs to do. By default it will run one full max cycle length
    """
    if n == -1:
        n = (2**len(l.state))
    print('count \t state \t\toutbit \t seq')
    print('-'*50)
    for _ in range(n):
        print(l.count,l.state, '', l.outbit,l.seq, sep='\t')
        l.next()
    print('-'*50)
    print('Output: ', l.seq)