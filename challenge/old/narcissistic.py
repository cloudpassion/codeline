import help

test = help.test()

def narcissistic( value ):
    value_string = str(value)
    p = [ int(x)**len(value_string) for x in value_string ]
    #return True if sum(p) == value else False
    return sum(p) == value

test.assert_equals(narcissistic(7), True, '7 is narcissistic');
test.assert_equals(narcissistic(371), True, '371 is narcissistic');
test.assert_equals(narcissistic(122), False, '122 is not narcissistic')
test.assert_equals(narcissistic(4887), False, '4887 is not narcissistic')
