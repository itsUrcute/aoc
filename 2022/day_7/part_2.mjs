import { readFileSync } from "fs";

let data = readFileSync("./input_1.txt", { encoding: "utf8", flag: "r" });

class File {
	constructor(name, size, dir, parent = null) {
		this.name = name;
		this.size = size;
		this.dir = dir;
		this.children = [];
		this.parent = parent;
	}
}

class FileSystem {
	constructor() {
		this.head = new File("", 0, true);
		this.current = this.head;
	}

	ls(...files) {
		this.current.children.push(...files);
	}

	cd(dirname) {
		if (dirname === "/") {
			this.current = this.head;
		} else if (dirname === "..") {
			this.current = this.current.parent ? this.current.parent : this.current;
		} else {
			let dir = this.current.children.find(x => x.name === dirname);
			if (!dir) {
				dir = new File(dirname, 0, true, this.current);
				this.current.children.push(dir);
			}
			this.current = dir;
		}
	}

	findSize(node = this.head) {
		node.size += node.children.reduce((a, v) => a + this.findSize(v), 0);
		return node.size;
	}

	findDirToDelete(totalSpace, spaceNeeded, node = this.head) {
		const spaceToDelete = spaceNeeded - (totalSpace - this.head.size);
		const currSpace = node.size >= spaceToDelete && node.dir ? node.size : this.head.size;
		return Math.min(currSpace, ...node.children.map(x => this.findDirToDelete(totalSpace, spaceNeeded, x)))
	}
}

const commands = data.trim().split(/\s*\$\s*/g);

const fs = new FileSystem();

for (let i of commands) {
	if (i.startsWith("cd")) {
		fs.cd(i.split(" ").at(-1));
	} else if (i.startsWith("ls")) {
		const files = i.split("\n");
		const fileData = []
		for (let j = 1; j < files.length; j++) {
			let [size, name] = files[j].split(" ");
			const dir = size === "dir";
			size = dir ? 0 : parseInt(size);
			fileData.push(new File(name, size, dir, fs.current));
		}
		fs.ls(...fileData);
	}
}

fs.findSize();

console.log(fs.findDirToDelete(70000000, 30000000));
