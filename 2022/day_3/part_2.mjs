import { readFileSync } from "fs";

const data = readFileSync("./input_1.txt", { encoding: "utf8", flag: "r" });

const rucksacks = data
	.trim()
	.split("\n");

const badges = [];

for (let i = 1; i <= rucksacks.length / 3; i++) {
	const first = rucksacks[(3 * i) - 3];
	for (let j of first) {
		if (rucksacks[(3 * i) - 2].includes(j)
			&& rucksacks[(3 * i) - 1].includes(j)) {
			badges.push(j);
			break;
		}
	}
}

const prioritySum = badges.reduce((a, v) => {
	const n = v.charCodeAt()
	const numVal = n <= 90 ? n - 38 : n - 96;
	return a + numVal;
}, 0);

console.log(prioritySum);
