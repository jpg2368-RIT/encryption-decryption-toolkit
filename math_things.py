import numpy as np
from tabulate import tabulate
import math
import sympy as sp
from DES import pad_to
import random

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

def last_n_digits(num: int, n: int) -> str:
    """
    Returns the last n digits of a number mathemetically
    
    :param num: The number
    :param n: How many last digits to get
    """
    return str(num%(10**n)).zfill(n)

def last_n_digits_euler(number:int, n:int) -> str:
    pass

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

def hex_to_poly1d(hex:int) -> np.poly1d:
    """
    Converts a hex (or really any int) to a np.poly1d

    :param hex: The input hex number
    :return poly: The resulting np.poly1d
    """
    b = f"{hex:b}"
    blist = []
    for n in b:
        blist.append(int(n))
    return np.poly1d(blist)

def hex_to_poly(hex: int) -> sp.Poly:
    """
    Converts a hex number to an sp.Poly

    :param hex: The number in hex
    :return poly: The sp.Poly representation of the hex number
    """
    # Convert hex to binary string, remove '0b' prefix, and pad to 8 bits
    bin_rep = bin(hex)[2:].zfill(8)  
    # Create polynomial with coefficients corresponding to binary representation
    poly = sum(int(bit) * sp.symbols('x')**i for i, bit in enumerate(reversed(bin_rep)))
    return sp.Poly(poly, sp.symbols('x'), domain=sp.GF(2))

def poly_to_hex(poly: sp.Poly) -> str:
    """
    Converts an sp.Poly into hex

    :param poly: The sp.Poly
    :return hex_value: The sp.Poly as a hex
    """
    # Get the coefficients in ascending order of powers
    coeffs = poly.all_coeffs()
    # Create a binary string based on coefficients
    binary_str = ''.join(str(int(c)) for c in coeffs)
    # Convert binary string to an integer and then to hex
    hex_value = hex(int(binary_str, 2))
    return hex_value

def eea_for_poly(poly: sp.Poly, irr_poly: sp.Poly = hex_to_poly(0x11b)) -> list:
    """
    Does the Extended Euclidian Algorithm for Polynomials and returns the table

    :param poly: The polynomial to do the EEA on
    :param irr_poly: The irreducible polynomial, the AES irr_poly by default
    :return table: The table of the calculations
    """
    table = []
    num = poly
    denom = irr_poly
    s = 0
    sm1 = 1
    sm2 = 0
    t = 1
    tm1 = 0
    tm2 = 1
    r = None
    q = None
    table.append([None, None, None, None, 1, 0])
    while r != 1:
        q, r = sp.div(num, denom)
        s = sm2 - q * sm1
        t = tm2 - q * tm1
        table.append([num, denom, q, r, s, t])
        num = denom
        denom = r
        sm2 = sm1
        sm1 = s
        tm2 = tm1
        tm1 = t
    return table

def poly_inv(poly: sp.Poly, irr_poly: sp.Poly = hex_to_poly(0x11b), show_table: bool = False, format: str = "fancy_grid") -> sp.Poly:
    """
    Does the multiplicitive inverse of a polynimial using the EEA for polynomials

    :param poly: The polynomial to use
    :param irr_poly: The irreducible polynomial, the AES irr_poly by default
    :param show_table: To display the table of computations or not, false by default
    :param format: The format for the table, fancy_grid by default
    :return res: The multiplicitave inverse of the polynomial
    """
    tab = eea_for_poly(poly, irr_poly)
    res = tab[-1][5]
    if show_table:
        for i, line in enumerate(tab):
            for j, poly in enumerate(line):
                try:
                    tab[i][j] = str(poly.as_expr()).replace("**", "^")
                except:
                    continue
        display_table(tab, ["Dividend (numerator)", "Divisor (denominator)", "Quotient (q)", "Remainder (r)", "s", "t"], format=format)
    return res

def sq_mult_table(n: int, exp: int, mod: int, format = "fancy_grid", show_table: bool = False) -> int:
    """
    Shows the square + multiply table for computing a^b mod n for large numbers
    
    Example:
        5**20 mod 7:\n
        step    bit     sq      mul\n
        1       1       1       5\n
        2       0       4       -\n
        3       1       2       3\n
        4       0       2       -\n
        5       0       4       -\n

    :param n: The base (a in a^b mod n)
    :param exp: The exponent (b in a^b mod n)
    :param mod: What to mod by (n in a^b mod n)
    :param format: The format to print the table with, fancy_grid by default
    :return result: The result of a^b%n
    """

    table = []
    headers = ["Step", "Bit", "SQ", "Mult"]
    bit, sq, mul = None, None, None
    for step in range(len(f"{exp:b}")):
        bit = f"{exp:b}"
        bit = bit[step]
        if step == 0:
            sq = 1
            mul = n
        else:
            sq = mul**2%mod if mul is not None else sq**2%mod
            mul = None if bit == "0" else sq*n%mod
        table.append([step+1, bit, sq, mul])

    print(tabulate(table, headers=headers, tablefmt=format)) if show_table else None
    return mul if mul != None else sq

