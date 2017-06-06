let sh = require('shelljs');
let fs = require('fs');

let filePathExists = filePath => sh.ls(filePath).length > 0;

let fileExists = fileName => sh.ls('.').includes(fileName);

let isDirectory = filePath => fs.lstatSync(filePath).isDirectory();

module.exports = {
	filePathExists,
	fileExists,
	isDirectory
};