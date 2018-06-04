let scraper = require('scraperjs');

scraper.StaticScraper.create('https://movie.douban.com/top250')
	.scrape($ => $('.item .title').map(a => {
		console.log(a);
		console.log($(a).text())
		return $(a).text();
	}).get())
	.then(c => console.log(c));
	