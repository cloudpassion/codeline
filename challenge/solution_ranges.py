import help

Test = help.test()

# aaaaa its hard for me
# need watch how other people solve this task

def solution(args):

    _ret = []
    args.append(0)
    args.append(0)
    n = 0
    while True:
        try:
            cur = args[n]
        except: break

        try:
            new = args[n+1]
        except: break

        rz = new - cur
        if rz == 1:
            cur_safe = cur
            p = 1
            app = [ cur ]
            while rz == 1:

                p += 1
                cur = args[n+1]
                new = args[n+2]

                app.append(cur)
                rz = new - cur
                n += 1

            if p >= 3:
                _ret.append(str(cur_safe)+'-'+str(cur))
            else:
                for a in app:
                    _ret.append(str(a))

        else:
            _ret.append(str(cur))

        n += 1

    return ','.join(_ret[0:-1])


Test.describe("Sample Test Cases")

Test.it("Simple Tests")
Test.assert_equals(solution([-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20]), '-6,-3-1,3-5,7-11,14,15,17-20')
Test.assert_equals(solution([-3,-2,-1,2,10,15,16,18,19,20]), '-3--1,2,10,15,16,18-20')