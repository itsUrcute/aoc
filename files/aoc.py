with open("input1.txt", "r") as file:
    alist = list(map(lambda x: int(x), file.readlines()))

with open("input2.txt", "r") as file:
    passlist = list(map(lambda x:x, file.readlines()))


def day1(list):
	for i in list:
		if 2020-i in list:
			return (2020-i)*i
			
def day1_2(list):
	for i in list:
		for a in list:
			if 2020-i-a in list:
				return((2020-i-a)*a*i)

def day2(list):
	x=0
	for i in list:
		num1 = int(i.split("-")[0])
		num2 = int(i.split("-")[1].split(" ")[0])
		count = i.split(": ")[1].count(i.split(": ")[0].split(" ")[1]) 
		if num1<=count and num2>=count:
			x+=1
	return x
	
def day2_1(list):
    x=0
    for i in list:
        num1 = int(i.split("-")[0])
        num2 = int(i.split("-")[1].split(" ")[0])
        sent = i.split(": ")[1].replace("\n","")
        lett = i.split(": ")[0].split(" ")[1]
        if (sent[num1-1] == lett and sent[num2-1] != lett) or (sent[num2-1] == lett and sent[num1-1]!=lett):
            x+=1
    return x


			
print(f"day 1, solution1 = {day1(alist)}")
print(f"day 1, solution2 = {day1_2(alist)}")
print(f"day 2, solution 1 = {day2(passlist)}")
print(f"day 2, solution 2 = {day2_1(passlist)}")