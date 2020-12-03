with open("input1.txt", "r") as file:
    alist = list(map(lambda x: int(x), file.readlines()))

with open("input2.txt", "r") as file:
    passlist = list(map(lambda x:x, file.readlines()))

with open("input3.txt", "r") as file:
    treelist = list(map(lambda x:x, file.readlines()))


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
	
def day2_2(list):
    x=0
    for i in list:
        num1 = int(i.split("-")[0])
        num2 = int(i.split("-")[1].split(" ")[0])
        sent = i.split(": ")[1]
        lett = i.split(": ")[0].split(" ")[1]
        if (sent[num1-1] == lett)^(sent[num2-1] == lett):
            x+=1
    return x

def day3(list):
	x=0
	start=0
	for i in range(1,len(list)):
		start+=3
		if start>30:
			start-=31
		if(list[i][start]=="#"):
			x+=1
	return x

def day3_2(list):
	x=0
	y=1
	z=0
	for s in range(1,10,2):
		right=0
		down =1
		if s==9:
			s = 1
			down = 2
		for i in range(1,len(list),down):
			if down==2:
				i+=1
			right+=s
			if right>30:
				right-=31
			if(list[i][right]=="#"):
				x+=1
		q=x-z
		y*=q
		z=x
				
	return y



			
print(f"day 1, solution 1 = {day1(alist)}")
print(f"day 1, solution 2 = {day1_2(alist)}")
print(f"day 2, solution 1 = {day2(passlist)}")
print(f"day 2, solution 2 = {day2_2(passlist)}")
print(f"day 3, solution 1 = {day3(treelist)}")
print(f"day 3, solution 2 = {day3_2(treelist)}")