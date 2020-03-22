class test():

    def describe(self, text):
        print(text)
    def it(self, text):
        print(text)

    def assert_equals(self, a,b, *args):
        if a == b:
            print('PASS', ': ', str(a), str(b), str(args))
        else:
            print('BADZ', ': ', str(a), str(b), str(args))
