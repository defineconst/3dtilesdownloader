#!/usr/bin/env python
# coding:utf-8

# from urllib.request import urlretrieve
# import urllib.request 
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
# 			'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
# 			'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
# 			'Accept-Encoding': 'gzip, deflate, br',
# 			'Accept-Language': 'zh-CN,zh;q=0.9',
# 			'Connection': 'keep-alive'}

# url = "http://data.marsgis.cn/3dtiles/max-ytlhz/tileset.json"

# add = "E:/3000_3D_GIS_Cesium/3DTilesFiles/max-ytlhz/tileset.json"

# def reporthook(a, b, c):
#         """
#         显示下载进度
#         :param a: 已经下载的数据块
#         :param b: 数据块的大小
#         :param c: 远程文件大小
#         :return: None
#         """
#         print("\rdownloading: %5.1f%%" % (a * b * 100.0 / c), end="")
		
# # javlib_Request =  urllib.request.Request(url, headers=headers)
# # javlib_urlopen =  urllib.request.urlopen(javlib_Request, timeout=10)
# # b = javlib_urlopen.read().decode('UTF-8')
# opener = urllib.request.build_opener()
# opener.addheaders =  [('User-agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36')]
# urllib.request.install_opener(opener)
# a, b = urllib.request.urlretrieve(url, add , reporthook) 
tileseturl = "https://lab.earthsdk.com/model/702aa950d03c11e99f7ddd77cbe22fea/tileset.json"
index = tileseturl.rfind('tileset.json')
print(str(index))
baseurl = tileseturl[0:(tileseturl.rfind('/')+1)]
print(baseurl)
baseurl = tileseturl[(tileseturl.rfind('/') + 1):len(tileseturl)]
print(baseurl)