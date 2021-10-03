import help

test = help.test()

def solution(number):
  return sum([ x for x in range(1,number) if x % 3 == 0 or x % 5 == 0])

test.assert_equals(solution(10), 23)
test.assert_equals(solution(16), 60)
