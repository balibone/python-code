import math


def find_nb(m):
    # sum of n cube terms has the formula (n(n+1)/2)^2
    root_of_vol = math.sqrt(m)
    if not root_of_vol.is_integer():
        return -1
    # NOTE: even if total volume is a square number, does not mean you will have
    # a working N.

    # solve for n where n^2+n-2(root_of_vol) = 0
    a = 1
    b = 1
    c = -2*root_of_vol
    discriminant = (b**2) - (4*a*c)
    n = int((-b + math.sqrt(discriminant))/(2*a))

    # even after solving for positive N, there is a chance it might not work back to the total volume.
    # 2 reasons: 1) it might have decimal points & 2) buggy test cases
    if ((n * (n + 1)) // 2) ** 2 == m:
        return n
    return -1
