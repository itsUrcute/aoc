with open("input.txt", "r") as file:
    credlist = file.read().split("\n\n")

for i in credlist:
    credlist = [sub.replace('\n', ' ') for sub in credlist]

x=0
for i in credlist:
    if len(i.split(" "))<7:
        x+=1
    if len(i.split(" "))>=7:
        for a in i.split(" "):
            if a.startswith("cid") and len(i.split(" "))==7:
                x+=1
print(len(credlist)-x)