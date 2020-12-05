with open("input.txt", "r") as file:
    seatlist = file.read().split("\n")

def sol(list):
    fl=[]
    k=[]
    o=[0,1,2,3,4,5,6,7]
    for i in range(128):
      k.append(i)
    for i in seatlist:
        seatrow=k
        seatcol=o
        a,b = i[0:7],i[7:10]
        for q in a:
            if q=="F":
                seatrow=seatrow[0:int(len(seatrow)/2)]
            elif q=="B":
                seatrow=seatrow[int(len(seatrow)/2):int(len(seatrow))]
        for w in b:
            if w=="L":
                seatcol=seatcol[0:int(len(seatcol)/2)]
            elif w=="R":
                seatcol=seatcol[int(len(seatcol)/2):int(len(seatcol))]
        fl.append(seatrow[0]*8+seatcol[0])
        fl.sort()
    return fl[-1]

print(f"day 5, solution 1 = {sol(seatlist)}")