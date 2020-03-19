def number(bus_stops, ret=0):
    # Good Luck!
    for en,ex in bus_stops: ret += en - ex
    print(ret)
    return ret


number([[10,0],[3,5],[5,8]]) # 5
number([[3,0],[9,1],[4,10],[12,2],[6,1],[7,10]]) # 17
number([[3,0],[9,1],[4,8],[12,2],[6,1],[7,8]]) # 21