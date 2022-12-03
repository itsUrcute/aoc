import { readFileSync } from "fs";

const data = readFileSync("./input_1.txt", { encoding: "utf8", flag: "r" });

const calList = data.trim().split("\n\n").map(x => x.split("\n"));

const calSorted = calList
	.map(x => x.reduce((a, v) => parseInt(v) + a, 0))
	.sort((a,b) => b - a);

console.log(calSorted[0] + calSorted[1] + calSorted[2]);
