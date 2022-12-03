import { readFileSync } from "fs";

const data = readFileSync("./input_1.txt", { encoding: "utf8", flag: "r" });

const calList = data.trim().split("\n\n").map(x => x.split("\n"));

const highestCal = Math.max(...calList.map(x => x.reduce((a, v) => parseInt(v) + a, 0)));

console.log(highestCal);
