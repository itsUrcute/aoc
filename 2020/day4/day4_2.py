with open("input.txt", "r") as file:
    credlist = file.read().split("\n\n")
def sol(list):
    for i in list:
        list = [sub.replace('\n', ' ') for sub in list]
        tlist=list
    x=0
    for i in list:
        if len(i.split(" "))<7:
            tlist = [sub.replace(i,"") for sub in tlist] 
            x+=1
        if len(i.split(" "))>=7:
            for a in i.split(" "):
                if a.startswith("cid") and len(i.split(" "))==7:
                    tlist = [sub.replace(i,"") for sub in tlist] 
                    x+=1
    while("" in tlist) : 
        tlist.remove("") 
    for q in tlist:
        w = q.split(" ")
        v=1
        for t in w:
            z = t.split(":")
            v=1            
            if z[0]=="byr" and v:
                if not(int(z[1])>=1920 and int(z[1])<=2002):
                    tlist = [sub.replace(q,"") for sub in tlist]
                    v=0

            if z[0]=="iyr" and v:
                if not(int(z[1])>=2010 and int(z[1])<=2020):
                    tlist = [sub.replace(q,"") for sub in tlist] 
                    v=0

            if z[0]=="eyr" and v:
                if not(int(z[1])>=2020 and int(z[1])<=2030):
                    tlist = [sub.replace(q,"") for sub in tlist] 
                    v=0

            if z[0]=="hgt" and v:
                if z[1].endswith("cm"):
                    num = int(z[1].replace("cm",""))
                    if not(num>=150 and num<=193):
                        tlist = [sub.replace(q,"") for sub in tlist]
                        v=0
                elif z[1].endswith("in"):
                    num = int(z[1].replace("in",""))
                    if not(num>=59 and num<=76):
                        tlist = [sub.replace(q,"") for sub in tlist]
                        v=0
                else:
                    tlist = [sub.replace(q,"") for sub in tlist]
                    v=0
            if z[0]=="hcl" and v:
                k=0
                if z[1].startswith("#") and len(z[1])==7:
                    str = z[1].replace("#","")
                    for e in str:
                        if e not in ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"]:
                            k+=1
                if k>0:
                    k=0
                    print("a")
                    tlist = [sub.replace(q,"") for sub in tlist]
                    v=0
                elif len(z[1])!=7:
                    tlist = [sub.replace(q,"") for sub in tlist]
                    v=0    

            if z[0]=="ecl" and v:
                if z[1] not in ["amb","blu","brn","gry","grn","hzl","oth"]:
                    v=0
                    tlist = [sub.replace(q,"") for sub in tlist]

            if z[0]=="pid" and v:
                if len(z[1])!=9:
                    v=0
                    tlist = [sub.replace(q,"") for sub in tlist]
                
            
    while("" in tlist): 
        tlist.remove("") 
    return len(tlist)


print(f"day 4, solution 2 = {sol(credlist)}")