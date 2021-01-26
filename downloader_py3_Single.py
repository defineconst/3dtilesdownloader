#!/usr/bin/env python coding:utf-8

import io
import gzip
import sys
import traceback
import json
import os
import time
import getopt
import urllib
# from urlparse import urlparse
from urllib.parse import urlparse
from urllib.request import urlretrieve
import urllib.request
# from urllib   import urlretrieve
import codecs
import socket
socket.setdefaulttimeout(300)

# from cStringIO import StringIO

contentsJson = []

def getContents(contents, n):
    global contentsJson
    # 下载content url里的东西
    if n.get('content') is not None:
        c = n['content']
        if c.get('url') is not None:
            contents.append(c['url'])
            if c['url'].find(".json") > -1:
                contentsJson.append(c['url'])

    if n.get('children') is not None:
        children = n['children']
        for i in range(len(children)):
            c = children[i]
            getContents(contents, c) 
    return

# 获取Json记录的瓦片文件
def getContentsOfB3DM(contents, n):
    # 下载content url里的东西
    if n.get('content') is not None:
        c = n['content']
        if c.get('url') is not None:
            if c['url'].find(".b3dm") > -1:
                contents.append(c['url'])

    if n.get('children') is not None:
        children = n['children']
        for i in range(len(children)):
            c = children[i]
            getContents(contents, c) 
    return	

# 获取Json文件八叉树文件
def getContentsJson(contents, n):
    # 下载content url里的东西
    if n.get('content') is not None:
        c = n['content']
        if c.get('url') is not None:
            if c['url'].find(".json") > -1:
                contents.append(c['url'])

    if n.get('children') is not None:
        children = n['children']
        for i in range(len(children)):
            c = children[i]
            getContents(contents, c) 
    return

def gzdecode(data):
    # with patch_gzip_for_partial():
    compressedStream = StringIO(data)
    gziper = gzip.GzipFile(fileobj=compressedStream)
    data2 = gziper.read()

    # print(len(data))
    return data2


def autoDownLoad(url, add):

    try:
        # a表示地址， b表示返回头
        a, b = urlretrieve(url, add)
        keyMap = dict(b)
        if 'content-encoding' in keyMap and keyMap['content-encoding'] == 'gzip':
            #print('need2be decode')
            objectFile = open(add, 'rb+')  # 以读写模式打开
            data = objectFile.read()
            data = gzdecode(data)
            objectFile.seek(0, 0)
            objectFile.write(data)
            objectFile.close()

        return True

    except urllib.error.ContentTooShortError:
        print('Network conditions is not good.Reloading.')
        autoDownLoad(url, add)
    except socket.timeout:
        print('fetch ', url, ' exceedTime ')
        try:
            urlretrieve(url, add)
        except:
            print('reload failed')
    except:
        traceback.print_exc()
    return False


if __name__ == "__main__":

    baseurl = ''
    savedir = ''
    start = 0

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hu:d:s:", [
                                   "url=", "dir=", "start="])
    except getopt.GetoptError:
        print('param error')
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print('python downloader.py  url  dir')
            sys.exit()
        elif opt in ("-u", "--url"):
            baseurl = arg
        elif opt in ("-d", "--dir"):
            savedir = arg
        elif opt in ("-s", "--start"):
            start = int(arg)

    if baseurl == '':
        print('please input url param')

    if savedir == '':
        print('please input dir param')
        sys.exit(2)

    if os.path.isfile(savedir):
        print('savedir can not be a file ', savedir)
        sys.exit(2)

    if not os.path.exists(savedir):
        os.makedirs(savedir)

    print(baseurl)
    uu = urlparse(baseurl)
    print(uu)
    print(uu.path, uu.query)
    # 解析url

    tileseturl = uu.scheme + "://" + uu.netloc + uu.path
    # print(tileseturl)
    if not tileseturl.endswith('.json'):
        # tileseturl += '/tileset.json'
        print('必须添加后缀,如:tileset.json')
        sys.exit(2)

    # baseurl = tileseturl[0:tileseturl.find('tileset.json')]
    baseurl = tileseturl[0:(tileseturl.rfind('/')+1)]
    # print(baseurl)
    # sys.exit(2)

    # tileseturl += '?' + uu.query
    print(tileseturl)

    filename = tileseturl[(tileseturl.rfind('/') + 1):len(tileseturl)]

    print(tileseturl)

    # urllib.URLopener.version = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36 SE 2.X MetaSr 1.0'
    opener = urllib.request.build_opener()
    opener.addheaders = [
        ('User-agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36')]
    urllib.request.install_opener(opener)

    tilesetfile = savedir + "\\" + filename
    print(tilesetfile)
    if not autoDownLoad(tileseturl, tilesetfile):
        sys.exit(2)

    print('download ' + filename + ' success')

    # 解析
    tileset = None
    try:
        f = codecs.open(tilesetfile, 'r', 'utf-8')
        s = f.read()
        f.close()

        tileset = json.loads(s)
    except Exception as e:
        print(e)

    contents = []
    getContents(contents, tileset['root'])
    print(contentsJson)
    
    for i in range(start, len(contents)):
        c = contents[i]

        file = savedir + '/' + c

        dirname = os.path.dirname(file)
        if not os.path.exists(dirname):
            os.makedirs(dirname)

        url = baseurl + c + '?' + uu.query
        if autoDownLoad(url, file):
            print(c + ' download success: ' +
                  str(i+1) + '/' + str(len(contents)))
        else:
            print(c + ' download failed: ' +
                  str(i+1) + '/' + str(len(contents)))
	
	
