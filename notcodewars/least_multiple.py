"""
Задача 4: "Наименьшее кратное"

2520 - самое маленькое число, которое делится без остатка на все числа от 1 до 10.

Какое самое маленькое число делится нацело на все числа от 1 до 20?
"""

# https://ru.stackoverflow.com/questions/962369/%D0%9A%D0%B0%D0%BA-%D0%BD%D0%B0%D0%B9%D1%82%D0%B8-%D1%81%D0%B0%D0%BC%D0%BE%D0%B5-%D0%BC%D0%B0%D0%BB%D0%B5%D0%BD%D1%8C%D0%BA%D0%BE%D0%B5-%D1%87%D0%B8%D1%81%D0%BB%D0%BE-%D0%BA%D0%BE%D1%82%D0%BE%D1%80%D0%BE%D0%B5-%D0%B4%D0%B5%D0%BB%D0%B8%D1%82%D1%81%D1%8F-%D0%BD%D0%B0%D1%86%D0%B5%D0%BB%D0%BE-%D0%BD%D0%B0-%D0%B2%D1%81%D0%B5-%D1%87%D0%B8%D1%81%D0%BB%D0%B0-%D0%BE%D1%82-1-%D0%B4%D0%BE-20
def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    print(a)
    return a

def lcm(a, b):
    return a * b // gcd(a, b)     # integer division

d = 1
for i in range(2, 21): #last i=20
    d = lcm(d, i)
    print(d)

def do_find_multiple():
    multiple = 20
    for i in range(20, 20**20, 20):
        all_mult = 0
        for divider in range(1, 21):
            if multiple % divider == 0:
                all_mult += 1
                continue
            else: break
        if all_mult == 20: return multiple
        else: multiple += 20

#print(do_find_multiple())
