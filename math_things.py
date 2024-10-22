import numpy as np
from tabulate import tabulate
import math
import sympy as sp
from DES import pad_to

def is_prime(n: int) -> bool:
    """
    Determines if a number is prime

    :param n: The number to check
    :return: True if prime, false else
    """
    if n < 2:
        return False
    for i in range(2, n):
        if n % i==0:
            return False
    return True

def find_mod_inverse(n:int , k: int = 26) -> int:
    """
    Brute forces the computation of the modular inverse

    :param n: The number to find the inverse of
    :param alph_length: The number to mod by
    :return n_inv: The modular inverse of n within k
    """
    for n_inv in range(k):
        if (n * n_inv) % k == 1:
            return n_inv
    return None

def gcd(a: int, b: int, log: bool = False) -> int:
    """
    Computes the GCD of two numbers

    :param a: Number 1
    :param b: Number 2
    :param log: If the log of hand computation should be printed out
    :return: The GCD of a and b
    """
    if b == 0:
        if log:
            print(a, end=" ")
        return a
    else:
        return gcd(b, a % b, log)
    
def eudlid_algo_show(a: int, b: int):
    """
    Computes the GCD of two numbers using the Euclidean algorithm and prints the steps as if solving by hand

    :param a: Number 1
    :param b: Number 2
    :param log: If the log of hand computation should be printed out
    :return: The GCD of a and b
    """
    n1 = max(a, b)
    n2 = min(a, b)
    r = n1 % n2
    q = n1 // n2
    res = -1
    print(f"q\tn1\tn2\tr")
    print("-"*20)
    while r != 0:
        print(f"{q}\t{n1}\t{n2}\t{r}")
        res = r
        n1 = n2
        n2 = r
        q = n1 // n2
        r = n1 % n2
    print(f"{q}\t{n1}\t{n2}\t{r}")
    return res

def euler_totient_quick(n: int):
    """
    Computes the Euler Totient Function of a number

    :param n: The number to compute
    :return result: The result of the function
    """
    if n == 1:
        return 1
    result = n
    p = 2
    # Check for every number up to the square root of n
    while p * p <= n:
        # Check if p is a divisor of n
        if n % p == 0:
            # If p is a prime factor, apply the formula
            while n % p == 0:
                n //= p
            result -= result // p
        p += 1
    # If n is still greater than 1, then it is a prime number
    if n > 1:
        result -= result // n
    return result

def get_prime_factors(n):
    """
    Gets the prime factors of a positive integer

    :param n: The int to get the prime factors of
    :return prime_factors: A set of the prime factors
    """
    prime_factors = []
    for i in range(2, n):
        if is_prime(i) and n % i == 0:
            prime_factors.append(i)
    return prime_factors

def euler_totient(n: int, log: bool = False) -> int:
    """
    Computes the Euler Totient Function of a number

    :param n: The number to compute
    :param log: If to log steps
    :return res: The result of the function
    """
    if is_prime(n):
        if log:
            print(n, "is prime so reduce by 1 for answer")
        return n-1
    res = n
    prime_factors = []
    for i in range(2, n):
        if is_prime(i) and n % i == 0:
            prime_factors.append(i)
            if log:
                print(f"Prime factor {i} found")
    if log:
        print(f"Final calculation: {n}", end="")
        for i in prime_factors:
            print(f" * (1-(1/{i}))", end="")
        print("")
    for i in prime_factors:
        res *= (1-(1/i))
    return int(res)

def euler_totient_temp(n: int, log: bool = False) -> int:
    """
    Computes the Euler Totient Function of a number

    :param n: The number to compute
    :param log: If to log steps
    :return res: The result of the function
    """
    if is_prime(n):
        if log:
            print(n, "is prime so reduce by 1 for answer")
        return n-1
    res = n
    prime_factors = []
    for i in range(2, n):
        if is_prime(i) and n % i == 0:
            prime_factors.append(i)
            if log:
                print(f"Prime factor {i} found")
    if log:
        print(f"Final calculation: %phi({n}) = {n}", end="")
        for i in prime_factors:
            print(f" times ( 1 - 1 over {i} )", end="")
        print("")
    for i in prime_factors:
        res *= (1-(1/i))
    return int(res)

