#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import time
import hashlib


def getmd5(file):
    if not os.path.isfile(file):
        return
    fd = open(file,'rb')
    md5 = hashlib.md5()
    md5.update(fd.read())
    fd.close()
    return md5.hexdigest()


allfile = []
md5list = []
identicallist = []

start = time.time()
inpath = "G:/最新/照片/2018-2019年照片备份/2021年"
# uipath = str(inpath.encode('utf-8'))

# 遍历文件夹下所有的文件
for path,dir,filelist in os.walk(inpath):
    for filename in filelist:
        # print(filename)
        allfile.append(os.path.join(path,filename))

#根据MD5值比较
for photo in allfile:
    md5sum = getmd5(photo)
    if md5sum not in md5list:
        md5list.append(md5sum)
    else:
        identicallist.append(photo)

# 删除重复照片
for idenPhoto in identicallist:
    os.remove(idenPhoto)

end = time.time()
last = end - start

print("identical photos: " + str(len(identicallist)))
print("time: " + str(last) +"s")
print("count: " + str(len(allfile)))

