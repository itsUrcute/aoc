with open("input.txt", "r") as file:
    list = list(map(lambda x: int(x), file.readlines()))

def day1(list):
	for i in list:
		if 2020-i in list:
			return (2020-i)*i
			
def day2(list):
	for i in list:
		for a in list:
			if 2020-i-a in list:
				return((2020-i-a)*a*i)
			
print(f"day 1, solution = {day1(list)}")
print(f"day 2, solution = {day2(list)}")