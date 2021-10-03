"""
Your task is to construct a building which will be a pile of n cubes. The cube at the bottom will have a volume of n^3, the cube above will have volume of (n-1)^3
and so on until the top
which will have a volume of 1^3.

You are given the total volume m of the building. Being given m can you find the number n of cubes you will have to build?

The parameter of the function findNb (find_nb, find-nb, findNb) will be an integer m and you have to return the integer n such as n^3 + (n-1)^3 + ... + 1^3 = m
if such a n exists or -1 if there is no such n.
Examples:

findNb(1071225) --> 45
findNb(91716553919377) --> -1

"""

def findNbz(m):

    #n^3 + (n-1)^3 + ... + 1^3 = m
    # 45^3 + (45-1)^3 + ... + (2-1)^3 = 1071225
    #1^3 + 2^3 = 9
    #1^3 + 2^3 + 3^3 = 34 (3)
    # 1     8    27  = 36
    # 2-1^3 3-1^3 4-1^3 4^3 = 1 8 27 64 = 100
    # 1     8    27  4^3 = 100
    #

    n = 0
    g = 0
    while g < m:
        g += (n+1)**3
        n += 1

    if g == m: return n
    else: return -1
    return n

def find_nb(m):
    n, p = 0, 0
    #n, p = 1, 1
    f = lambda n: (n+1)**3
    while p < m:
        p += f(n)
        n += 1
    if p == m: return n
    else: return -1

    #_ = [ (n+1)**3 for n in range(0, m) if g > m else n ]

print(find_nb(1071225))
print(find_nb(91716553919377))
print(find_nb(4183059834009))
print(find_nb(24723578342962))
print(find_nb(135440716410000))
print(find_nb(40539911473216))
print(find_nb(26825883955641))
"""
test.assert_equals(find_nb(4183059834009), 2022)
test.assert_equals(find_nb(24723578342962), -1)
test.assert_equals(find_nb(135440716410000), 4824)
test.assert_equals(find_nb(40539911473216), 3568)
test.assert_equals(find_nb(26825883955641), 3218)
"""
