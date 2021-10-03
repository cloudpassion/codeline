

class Test:

    @staticmethod
    def describe(text):
        print(text)

    @staticmethod
    def it(text):
        print(text)

    @staticmethod
    def assert_equals(a, b, *args):
        if a == b:
            print(f'PASS {a} == {b}, args:{args}')
        else:
            print(f'BADZ {a} != {b}, args:{args}')