def poly_mult(p1:sp.Poly, p2:sp.Poly, modp:sp.Poly = hex_to_poly(0x11B)):
    return p1 * p2 % modp

def poly_to_expr(poly: sp.Poly):
    """
    Converts an sp.Poly object to a str with ^ instead of **

    :param poly: The polynomial
    :return: The poly converted to a string
    """
    return str(poly.as_expr()).replace("**", "^")

def hex_poly_mult(poly1: int, poly2: int, mod: int = 0x11B) -> int:
    """
    Multiplies two hex number representations of polynomials mod another polynomial (the AES polynomial by default)

    :param poly1: The first polynomial
    :param poly2: The second polynomial
    :param mod: The polynomial to mod by, the AES poly by default
    :return hex: The hex representation of poly1 * poly2 % mod 
    """
    poly1 = hex_to_poly(poly1)
    poly2 = hex_to_poly(poly2)
    mod = hex_to_poly(mod)
    return int(poly_to_hex(poly1 * poly2 % mod), 16)

def generate_n_bit_prime(n: int, log_fails: bool = False) -> int:
    """
    Generates a prime number with n bits

    :param n: The number of bits for the prime to be
    :param log_fails: If the function should print out the fails
    :return prime_num: The generated prime number
    """
    prime_num = None
    while True:
        nstr = ""
        for _ in range(n):
            nstr += str(random.randint(0,1))
        p_cand = int(nstr, 2)
        if sp.isprime(p_cand):
            prime_num = p_cand
            break
        print(f"Failed: {p_cand}") if log_fails else None
    return prime_num

def PI(nums: list | tuple):
    """
    Summation but for products

    :param nums: List of numbers to multiply together
    :return prod: The product
    """
    prod = 1
    for num in nums:
        prod *= num
    return prod

def crt(nums: list | tuple, in_mod: list | tuple, logging: bool = False, latex_logging: bool = False):
    """
    Does the Chinese Remainder Theorem with numbers.
    x mod M = a_1*b_1*c_1 + ... + a_n*b_n*c_n from a_1 mod m_1 ... a_n mod m_n, M = sum(m_1...m_n)

    :param nums: a_1...a_n
    :param in_mod: m_1...m_n
    :param logging: Will print out the full equation if true, False by default
    :param latex_logging: Will format the log with LaTeX, False by default
    :return x, M: A tuple of the number and what mod it is in (x mod M)
    """
    if len(nums) != len(in_mod):
        raise ValueError("Length of nums and in_mod must be the same")
    if math.gcd(*in_mod) != 1:
        raise ValueError("Elements of in_mod must be coprime")
    log1 = []
    log2 = []
    times = "*" if not latex_logging else " \\cdot "
    num_sum = 0
    M: int = PI(in_mod)
    for i in range(len(nums)):
        a = nums[i]
        c = int(M/in_mod[i])
        b = sp.mod_inverse(c, in_mod[i])
        log1.append(f"({a}{times}{b}{times}{c})")
        log2.append(f"{PI([a,b,c])}")
        num_sum += a*b*c
    x = int(num_sum % M)
    print(*log1, sep=" + ", end=" = ") if logging else None
    print(*log2, sep=" + ", end=" = ") if logging else None
    print(f"{num_sum} {'mod' if not latex_logging else '\\bmod'} {M}", end=" = " if not latex_logging else " \\equiv ") if logging else None
    print(f"{x} {'mod' if not latex_logging else '\\bmod'} {M}") if logging else None
    return x, M

chinese_remainder_theorem = crt

def fermat_primality_test(num: int, runs: int = 1, logging: bool = False):
    """
    Does the Fermat Primality Test

    :param num: The prime candidate to test
    :param runs: The number of times to run the test, each one increasing the probability that the result is correct
    :param logging: Option to output the log of the runs, false by default
    :return: If the number is prime or not based on the test
    """
    for _ in range(runs):
        base = random.randint(2, num-2)
        print(f"Testing base {base}: result = ", end="") if logging else None
        calc = sq_mult_table(base, num-1, num)
        print('prime' if calc == 1 else 'not prime') if logging else None
        if calc != 1:
            return False
    return True

def get_factors(n) -> list:
    """
    Gets all factors of a number

    :param n: The number to get factors of
    :return factor_list: The list of factors
    """
    factor_list = []
    for i in range(1, n+1):
        if n%i==0:
            factor_list.append(i)
    return factor_list

