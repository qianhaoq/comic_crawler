import json
import os
import requests

# f = open('lost.txt', 'r')

dir_path = '%s/tinyData/' % (os.getcwd())
if not os.path.exists(dir_path):
    os.makedirs(dir_path)


with open('items.json', 'r') as f:
    while True:
        line = f.readline()
        if not line:
            break
        data = json.loads(line)
        print(data['number'])
        # print(data['image_urls'])
        item_path = dir_path + data['number'] + '/'
        if not os.path.exists(item_path):
            os.makedirs(item_path)
        for idx, url in enumerate(data['image_urls'],1):
            ir = requests.get(url)
            if ir.status_code == 200:
                filetype = url.split(".")[-1]
                filename = item_path + str(idx) + "." + filetype
                open(filename, 'wb').write(ir.content)


# with open('items_bak.json', 'r') as f:
#     data = json.load(f)









# import re

# f = open('aaaa.html', 'r')
# data = f.read()
# # result = re.search('"ou":"(.*?)","ow":250,',data)
# result = re.findall('"ou":"(.*?)","ow"',data)

# print(len(result))
# print(result[0])
# print(result.group()