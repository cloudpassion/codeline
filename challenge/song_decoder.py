# my fail. forget what python have split(),replace() and other function to text operating
def song_decoder(_text):
    _ret, _next = '', ''
    n = 0
    ftry = True
    while n < len(_text):

        _next = _text[n:n+3]
        while _next == "WUB":
            n += 3
            try: _next = _text[n:n+3]
            except: break
            continue
        if ftry: ftry = False
        else:
            if _text[n-3:n] == "WUB" and n < len(_text): _ret += ' '
        try: _ret += _text[n]
        except: break
        n += 1
    return _ret

print('|'+song_decoder("WUBWEWUBAREWUBWUBTHEWUBCHAMPIONSWUBMYWUBFRIENDWUB")+'|')
print('|'+song_decoder("AWUBBWUBC")+'|')
print('|'+song_decoder("WUBAWUBBWUBCWUB")+'|')
print('|'+song_decoder("AWUBWUBWUBBWUBWUBWUBC")+'|')
print('|'+song_decoder("WUBWUBWUBWUBABCWUBWUBBCDWUBWUBWUBWUBWUB")+'|')



