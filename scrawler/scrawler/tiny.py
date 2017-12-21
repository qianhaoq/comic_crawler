import json
import os
import requests
import re
import logging
import time

dir_path = '%s/tinyData/' % (os.getcwd())
if not os.path.exists(dir_path):
    os.makedirs(dir_path)

log_fd = open('tiny.log','a+')
with open('pokemon_list8', 'r') as f:
    while True:
        line = f.readline()
        if not line:
            break
        data = json.loads(line)
        print(data['number'])
        item_path = dir_path + data['number'] + '/'
        if not os.path.exists(item_path):
            os.makedirs(item_path)
        for idx, url in enumerate(data['image_urls'],1):
            print(url)
            try:
                ir = requests.get(url)
            except Exception as err:
                time_now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                log_fd.write(str(time_now) + "; Requests ERROR; " + str(err) + "; " + data['number'] + "; " + url + '\n')
                continue
            if ir.status_code == 200:
                flag = 0
                raw_filetype = url.split(".")[-1]
                type_list = ["jpg", "png", "gif", "jpeg", "JPG", "JPEG", "PNG", "GIF"]
                for type_item in type_list:
                    filetype = re.search(type_item, raw_filetype, flags=0)
                    if filetype:
                        break
                if not filetype:
                    filetype = raw_filetype
                    flag = 1

                if flag == 0:
                    filename = item_path + str(idx) + "." + filetype.group(0)
                else:
                    filename = item_path + str(idx) + "." + filetype
                print(filename)
                try:
                    open(filename, 'wb').write(ir.content)
                except Exception as err: #捕捉其余类型异常 
                    time_now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                    log_fd.write(str(time_now) + "; Requests ERROR; " + str(err) + "; " + data['number'] + "; " + url + '\n')
                    # print("ERROR:can't save pic" + filename) 
log_fd.close()
