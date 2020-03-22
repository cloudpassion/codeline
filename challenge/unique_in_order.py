import help

test = help.test()

def unique_in_order(iterable):
    p = [ x for n, x in enumerate(iterable) if n == 0 or iterable[n-1] != x ]
    return p if p or not iterable else list(iterable[0])


test.assert_equals(unique_in_order('AAAABBBCCDAABBB'), ['A','B','C','D','A','B'])
test.assert_equals(unique_in_order('AAAAAAA'), ['A'])
test.assert_equals(unique_in_order([1,2,2,3,3]), [1,2,3])
test.assert_equals(unique_in_order([]), [])
