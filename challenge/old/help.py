

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
            print('PASS', ': ', str(a), str(b), str(args))
        else:
            print('BADZ', ': ', str(a), str(b), str(args))
