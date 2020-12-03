with open("input.txt", "r") as file:
    passlist = list(map(lambda x:x, file.readlines()))

def sol(list):
    x=0
    for i in list:
        num1 = int(i.split("-")[0])
        num2 = int(i.split("-")[1].split(" ")[0])
        sent = i.split(": ")[1]
        lett = i.split(": ")[0].split(" ")[1]
        if (sent[num1-1] == lett)^(sent[num2-1] == lett):
            x+=1
    return x

print(f"day 2, solution 2 = {sol(passlist)}")