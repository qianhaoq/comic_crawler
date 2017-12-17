comic_crawler
===
# 一个采用`scrapy`框架实现的漫画爬虫
---
运行前准备
- 安装 scrapy

	# 更新
	`sudo apt update && sudo apt upgrade`

	# 安装必要的库
	`sudo apt install python3-pip python3-dev libevent-dev libssl-dev`

	# 安装中文
	`sudo apt-get install language-pack-zh-hans`

	# 设置locale
	`vim /etc/environment`
	## 添加以下2行
	`LANG="zh_CN.UTF-8"`

	`LANGUAGE="zh_CN:zh:en_US:en"`

	# 安装scrapy
	`sudo pip3 install scrapy`

	# 安装pillow
	`sudo pip3 install pillow`

---
运行命令

- `cd comic_crawler/scrawler/scrawler/`
- `scrapy crawl comic `
