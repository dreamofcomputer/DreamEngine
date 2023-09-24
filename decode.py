def printmap_move(x,y,man):
    import gamecode
    import mapeditcode
    mapstr=gamecode.move(x,y,man)
    ph=0
    hn=mapeditcode.gethn()
    trueh=int(hn)-1
    while ph<=trueh:
        print(mapstr[ph])
        ph=ph+1
def printmap_move_dphy_nt(x,y,man,phything):
    import gamecode
    import mapeditcode
    mapstr=gamecode.move_dphy_nt(x,y,man,phything)
    ph=0
    hn=mapeditcode.gethn()
    trueh=int(hn)-1
    while ph<=trueh:
        print(mapstr[ph])
        ph=ph+1
def printmap_move_dphy_yt(x,y,man,phything):
    import gamecode
    import mapeditcode
    mapstr=gamecode.move_dphy_yt(x,y,man,phything)
    ph=0
    hn=mapeditcode.gethn()
    trueh=int(hn)-1
    while ph<=trueh:
        print(mapstr[ph])
        ph=ph+1
def gameprint(printstr):
        print(printstr)