import { readFileSync } from "fs";

const data = readFileSync("./input_1.txt", { encoding: "utf8", flag: "r" });

const itemScore = {
	"X": 1,
	"Y": 2,
	"Z": 3
}

const res = {
	"AX": 3,
	"BX": 0,
	"CX": 6,
	"AY": 6,
	"BY": 3,
	"CY": 0,
	"AZ": 0,
	"BZ": 6,
	"CZ": 3
}

const rounds = data.trim().split("\n").map(x => x.split(" "));

const results = rounds.map(x => res[x[0] + x[1]] + itemScore[x[1]]);

console.log(results.reduce((a, v) => a + v));
