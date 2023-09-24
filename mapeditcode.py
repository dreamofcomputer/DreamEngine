hn=input("行数>")
def mapget():
    import linecache
    maplist=["","","","","","","","","","","","","","",""]
    trueh=int(hn)-1
    rh=0
    gh=0
    while rh<=trueh:
        maplist[rh]=linecache.getline(r"../map/map.txt",rh+1)
        rh=rh+1
    while gh<=trueh:
        gaitxt=maplist[gh]
        gaitxt=list(gaitxt)
        del gaitxt[len(gaitxt)-1]
        gaitxt="".join(gaitxt)
        maplist[gh]=gaitxt
        gh=gh+1
    return maplist
def gethn():
    return hn