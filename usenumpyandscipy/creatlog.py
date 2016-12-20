filename = 'F:/log/androidbug/dl/download.log'
import time


def ft():
    return time.strftime("%Y%m%d%H%M%S", time.localtime())


import os
import shutil


def creatlog(filename=filename):
    dir = os.path.dirname(filename)
    if not os.path.exists(filename):
        if not os.path.exists(dir):
            os.makedirs(dir)
    if not os.path.exists(filename):
        open(filename, 'w').close()
    elif os.path.exists(filename):
        filecopy = os.path.join(dir, ft() + ".log")
        shutil.copy(filename, filecopy)


if __name__ == "__main__":
    creatlog()
