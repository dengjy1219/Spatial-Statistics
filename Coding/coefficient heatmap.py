import random
from matplotlib import pyplot as plt
from matplotlib import cm
from matplotlib import axes
from matplotlib.font_manager import FontProperties
plt.rcParams['font.sans-serif']=['SimHei']

def draw():
 xLabel=['安徽','北京','福建','甘肃','广东','广西','贵州','海南','河北','河南','黑龙江','湖北','湖南','吉林','江苏','江西','辽宁','内蒙古','宁夏','青海','山东','山西','陕西','上海','四川','天津','西藏','新疆','云南','浙江','重庆']
 yLabel = ['2005','2010','2015']

 f=open(r'C:\Users\dell\Desktop\2021年春季\统计建模\实证结果\datatts.csv','r',encoding='utf-8-sig')
 data = []
 for line in f:
  temp = line.replace('\n','').split(',')
  for j in range(31):
    temp[j]=eval(temp[j])
  data.append(temp)
 f.close()

 fig = plt.figure(dpi=300,figsize=(12,4))
 ax = fig.add_subplot(111)
 ax.set_yticks(range(len(yLabel)))
 ax.set_yticklabels(yLabel)
 ax.set_xticks(range(len(xLabel)))
 ax.set_xticklabels(xLabel,rotation=270)
 im = ax.imshow(data, cmap='RdBu_r',aspect='auto')
 plt.colorbar(im,orientation='vertical')
 plt.show()
 
d = draw()
