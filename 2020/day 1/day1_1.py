with open("input.txt", "r") as file:
    numlist = list(map(lambda x: int(x), file.readlines()))

def sol(list):
	for i in list:
		if 2020-i in list:
			return (2020-i)*i
			
print(f"day 1, solution 1 = {sol(numlist)}")