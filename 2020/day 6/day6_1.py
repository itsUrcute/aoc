with open("input.txt", "r") as file:
    anslist = file.read().split("\n\n")

def sol(slist):
    x=0
    for i in slist:
        slist = [sub.replace('\n', '') for sub in slist]
    for i in slist:
        a = list(i)
        a = list(dict.fromkeys(a))
        x+=len(a)
    return(x)

print(f"day 6, solution 1 = {sol(anslist)}")
