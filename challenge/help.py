class test():

    def describe(self, text):
        print(text)

    def assert_equals(self, a,b):
        if a == b:
            print('PASS', ': ', str(a), str(b))
        else:
            print('BADZ', ': ', str(a), str(b))
