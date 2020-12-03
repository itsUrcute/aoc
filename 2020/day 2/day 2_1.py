with open("input.txt", "r") as file:
    passlist = list(map(lambda x:x, file.readlines()))


def sol(list):
	x=0
	for i in list:
		num1 = int(i.split("-")[0])
		num2 = int(i.split("-")[1].split(" ")[0])
		count = i.split(": ")[1].count(i.split(": ")[0].split(" ")[1]) 
		if num1<=count and num2>=count:
			x+=1
	return x


print(f"day 2, solution 1 = {sol(passlist)}")