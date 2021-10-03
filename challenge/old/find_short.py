
class test():
    def assert_equals(self, a,b):
        print(a, b)

def find_short(s):
    # your code here
    l = len(s.split()[0])
    for word in s.split():
        if len(word) <= l: l = len(word)
    return l  # l: shortest word length

test = test()
test.assert_equals(find_short("bitcoin take over the world maybe who knows perhaps"), 3)
test.assert_equals(find_short("turns out random test cases are easier than writing out basic ones"), 3)
test.assert_equals(find_short("lets talk about javascript the best language"), 3)
test.assert_equals(find_short("i want to travel the world writing code one day"), 1)
test.assert_equals(find_short("Lets all go on holiday somewhere very cold"), 2)
