import { readFileSync } from "fs";

let data = readFileSync("./input_1.txt", { encoding: "utf8", flag: "r" });

data = data.split("\n\n");

let crates = data[0].split("\n");
const stackCount = crates.pop().trim().split(" ").length;

crates = crates
	.map(x => x.match(/(.{3}).?/gm).map(y => y.trim()))
	.map(x => x.map(y => y ? y[1] : null));

const stacks = Array.from({length: 9}).map(_ => []);

for (let i = crates.length - 1; i >= 0; i--) {
	for (let j = 0; j < stackCount; j++) {
		if (!crates[i][j]) continue;
		stacks[j].push(crates[i][j]);
	}
}

const instructions = data[1].trim().split("\n").map(x => x.match(/\d+/g));

for (let instruction of instructions) {
	const [count, fr, to] = instruction;
	for (let i = 0; i < parseInt(count); i++) {
		stacks[parseInt(to) - 1].push(stacks[parseInt(fr) - 1].pop());
	}
}

console.log(stacks.map(x => x.at(-1)).join(""));
