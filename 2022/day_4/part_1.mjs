import { readFileSync } from "fs";

const data = readFileSync("./input_1.txt", { encoding: "utf8", flag: "r" });

const elfPairs = data
	.trim()
	.split("\n")
	.map(x => {
		const pair = x.split(",");
		return pair.map(x => {
			let [a, b] = x.split("-");
			return [parseInt(a), parseInt(b)];
		});
	});

const containedPairs = elfPairs.filter(x => {
	return (x[0][0] <= x[1][0] && x[0][1] >= x[1][1])
	|| (x[0][0] >= x[1][0] && x[0][1] <= x[1][1]);
}).length;

console.log(containedPairs);
