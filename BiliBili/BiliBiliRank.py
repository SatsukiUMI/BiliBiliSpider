# -*- coding: utf-8 -*-
import csv
import requests
from lxml import etree
import re
import copy
url = 'https://www.bilibili.com/ranking/bangumi/13/0/3'
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}
#配置参数发请求
res = requests.get(url,headers = headers)
#if res.status_code == 200:
#    print('响应成功')
#else:
#    print('响应失败')
res.encoding = 'utf-8'
#获取到响应页面
html = res.text
#xpath解析
oriPage = etree.HTML(html)
levelList = oriPage.xpath('//ul[@class="rank-list bangumi"]/li//text()')
#print(levelList)


#保存到csv，完整版
#l是大列表，含全部的数据，去除原来数据中无用的\n和空格
l = []
for data in levelList:
    data = data.strip().replace("\n","")
    l.append(data)
#按列表划分出50个榜单的番剧数据的小列表l2。
#每8个数据划分为一组，共50组
n = 8
l2 = [l[i:i + n] for i in range(0, len(l), n)]
#经过简单数据筛选的列表l3
l3 = []
for i in l2:
    drop = re.findall(r'.*?([0-9]).*?',i[2])
    if len(drop) == 1:
        l3.append(i)
# print(l3)




#l2是二维列表，csv文件可以直接写入
#调整文件保存位置,去除写入时的空格。
with open('.\\rank\\b站榜单999.csv','w',newline='',encoding='utf8') as csvfile:
    writer = csv.writer(csvfile)
    print("请选择要保留的数据")
    print("1.全部数据")
    print("2.当季数据")
    print("3.数据分析用")
    save = int(input("请输入"))
#    写入csv表头
    #尝试写csv中文表头，通过
#    writer.writerow(['排名', '名称', '已播出集数', '播放量','评论数','喜欢人数','综合得分','无用数据'])
    if save == 2:
        writer.writerow(['rank', 'title', 'episode', 'play', 'comment', 'love', 'score', 'else'])
        writer.writerows(l3)
        print("季度榜单保存完毕")
    elif save ==1:
        writer.writerow(['rank', 'title', 'episode', 'play', 'comment', 'love', 'score', 'else'])
        writer.writerows(l2)
        print('总榜单保存完毕')
    else:
        writer.writerows(l3)
        print("保存完毕")



# 保存到txt
# file = open('排行榜.txt','a')
# for k in range(len(levelList)):
#    data = str(levelList[k].replace("'",'').replace(',','')+'\n')
#    file.write(data)
# file.close()
# print('保存完毕')





        
        
        








