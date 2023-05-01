
# Algorithm 1.1E

def euclid (m: int, n: int) -> int:
    """
    Calculate the greatest common divisor among positive integers `m` and `n`.
    """
    assert m >= 0 and n >= 0, "m and n must be positive integers"

    r: int = m % n

    while r != 0:
        m = n
        n = r
        r = m % n

    return n
        
if __name__ == "__main__":
    print(euclid(2166, 6099))