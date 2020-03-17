# -*- coding: utf-8 -*-
"""博客构建配置文件
"""

# For Maverick
site_prefix = "/bthl/"
source_dir = "../src/"
build_dir = "../dist/"
index_page_size = 10
archives_page_size = 20
template = {
    "name": "Prism",
    "type": "git",
    "url": "https://github.com/Reedo0910/Maverick-Theme-Prism.git",
    "branch": "deploy"
}
enable_jsdelivr = {
    "enabled": True,
    "repo": "Leouas/bthl@gh-pages"
}

# 站点设置
site_name = "Gyanle Yao"
site_logo = "${static_prefix}logo.png"
site_build_date = "2019-12-18T16:51+08:00"
author = "Leouas"
email = "Leoua7@163.com"
author_homepage = "https://Leouas.top"
description = "nothing"
key_words = ['Leouas','Leoua7', 'blog']
language = 'en'
external_links = [
    {
        "name": "Maverick",
        "url": "https://github.com/AlanDecode/Maverick",
        "brief": "Go My Own Way"
    },
    {
        "name": "Leouas",
        "url": "https://Leouas.top",
        "brief": "冰糖葫芦Sayk's Blog"
    }
]
nav = [
    {
        "name": "首页",
        "url": "${site_prefix}",
        "target": "_self"
    },
    {
        "name": "归档",
        "url": "${site_prefix}archives/",
        "target": "_self"
    },
    {
        "name": "关于",
        "url": "${site_prefix}about/",
        "target": "_self"
    }
]

social_links = [
    {
        "name": "Twitter",
        "url": "https://twitter.com/Leoua7",
        "icon": "gi gi-twitter"
    },
    {
        "name": "GitHub",
        "url": "https://github.com/Leouas",
        "icon": "gi gi-github"
    },
    {
        "name": "Weibo",
        "url": "https://weibo.com/",
        "icon": "gi gi-weibo"
    }
]

head_addon = r'''
<meta http-equiv="x-dns-prefetch-control" content="on">
<link rel="dns-prefetch" href="//cdn.jsdelivr.net" />
'''

footer_addon = ''

body_addon = ''
