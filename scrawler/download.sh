#!/bin/sh
set -x
# scp -r -P 28908 root@67.218.159.92:/root/git/comic_crawler/scrawler/scrawler/tinyData /home/qh/git/comic_crawler/scrawler/rawData/0_3_8/
# scp -r -P 22 root@45.77.126.21:/root/git/comic_crawler/scrawler/scrawler/tinyData /home/qh/git/comic_crawler/scrawler/rawData/1_7/
# scp -r -P 22 root@207.246.122.70:/root/git/comic_crawler/scrawler/scrawler/tinyData /home/qh/git/comic_crawler/scrawler/rawData/2_6/
# scp -r -P 22 root@139.162.113.67:/root/git/comic_crawler/scrawler/scrawler/tinyData /home/qh/git/comic_crawler/scrawler/rawData/4/
# scp -r -P 22 root@45.33.37.117:/root/git/comic_crawler/scrawler/scrawler/tinyData /home/qh/git/comic_crawler/scrawler/rawData/5/

# banwagong服务器，可直接下载
wget -c -r ftp://67.218.159.92/ -P /home/qh/git/comic_crawler/scrawler/rawData/ &
wait
echo "step 1 done"

# vultr服务器，可直接下载
wget -c -r ftp://45.77.126.21/ -P /home/qh/git/comic_crawler/scrawler/rawData/ &
/usr/bin/proxychains wget -c -r ftp://139.162.113.67/ -P /home/qh/git/comic_crawler/scrawler/rawData/ &

# 等待下载完毕
wait
echo "step 2 done"

# linode日本服务器，不可直接下载，要用proxychains
/usr/bin/proxychains wget -c -r ftp://45.33.37.117/ -P /home/qh/git/comic_crawler/scrawler/rawData/ &
wget -c -r ftp://207.246.122.70/ -P /home/qh/git/comic_crawler/scrawler/rawData/ &
wait
touch "compelte!"
# 45.77.126.21  22 Los Angeles
# 207.246.122.70 22 New Jersey

# linode
# 45.33.37.117 28999 Fremont, CA, USA
# 139.162.113.67 japan

# banwagong
# 67.218.159.92 28908 Los Angeles