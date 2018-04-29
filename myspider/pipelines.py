# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import codecs
import json
import os

class MyspiderPipeline(object):
    def process_item(self, item, spider):
        return item

# 只能一次处理一个item？
class JsonWriterPipeline(object):

    # def open_spider(self, spider):

        # self.file = codecs.open('test.jl', 'w', encoding='utf-8')
        # self.file = open('items.jl', 'w')

    # def close_spider(self, spider):
        # self.file.close()

    def process_item(self, item, spider):

        filename = 'public/data/' + item['tag_name'] + '/' + item['sub_tag_name'] + '.json'
        print('process_item: ' + filename)
        if not os.path.exists(os.path.dirname(filename)):
            os.makedirs(os.path.dirname(filename))

        with codecs.open(filename, 'a', encoding='utf-8') as f:
            f.write(json.dumps(dict(item), ensure_ascii=False) + ',\n')

        # lines = json.dumps(dict(item), ensure_ascii=False) + '\n'        
        # self.file.write(lines)
        return item