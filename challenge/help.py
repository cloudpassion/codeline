class test():
    def assert_equals(self, a,b):
        if a == b:
            print('PASS', ': ', str(a), str(b))
        else:
            print('BADZ', ': ', str(a), str(b))
