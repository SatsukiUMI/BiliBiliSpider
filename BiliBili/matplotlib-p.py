'''
绘制播放量条形图和折线图
'''
import numpy as np
import matplotlib.pyplot as mp
#查看系统字体
#import matplotlib
# a=sorted([f.name for f in matplotlib.font_manager.fontManager.ttflist])
# for i in a:
#     print(i)
#引入系统自带的仿宋字体
mp.rcParams['font.family']=['STFangsong']
titles,plays= \
    np.loadtxt(
        open("./rank/test.csv",encoding='utf8'),
        delimiter=',',
        usecols=(1,3),
        unpack=True,
        dtype='U30, f8'
        )
mp.figure('b站榜单', facecolor='lightgray',figsize=(10,15))
mp.title('BiliBili Anime Rank', fontsize=25)
mp.xlabel('番剧名', fontsize=18,)
mp.ylabel('播放量', fontsize=18)
mp.tick_params(labelsize=20)
x = np.arange(len(titles))
mp.xticks(x,titles,rotation=87)
l = [i for i in range(0,2600,100)]
mp.yticks(l,l)
mp.ylim(20,2600)
#绘制播放量条形图
mp.bar(x+0.2, plays,0.5,
       color='dodgerblue', label='播放量条形：\n单位：万',)
#绘制折线图
mp.plot(x,plays,color="orangered",linewidth=5,linestyle="-",label="播放量折线",alpha=0.8)
mp.legend(fontsize=20)
mp.show()