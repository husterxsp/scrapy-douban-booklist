# -*- coding: utf-8 -*-
import json
import random
import os
import errno
import codecs
import sys
import re

reload(sys)
sys.setdefaultencoding('utf-8')

# 文件最后一行的逗号得去掉，不然前端解析json格式不对。。。
for root, dirs, files in os.walk("data"):
    for name in files:
        if os.path.splitext(name)[1] != '.json' or name == 'contents.json':
            continue

        filename = os.path.join(root, name)
        print(filename)
        with codecs.open(filename, 'r+', encoding='utf-8') as f:
            # 先删除最后的逗号
            f.seek(-1, os.SEEK_END)
            f.truncate()
            # 再重新写入
            f.seek(0, 0)
            content = f.read()
            f.seek(0, 0)
            f.write('[' + content + ']')

        # 删除上面写入的 [ ]，恢复原来的格式
        # with open(filename, 'r+') as f:
        #     f.seek(1, os.SEEK_SET)
        #     content = f.read();
        #     f.seek(0, 0)
        #     f.truncate()
        #     f.write(content)

        #     f.seek(-1, os.SEEK_END)
        #     f.truncate()

        #     # 把原来的逗号加进去
        #     f.seek(0, 0)
        #     content = f.read()
        #     f.write(content + ',')
