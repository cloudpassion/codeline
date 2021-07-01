"""
http://www.pythonchallenge.com/pc/def/map.html
https://tproger.ru/problems/python-challenge-level-one/

g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr’q
 ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.

    K → M;
    O → Q;
    E → G.
"""

import string
raw = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw\
fylb gq glcddgagclr ylb rfyr’q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq\
pcamkkclbcb. lmu ynnjw ml rfc spj."


def try1():

    text = r''
    for letter in raw:
        if letter in string.ascii_lowercase:
            _ord = ord(letter)
            text += chr(_ord+2) if _ord+2 <= ord('z') else chr(_ord-26+2)
        else:
            text += letter
    return text


def try2():

    def decrypt_letter(letter, offset):

        _ord = ord(letter)
        _dec = chr(_ord + offset) if _ord + offset <= ord('z') else chr(_ord - len(string.ascii_lowercase) + offset)

        return _dec if _dec in string.ascii_lowercase \
            else letter

    def decrypt(word, offset):
        return ''.join([decrypt_letter(x, offset) for x in word])

    def find_offset(word_num=3):

        _word = raw.split(' ')[word_num]
        for i in range(1, len(string.ascii_lowercase)+1):
            _dec = decrypt(_word, i)

    def decrypt_raw():
        return ' '.join([decrypt(word, 2) for word in raw.split(' ')])

    return decrypt_raw()


try1()
try2()

raw = "map"
print(try2())


