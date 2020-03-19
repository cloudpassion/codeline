import re
import help

test = help.test()

def validBraces(string):

    last_brace = []
    equal = { ')': '(', '}': '{', ']': '[' }

    if not re.search('[\)\}\]]', string) or not re.search('[\(\{\[]', string):
        return False
    for brace in string:
        if re.search('[\)\}\]]', brace):
            try:
                if equal[brace] != last_brace[-1]:
                   return False
                else: last_brace = last_brace[0:-1]
            except: return False
        if re.search('[\(\{\[]', brace):
            last_brace.append(brace)

    return True

test.assert_equals(validBraces("()"), True);
test.assert_equals(validBraces("[(])"), False);
test.assert_equals(validBraces("([()])"), True);
test.assert_equals(validBraces("({][({})])"), False);
test.assert_equals(validBraces("}({}()[][({})])"), False);
test.assert_equals(validBraces("((((("), False);
test.assert_equals(validBraces("}}})))]]]))"), False);
test.assert_equals(validBraces("(){}[]"), True);
