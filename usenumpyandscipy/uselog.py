# -*- coding:utf-8 -*-
import logging

filename = 'F:/log/bigdata/png/download.log'

import creatlog as cl

cl.creatlog(filename)

# 配置日志信息
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%m-%d %H:%M',
                    filename=filename,
                    filemode='w')
# 定义一个Handler打印INFO及以上级别的日志到sys.stderr  
console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
# 设置日志打印格式  
formatter = logging.Formatter('[%(name)s_%(levelname)s]: %(message)s')
console.setFormatter(formatter)
# 将定义好的console日志handler添加到root logger  
logging.getLogger('').addHandler(console)
#  download
dl = logging.getLogger('dl')


def dldebug():
    dl.debug('test')


if __name__ == "__main__":
    dldebug()
