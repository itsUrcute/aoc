with open("input.txt", "r") as file:
    credlist = file.read().split("\n\n")

def sol(list):
    for i in list:
        list = [sub.replace('\n', ' ') for sub in list]

    x=0
    for i in list:
        if len(i.split(" "))<7:
            x+=1
        if len(i.split(" "))>=7:
            for a in i.split(" "):
                if a.startswith("cid") and len(i.split(" "))==7:
                    x+=1
    return len(list)-x

print(f"day 4, solution 1 = {sol(credlist)}")