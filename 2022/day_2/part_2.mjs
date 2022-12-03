import { readFileSync } from "fs";

const data = readFileSync("./input_1.txt", { encoding: "utf8", flag: "r" });

const outComeScore = {
	"X": 0,
	"Y": 3,
	"Z": 6
}

const res = {
	"AX": 3,
	"BX": 1,
	"CX": 2,
	"AY": 1,
	"BY": 2,
	"CY": 3,
	"AZ": 2,
	"BZ": 3,
	"CZ": 1
}

const rounds = data.trim().split("\n").map(x => x.split(" "));

const results = rounds.map(x => res[x[0] + x[1]] + outComeScore[x[1]]);

console.log(results.reduce((a, v) => a + v));