def ext_euclid_algo(a: int, b: int) -> tuple:
    """
    Does the extended euclidian algorithim

    q = quotient, r = remainder, x = inv(a) mod b, y = inv(b) mod a

    :param a: The first number
    :param b: The second number
    :return (lines, ext_lines): A tuple with the table data of each of the parts of the algorithim
    """

    # do normal euclid algo
    a, b = max(a, b), min(a, b)
    lines = []
    q = -1
    r = -1
    while r != 0:
        q = a//b
        r = a%b
        lines.append((a, b, q, r))
        a = b
        b = r
    lines.append((a, b, None, None))

    # do extended part
    ext_lines = []
    if a == 1: # dont do ext part if a != 1 because there is no mod inverse
        x, y, xp, yp = 1 , 1, 1, 1
        # do it upside down and then flip at end
        xp = a # should be 1
        yp = b # should be 0
        for l in range(len(lines)-1):
            x = yp
            q2 = lines[len(lines)-(l+2)][2] # get q from corresponding line
            y = xp - yp * q2
            ext_lines.append((x, y, xp, yp))
            xp = x
            yp = y
        ext_lines.reverse()
    return lines, ext_lines

def display_table(table_contents, headings, format:str = "fancy_grid", latex_out: bool = False) -> None:
    """
    Displays a table of data using tabulate

    :param table_contents: A 2D list or tuple of the table contents
    :param headings: A list or tuple of each of the headings titles
    :param format: The tabular format to use, fancy_grid by default
    :param latex_out: If the LaTeX table should also be printed, false by default
    """
    # for i in headings:
    #     print(f"{i}\t", end="")
    # print("")
    # print("-"*sep_length)
    # for line in table_contents:
    #     for n in line:
    #         print(f"{n}\t", end="")
    #     print("")
    print(tabulate(table_contents, headers=headings, tablefmt=format))
    if latex_out:
        print(tabulate(table_contents, headers=headings, tablefmt="latex"))

def mod_inv(a: int, b: int, show: bool = False) -> int:
    """
    Calculates the modular/multiplicative inverse of a in mod b

    :param a: a in "a mod b"
    :param b: b in "a mod b"
    :return a_inv: The inverse of a in mod b
    """
    t, table = ext_euclid_algo(a, b)
    if show:
        display_table(t, ["a", "b", "q", "r"])
        display_table(table, ["x", "y", "x\'", "y\'"])
    if table == []:
        return None
    return table[0][1] if table[0][1]>0 else table[0][0]

def roots_test(p: sp.Poly, n: int) -> list:
    """
    Does the roots test and prints the table for a number in Z_n

    :param p: The polynomial to find the roots of with the ring already embedded
    :param n: The ring to be in (Z_n)
    """
    ring = sp.GF(n)
    table = []
    # test inputs
    for i in range(n):
        table.append((i, p.eval(i)))
    print(table)
    
    # check for any 0s -> no 0s = inconclusive, a 0 = is a root
    # for no 0s, check all polynomials up to m//2 (m = degree of initial polyomial)
    #TODO roots_test()

def order(a: int, b: int, log: bool = False) -> int:
    """
    Finds the order of a mod b

    :param a: a in a mod b
    :param b: b in a mod b
    :return order: The order of a mod b
    """
    if log:
        heads = ["k", "a^k", "a^k mod b"]
        table = []
    if gcd(a, b) != 1:
        if log:
            print(f"gcd({a}, {b}) != 1 => order DNE")
        return -1
    else:
        for k in range(1, 2**64):
            if log:
                table.append((k, a**k, a**k%b))
            if (a**k) % b == 1:
                if log:
                    print(f"Table for {a} mod {b}:")
                    print(tabulate(table, headers=heads, tablefmt="fancy_grid"))
                return k
    return -1

def prim_elements_in(z: int) -> list:
    """
    Finds all primitive elements in a ring
    
    :param z: The ring (ints up to z) to check
    :return prims: A list of the primitive elements
    """
    prims = []
    for n in range(z):
        try:
            if sp.is_primitive_root(n, z):
                prims.append(n)
        except:
            continue
    return prims

def last_n_digits(num: int, digits: int):
    """
    Returns the last n digits of a number mathemetically
    
    :param num: The number
    :param digits: How many last digits to get
    """
    return pad_to(str(num%(10**digits)), digits)

def russian_peasant_algo(a: int, b: int, format = "outline", testing = False):
    # a, b = min(a, b), max(a, b)
    table = [[a, b]]
    while b != 0:
        a*=2
        b//=2
        table.append([a, b])
    display_table(table, ["a", "b"], format=format) if not testing else None
    tot = 0
    to_remove = []
    for line in table:
        if line[1]%2==1:
            tot+=line[0]
        else:
            to_remove.append(line)
    for line in to_remove:
        table.remove(line)
    display_table(table, ["a", "b"], format=format) if not testing else None
    return tot


# gcd_show(29, 17)
# e, e2 = ext_euclid_algo(29, 17)
# display_table(tuple("a b q r".split()), e, 30)
# print("")
# display_table(tuple("x y x\' y\'".split()), e2, 30)