import numpy as np
import math

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
    return -1

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
    
def gcd_show(a: int, b: int):
    """
    Computes the GCD of two numbers and prints the steps as if solving by hand

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