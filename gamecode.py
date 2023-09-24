def move(x,y,man):
    import mapeditcode
    mapstr=mapeditcode.mapget()
    ystr=mapstr[y-1]
    ystr=list(ystr)
    ystr[x-1]=man
    ystr="".join(ystr)
    mapstr[y-1]=ystr
    return mapstr
def move_dphy_nt(x,y,man,phything):
    import mapeditcode
    mapstr=mapeditcode.mapget()
    ystr=mapstr[y-1]
    ystr=list(ystr)
    if ystr[x-1]!=phything:
        ystr[x-1]=man
    ystr="".join(ystr)
    mapstr[y-1]=ystr
    return mapstr
def move_dphy_yt(x,y,man,phything):
    import mapeditcode
    mapstr=mapeditcode.mapget()
    ystr=mapstr[y-1]
    ystr=list(ystr)
    if ystr[x-1]==phything:
        ystr[x-1]=man
    ystr="".join(ystr)
    mapstr[y-1]=ystr
    return mapstr