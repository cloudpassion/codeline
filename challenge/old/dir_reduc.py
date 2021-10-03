import help

test = help.test()

def dirReduc(arr):

    _ret = []
    b = ''.join(arr)
    for i in range(0,len(arr)):
        b = b.replace('SOUTHNORTH','').replace('NORTHSOUTH','').replace('WESTEAST','').replace('EASTWEST','')

    for z in [ 'SOUTH', 'NORTH', 'WEST', 'EAST' ]:
        b = b.replace(z, z+' ')

    for zz in b.split(' '):
        if zz != '':
            _ret.append(zz.replace(' ',''))

    return _ret

a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
test.assert_equals(dirReduc(a), ['WEST'])
u=["NORTH", "WEST", "SOUTH", "EAST"]
test.assert_equals(dirReduc(u), ["NORTH", "WEST", "SOUTH", "EAST"])