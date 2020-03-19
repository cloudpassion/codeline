import help
test = help.test()

def sum_dig_pow(a, b): # range(a, b + 1) will be studied by the function

    ret = []
    for numI in range(a, b+1):
        summ = sum(int(x)**(i+1) for i, x in enumerate(str(numI)))
        if summ == numI: ret.append(summ)

    return ret

test.describe("Example Tests")
test.assert_equals(sum_dig_pow(1, 10), [1, 2, 3, 4, 5, 6, 7, 8, 9])
test.assert_equals(sum_dig_pow(1, 100), [1, 2, 3, 4, 5, 6, 7, 8, 9, 89])
test.assert_equals(sum_dig_pow(10, 89),  [89])
test.assert_equals(sum_dig_pow(10, 100),  [89])
test.assert_equals(sum_dig_pow(90, 100), [])
test.assert_equals(sum_dig_pow(89, 135), [89, 135])