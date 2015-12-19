#!/bin/bash

mkdir -p html
set -e

## ja

# hatena
wget -O html/ja_potatostudio.hatenablog.com.html http://potatostudio.hatenablog.com/entry/2015/12/17/073000
# ameblo
wget -O html/ja_ameblo.jp.html http://ameblo.jp/pico-art/entry-12099702897.html
# livedoor blog
wget -O html/ja_drive-kyuusyuu.blog.jp.html http://drive-kyuusyuu.blog.jp/floralvillage.html
# wordpress.com
wget -O html/ja_prepro.wordpress.com.html https://prepro.wordpress.com/2012/01/05/ipython_config-py%E3%81%AE%E8%A8%AD%E5%AE%9A%E3%83%A1%E3%83%A2/

## en

# medium
wget -O html/en_medium.com.html https://medium.com/wandering-cto/my-journey-into-the-berlin-startup-scene-4dc8faecd305
# github.com/blog
wget -O html/en_github.com.html https://github.com/blog/2093-how-the-services-team-uses-github
# blogger
wget -O html/en_googleblog.blogspot.jp.html https://googleblog.blogspot.jp/2015/12/icymi-few-stocking-stuffers-from-around.html
# blogger + splash (192.168.59.103 is a docker host where splash is running)
wget -O html/en_googleblog.blogspot.jp.splash.html 'http://192.168.59.103:8050/render.html?url=https://googleblog.blogspot.jp/2015/12/icymi-few-stocking-stuffers-from-around.html'
