import { readFileSync } from "fs";

const data = readFileSync("./input_1.txt", { encoding: "utf8", flag: "r" });

const rucksacks = data
	.trim()
	.split("\n")
	.map(x => [x.slice(0, x.length / 2), x.slice(x.length / 2)]);

const commonItems = rucksacks.map(x => {
	for (let i of x[0]) {
		if (x[1].includes(i)) {
			return i;
		}
	}
});

const prioritySum = commonItems.reduce((a, v) => {
	const n = v.charCodeAt()
	const numVal = n <= 90 ? n - 38 : n - 96;
	return a + numVal;
}, 0);

console.log(prioritySum);
