with open("input.txt", "r") as file:
    treelist = list(map(lambda x:x, file.readlines()))

def sol(list):
	x=0
	start=0
	for i in range(1,len(list)):
		start+=3
		if start>30:
			start-=31
		if(list[i][start]=="#"):
			x+=1
	return x


print(f"day 2, solution 1 = {sol(treelist)}")