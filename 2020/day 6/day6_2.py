with open("input.txt", "r") as file:
    anslist = file.read().split("\n\n")

def sol(slist):
    x=0
    for i in slist:
        clist = [sub.replace('\n', '') for sub in slist]
    for i in slist:
        tl=list(i)
        mcount=len(i.split("\n"))
        for c in clist:
            for q in c:
                acount = tl.count(q)
                if acount==mcount:
                    x+=1
                while q in tl:
                    tl.remove(q)
    return(x)

print(f"day 6, solution 2 = {sol(anslist)}")