def is_semi_prime(n) -> bool:
    """
    Determines if a number is a semi-prime, that is, all factors of a number are primes aside from 1 and itself

    :param n: The number to check if it is a semi-prime
    """
    factors = get_factors(n)
    factors.remove(1)
    factors.remove(n)
    for factor in factors:
        if not is_prime(factor):
            return False
    return True

def is_carmichael_number(num: int) -> bool:
    """
    Checks if a number is a Caarmichael

    :param num: The number to check
    """
    if num%2==0:
        return False
    # check up to sqrt(n)
    p_factors = get_prime_factors(math.ceil(math.sqrt(num)))
    #TODO finish carmichael num

def is_generator(num: int, ring: int) -> bool:
    """
    Checks if a number is a generator in a ring (same thing as a primitive element)

    :param num: The number to check
    :param ring: The ring to check in
    :return: If the number is a generator in the ring
    """
    return sp.is_primitive_root(num, ring)

def find_generators(ring: int) -> list[int]:
    """
    Finds all generators in a ring. A generator is the same thing as a primitive element

    :param ring: The ring
    :return gens: The list of generators
    """
    return prim_elements_in(ring)

def num_of_generators(ring:int) -> int:
    """
    Calculates the number of generators in a ring

    :param ring: The ring
    :return: The number of generators in the ring
    """
    return euler_totient(euler_totient(ring))

def discrete_log_problem(n: int | float, base: int | float, mod: int, log: bool = False) -> list:
    """
    Finds the value of x to satisfy base^x = n mod mod

    :param n: The target number
    :param base: The base
    :param mod: The ring
    :param log: Logs the output, false by default
    :return: A list of all answers
    """
    print(f"Solving for x in {base}^x = {n} mod {mod}") if log else None
    ans = []
    for x in range(mod):
        num = pow(base, x, mod)
        print(f"{base}^{x} = {num} mod {mod}") if log else None
        if num == n:
            print(f"Solution found: x = {x}") if log else None
            ans.append(x)
    return ans

def nPr(n: int | float, r: int | float):
    """
    Permutation calculation ((n!)/((n-r)!))

    :param n: The n value
    :param r: The r value
    :return: The result
    """
    return (math.factorial(n))/(math.factorial(n-r))

def nCr(n: int | float, r: int | float):
    """
    Combination calculation

    :param n: The n
    :param r: The r
    :return: The result
    """
    return math.factorial(n)/(math.factorial(r)*math.factorial(n-r))

def probability_of_random_prime_up_to_n(n: int):
    return 1/num_primes_up_to_n(n)

def probability_of_random_prime_of_only_n_bits(n: int):
    return 1/num_primes_of_n_bits(n)

def num_primes_up_to_n(n: int):
    """
    Approximates the number of prime numbers up to a number

    :param n: The number to find primes up to
    :return: The number of primes up to n
    """
    return n/math.log(n)

def num_primes_of_n_bits(bits: int):
    """
    Finds the number of primes of only n bits

    :param bits: The number of bits
    :return: The number of primes of only n bits
    """
    below = num_primes_up_to_n(2**(bits-1))
    all = num_primes_up_to_n(2**bits)
    return all - below

def birthday_collision_probability(num_of_people: int) -> float:
    """
    Finds the probability that, with some number of people, there will be multiple people will have the same birthday (assuming 365 days in a year)
    (can only handle up to n=120)
    
    :param num_of_people: The amount of people in the group
    :return: The probability that there will be a collision (multiple people with the same birthday)
    """
    return 1-((nPr(365, num_of_people))/(365**num_of_people))

def num_hash_checked_before_collision(num_bits: int, prob_of_collision: float) -> float:
    """
    Computes how many hashes must be checked before two random vavlues will give the same output

    :param num_bits: The number of bits in the hash function
    :param prob_of_collision: The probability that there will be a collision
    :return: The number of hashes to check before a collision
    """

    return 2**((num_bits+1)/2) * math.sqrt(math.log((1)/(1-prob_of_collision)))

def main():
    # sq_mod_table(5, 20, 7)
    # gcd_show(29, 17)
    # e, e2 = ext_euclid_algo(29, 17)
    # display_table(tuple("a b q r".split()), e, 30)
    # print("")
    # display_table(tuple("x y x\' y\'".split()), e2, 30)
    # crt([1,2,3], [3,5,7], logging=True)
    # p = generate_n_bit_prime(100)
    # p=217839461
    # print(f"{p=}")
    # print(fermat_primality_test(p, 20, True))
    print(num_of_generators(4973))
    pass

if __name__ == "__main__":
    main()