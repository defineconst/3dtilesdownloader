


参数
   -u --url  必选，需要下载的3d tiles 地址

   -d --dir  必选，需要保存的目录

   -s --start 可选，默认为0，有时候会下载失败，重新执行的时候可以通过此参数跳过前多少个

示例：

python downloader_py3_multi.py -u https://lab.earthsdk.com/model/702aa950d03
c11e99f7ddd77cbe22fea/tileset.json -d E:\3000_3D_GIS_Cesium\3DTilesFiles\shanghai_building

python downloader.py -u https://beta.cesium.com/api/assets/1458/tileset.json?access_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiIxYmJiNTAxOC1lOTg5LTQzN2EtODg1OC0zMWJjM2IxNGNlYmMiLCJpZCI6NDQsImFzc2V0cyI6WzE0NThdLCJpYXQiOjE0OTkyNjM4MjB9.1WKijRa-ILkmG6utrhDWX6rDgasjD7dZv-G5ZyCmkKg -d c:\gisdata\3dtiles  


python downloader.py -u http://data.marsgis.cn/3dtiles/max-ytlhz/tileset.json -d E:\3000_3D_GIS_Cesium\3DTilesFiles\max-ytlhz  

python downloader.py -u https://lab.earthsdk.com/model/702aa950d03c11e99f7ddd77cbe22fea/tileset.json -d E:\3000_3D_GIS_Cesium\3DTilesFiles\shanghai_building 
 

这个数据里有 392个b3dm，如果下载第100个出错，下次可以从第100个开始重新下载


python downloader.py -u https://beta.cesium.com/api/assets/1458/tileset.json?access_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiIxYmJiNTAxOC1lOTg5LTQzN2EtODg1OC0zMWJjM2IxNGNlYmMiLCJpZCI6NDQsImFzc2V0cyI6WzE0NThdLCJpYXQiOjE0OTkyNjM4MjB9.1WKijRa-ILkmG6utrhDWX6rDgasjD7dZv-G5ZyCmkKg -d c:\gisdata\3dtiles -s 100