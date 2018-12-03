
import time
import os
import re
import requests
from lxml import etree

from aip import AipFace

APP_ID="15030397"
API_KEY="qWrEVYLmjb5ozCmlt3uxznOE"
SECRET_KEY="DQcKtYhvB8KB6mITplg0XZSHwtQZgsoA"

DIR ="./beatiful_girl"
BEAUTY_THRESHOLD=45

AUTHORIZATION=""

LIMIT=10

SOURCE="19552207"
USEr_AGENT="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36"




















##获取每日bing首页图片壁纸
# import urllib.request
# import requests
# import os.path
#
# def save_img(img_url,dirname):
#     try :
#         if not os.path.exists(dirname):
#             print('文件夹',dirname,'不存在，重新建立')
#             os.makedirs(dirname)
#         #获取图片文件名，包括后缀
#         basename=os.path.basename(img_url)
#         #拼接目录与文件名，得到图片路径
#         filepath=os.path.join(dirname,basename)
#         #下载图片，并保存在文件夹中
#         urllib.request.urlretrieve(img_url,filepath)
#     except  IOError as e:
#         print('文件操作失败',e)
#     except Exception as e :
#         print('错误',e)
#     print('Save ',filepath,'Successfully !\n')
#
#     return  filepath
# #请求网页，跳转到最终img地址
# def get_img_url(raw_img_url="https://area.sinaapp.com/bingImg/"):
#     r=requests.get(raw_img_url)
#     img_url=r.url#得到图片地址的网址
#     print('img_url',img_url)
#     return   img_url
#
# #设置图片绝对路径filepath所指向的图片为壁纸
# # def set_img_as_wallpapper(filepath):
# #     ctypes.windll.user32.SystemParametersInfoW(20, 0, filepath, 0)
#
# def main():
#     dirname='./Image'#图片要保存的位置
#     img_url=get_img_url()
#     filepath=save_img(img_url,dirname)
#     print(filepath)
#
#
# main()

