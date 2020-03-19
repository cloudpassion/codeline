import string
import help
test = help.test()

alphabet = { z: letter for z, letter in zip(string.ascii_lowercase, range(1, len(string.ascii_lowercase)+1)) }
def high(x, h = 0, ret = ''):

    for word in x.split():
            z = sum(alphabet[letter] for letter in word)
            if z > h: h, ret = z, word

    return ret

test.assert_equals(high('man i need a taxi up to ubud'), 'taxi')
test.assert_equals(high('what time are we climbing up the volcano'), 'volcano')
test.assert_equals(high('take me to semynak'), 'semynak')
test.assert_equals(high('tyhwghhnyj vzqvamubfr '), 'tyhwghhnyj')