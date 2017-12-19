#!/usr/bin/python3
import os
import urllib.request
import gzip
import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 伪装User-Agent
header = {}
header['User-Agent'] = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36"

# 设定监控的url
# url = "https://www.google.ca/search?source=lnms&tbm=isch&q=Mismagius&espv=2&biw=1366&bih=667&site=webhp&source=lnms&tbm=isch&sa=X&ei=XosDVaCXD8TasATItgE&ved=0CAcQ_AUoAg"
url = "https://www.google.ca/search?source=lnms&tbm=isch&q=pikachu&espv=2&biw=1366&bih=667&site=webhp&source=lnms&tbm=isch&sa=X&ei=XosDVaCXD8TasATItgE&ved=0CAcQ_AUoAg"
# url = "https://www.baidu.com"

req = urllib.request.Request(url, headers = header)
response = urllib.request.urlopen(req)
data = response.read()
try:
    html = gzip.decompress(data).decode("utf-8")
    print("gzip")
except:
    print("decode")
    html = data.decode("utf-8")

# print(html)
