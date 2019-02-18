'''
绘制评论数与喜爱人数条形图
'''
import numpy as np
import matplotlib.pyplot as mp
mp.rcParams['font.family']=['STKaiti']
np.set_printoptions(precision=3,suppress=True)
titles,comments,loves= \
    np.loadtxt(
        open("./rank/test.csv",encoding='utf8'),
        delimiter=',',
        usecols=(1,4,5),
        unpack=True,
        dtype='U30, f2, f2'
        )
comments[-1] = comments[-1] * 0.0001
comments[-4] = comments[-4] * 0.0001

mp.figure('b站榜单', facecolor='lightgray',figsize=(10,15))
mp.title('BiliBili Anime Rank', fontsize=25)
mp.xlabel('番剧名', fontsize=18,)
mp.ylabel('评论数与喜爱人数', fontsize=18)
mp.tick_params(labelsize=20)
x = np.arange(len(titles))
mp.xticks(x,titles,rotation=87)
l = [i for i in range(0,240,10)]
mp.yticks(l,l)
mp.bar(x-0.2, comments,0.4,
       color='dodgerblue', label='评论数：单位：万',)
mp.bar(x+0.2, loves, 0.4,
       color='orangered', label='喜爱数：单位：万',)
#获取特殊点(评论最多数)
comments_max_y = max(comments)
index1 =np.where(comments==comments_max_y)
loves_max_y = max(loves)
index2 = np.where(loves==loves_max_y)
#去找该特殊点对应的title
titles_max_x = titles[index1]
titles_max_x2 = titles[index2]
#坐标移动,把特殊点移动到条形图中心上
index3 = np.where(titles==titles_max_x)
# print(index3)
# input('ss')
x1 = x[index3] - 0.2
x2 =x[index3] + 0.2
mp.scatter(x1,comments_max_y,
           facecolor='limegreen', s=80,
           marker='h', zorder=3)
mp.scatter(x2,loves_max_y,
           facecolor='darkblue', s=50,
           marker='X', zorder=3)
#特殊点备注
mp.annotate('评论最多',
            xycoords='data',
            xy=(x1, comments_max_y),
            textcoords='offset points',
            xytext=(-35, 70),
            fontsize=14,
            arrowprops=dict(
                arrowstyle='->',
                connectionstyle='angle3'))
mp.annotate('喜爱最多',
            xycoords='data',
            xy=(x2, loves_max_y),
            textcoords='offset points',
            xytext=(10, 15),
            fontsize=14,
            arrowprops=dict(
                arrowstyle='->',
                connectionstyle='angle3'))
mp.legend(fontsize=20)
mp.show()