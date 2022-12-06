import { readFileSync } from "fs";

let data = readFileSync("./input_1.txt", { encoding: "utf8", flag: "r" });

const lenOfMarker = 4;

function updateMap(map, addChr, rmChr) {
	if (map.has(addChr)) {
		map.set(addChr, map.get(addChr) + 1)
	} else {
		map.set(addChr, 1);
	}
	if (rmChr) {
		if (map.get(rmChr) === 1) {
			map.delete(rmChr);
		} else {
			map.set(rmChr, map.get(rmChr) - 1);
		}
	}
}

function findMarker(data, lenOfMarker) {
	let index = lenOfMarker;
	const chars = new Map();
	for (let i = 0; i < lenOfMarker; i++) {
		updateMap(chars, data[i]);
	}
	while (index < data.length) {
		if (chars.size === lenOfMarker) {
			return index;
		} else {
			updateMap(chars, data[index], data[index - lenOfMarker]);
			index++;
		}
	}
	return -1;
}

console.log(findMarker(data, lenOfMarker));
