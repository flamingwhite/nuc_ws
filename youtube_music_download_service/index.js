let fs = require('fs');
let child_process = require('child_process');
let express = require('express');
let url = require('url');


const promisify = (fn, context) => (...params) => new Promise((res, rej) => fn.call(context, ...params, (err, result) => err ? rej(err) : res(result)));

let app = express();

app.get('/:format', (req, res) => {
	console.log(req.body)
	console.log(req.params.format)
	console.log(req.query)
	console.log(req.query.url)
	let path = req.query.url;
	let format = req.params.format;

	let {host} = url.parse(String(req.query.url))
	console.log("roff ", host)
	let temp = host.split('.');
	host = temp[temp.length - 2];
	console.log('host is ', host)

	if(format.indexOf('music') >= 0) {
		return downloadMp3(path)
			.then(() => res.send('Mp3 downloaded'));
	} else if (format.indexOf('video') >= 0) {
		return downloadMp4(path, host) 
			.then(() => res.send('video downloaded'));
	}



});

const downloadMp3 = (path) => {
	return promisify(child_process.exec, child_process)(`cd ~/Dropbox/Youtube_media_programming/music; youtube-dl --extract-audio -o "%(title)s.%(ext)s" --audio-format mp3 ${path}`);
}

const downloadMp4 = (path, host) => {
	// let folder = `~/Dropbox/Youtube_media_programming/${host}`;
	let folder = `/home/yong/Dropbox/Youtube_media_programming/${host}`;

	if(!fs.existsSync(folder)){
		fs.mkdirSync(folder);
	}

	console.log('not find video ', path, 'I will downloading it \n');
	return promisify(child_process.exec, child_process)(`cd /home/yong/Dropbox/Youtube_media_programming/${host}; youtube-dl -o "%(title)s.%(ext)s" ${path}`);
}

app.listen(7000, () => console.log('Youtube download app running on port 7000'));
