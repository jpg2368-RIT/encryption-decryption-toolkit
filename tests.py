from math_things import *

order_cases = (
    ((3, 9), -1),
    ((12, 7), 6),
    ((200, 761), 380),
    ((12, 22), -1),
    ((26, 71), 14)
)

def test(func, test_cases: tuple):
    """
    Tests a function with given test cases

    :param func: The function to test
    :param test_cases: A tuple containing a tuple with the arguments of the function and the expected result
    """
    print(f"Testing {func.__name__}():")
    for args, expected_result in test_cases:
        res = func(*args)
        print(f"\t{func.__name__}{args} = {res}", "==" if res == expected_result else "!=", expected_result)
    print("")

def testa(func, test_cases: tuple):
    for args, expected in test_cases:
        assert func(*args) == expected

def main():
    test(order, order_cases)
    testa(order, order_cases)

if __name__ == "__main__":
    main()