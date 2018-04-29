# -*- coding: utf-8 -*-
import scrapy
import re
import sys
import os
import random
import json
import codecs
from myspider.items import BookItem

# 修改默认的ASCII编码
reload(sys)
sys.setdefaultencoding('utf-8')


# 全局变量contents 用于记录tag 目录，同时也是check point, 用于中断恢复
# last_url 保存上次请求成功的url
# {
#     '文学': {
#         '小说': 'last_url',
#         '中国小说': 'last_url',
#     }
# }

contents = {}

class DoubanSpider(scrapy.Spider):
    name = "douban"
    
    def start_requests(self):

        global contents

        contestsPath = 'public/data/contents.json'
        if (os.path.exists(contestsPath)):
            with codecs.open(contestsPath, 'r', encoding='utf-8') as f:
                contents = json.loads(f.read())
        
        urls = [
            'https://book.douban.com/tag/',
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    # sys.exit()

    # 处理tag列表
    def parse(self, response):
        # 注意xpath中的[1]表示第一个
        for tag in response.xpath('//div[@class="article"]/div[2]/div'):
            # tag = response.xpath('//div[@class="article"]/div[2]/div[1]')
            tag_name = tag.css('.tag-title-wrapper::attr(name)').extract_first()

            if tag_name not in contents:
                contents[tag_name] = {}

            for sub_tag in tag.css('td'):
                # sub_tag = tag.css('td')[1]
                sub_tag_name = sub_tag.css('a::text').extract_first()
                sub_tag_url = sub_tag.css('a::attr(href)').extract_first()

                if sub_tag_name in contents[tag_name]:
                    last_url = contents[tag_name][sub_tag_name]

                    # 查找之前保存的url
                    start_pos = re.search(r'start=(\d+)', last_url, flags=0)
                    if start_pos is not None:
                        start_pos = str(int(start_pos.group(1)) + 20)
                    else:
                        start_pos = str(20)
                    sub_tag_url = last_url.split('?')[0] + '?start=' + start_pos
                    print(sub_tag_url)

                yield response.follow(sub_tag_url, 
                        self.parse_sub_tag, 
                        meta={
                            'tag_name': tag_name,
                            'sub_tag_name': sub_tag_name,
                        })

    # 处理某个子tag
    def parse_sub_tag(self, response):
        global contents

        tag_name = response.meta.get('tag_name')
        sub_tag_name = response.meta.get('sub_tag_name')

        contents[tag_name][sub_tag_name] = response.url

        for item in response.css('li.subject-item'):

            book = BookItem()
            book['tag_name'] = tag_name
            book['sub_tag_name'] = sub_tag_name
            book['name'] = item.css('.info h2 a::attr(title)').extract_first();
            book['url'] = item.css('.info h2 a::attr(href)').extract_first();
            book['book_id'] = item.css('.info h2 a::attr(href)').re(r'(\d+)')[0];
            # 部分图书暂无评分 None
            book['score'] = float(item.css('span.rating_nums::text').extract_first() or 0);
            book['description'] = item.css('.info p::text').extract_first();
            book['comment_num'] = int(item.css('.star .pl::text').re(r'(\d+)')[0]);

            # 处理description等字段里面的空白空白
            for attr, value in book.items():
                if type(value) is unicode:
                    value = re.sub(re.compile(r'\s+|\n|\t'), '', str(value))
                    book[attr] = value

            yield book

        # next page
        for href in response.css('div.paginator span.next a::attr(href)'):
            yield response.follow(href, 
                        self.parse_sub_tag, 
                        meta={
                            'tag_name': tag_name,
                            'sub_tag_name': sub_tag_name,
                        })

    # scrapy crawl end
    def closed(self, reason):
        with codecs.open('public/data/contents.json', 'w', encoding='utf-8') as f:
            f.write(json.dumps(contents, ensure_ascii=False))

        print('All Closed')
        print(reason)


