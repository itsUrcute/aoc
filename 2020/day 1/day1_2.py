with open("input.txt", "r") as file:
    numlist = list(map(lambda x: int(x), file.readlines()))

def sol(list):
	for i in list:
		for a in list:
			if 2020-i-a in list:
				return((2020-i-a)*a*i)

print(f"day 1, solution 2 = {sol(numlist)}")