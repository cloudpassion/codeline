import help

Test = help.test()

def valid_parentheses(string):
    new_string = ''.join([ l for l in string if l == '(' or l == ')'])
    while '()' in new_string:
        new_string = new_string.replace('()', '')
    return True if new_string == '' else False

Test.assert_equals(valid_parentheses("  ("),False)
Test.assert_equals(valid_parentheses(")test"),False)
Test.assert_equals(valid_parentheses(""),True)
Test.assert_equals(valid_parentheses("hi())("),False)
Test.assert_equals(valid_parentheses("hi(hi)()"),True)
