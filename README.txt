Python course's homework, just learn scrapy.

myspider/douban.py will crawl douban booklist by tag and will save the item in public/data directory line by line, and then I use public/processjson.py to convert those files to the format of json, so I can read them in the frontend directly.

Run:
1. Delete the public/data directory.(Because the spider save data by formats like JSON Lines)
2. Add available proxy in myspider/middlewares/httpproxy.py.
3. $ scrapy crawl douban
