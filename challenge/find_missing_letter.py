import help

test = help.test()

def find_missing_letter(chars):
   return [chr(ord(letter)-1) for n, letter in enumerate(chars) if ord(chars[n]) - ord(chars[n-1]) != 1 ][-1]

test.describe("kata tests")
test.it("example tests")
test.assert_equals(find_missing_letter(['a','b','c','d','f']), 'e')
test.assert_equals(find_missing_letter(['O','Q','R','S']), 'P')

