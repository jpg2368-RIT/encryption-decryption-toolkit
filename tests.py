from math_things import *
import random

order_cases = (
    ((3, 9), -1),
    ((12, 7), 6),
    ((200, 761), 380),
    ((12, 22), -1),
    ((26, 71), 14)
)

rpalgo_test = []

for i in range(20):
    a, b = random.randint(1, 2**20), random.randint(1, 2**128)
    rpalgo_test.append(((a, b, None , True), a*b))

def test(func, test_cases, log = False):
    """
    Tests a function with given test cases

    :param func: The function to test
    :param test_cases: An iterable (list/tuple) containing a tuple with the arguments of the function and the expected result
    """
    print(f"Testing {func.__name__}():")
    bad = []
    for args, expected_result in test_cases:
        res = func(*args)
        print(f"\t{func.__name__}{args} = {res}", "==" if res == expected_result else "!=", expected_result) if log else None
        if res != expected_result:
            bad.append(f"\t{func.__name__}{args} = {res} != {expected_result}")
    if len(bad) > 0:
        print("Failed cases:")
        for line in bad:
            print(line)
    else:
        print("All tests succeeded")
    print("")

def testa(func, test_cases: tuple):
    for args, expected in test_cases:
        assert func(*args) == expected

def main():
    test(order, order_cases)
    testa(order, order_cases)
    test(russian_peasant_algo, rpalgo_test)

if __name__ == "__main__":
    main()