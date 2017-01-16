#!/bin/bash
# PATH=/opt/someApp/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
PATH=/home/yong/.virtualenvs/y3/bin:/home/yong/.pyenv/plugins/pyenv-virtualenv/shims:/home/yong/.pyenv/shims:/home/yong/.pyenv/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games

# rest of script follows

source ~/.virtualenvs/y3/bin/activate;
cd /home/yong/Workspace/instagram_video_scrapy;

/home/yong/.virtualenvs/y3/bin/scrapy crawl instavideo &> ./logs/log-scrapy-$(date '+%m-%d-%y')
python3 instagram_video_scrapy/downloadVideos.py &> ./logs/download-log-$(date '+%m-%d-%y')

killall firefox
killall Xvfb
