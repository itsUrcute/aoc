with open("input.txt", "r") as file:
    treelist = list(map(lambda x:x, file.readlines()))

def sol(list):
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

print(f"day 2, solution 1 = {sol(treelist)}")