f=open(r'C:\Users\dell\Desktop\2021年春季\统计建模\数据\firm_2005_0.csv','r',encoding='utf-8')
fw=open(r'C:\Users\dell\Desktop\2021年春季\统计建模\数据\firm_2005-高科技.csv','w',encoding='utf-8')

dic={}
cnt=0
flag=0
for line in f:
    cnt+=1
    ls=line.split('\t')
    if ls[0]=='name':
        continue
    if len(ls)==11:
        if ls[6]!='科学研究和技术服务业' and ls[6]!='信息传输、软件和信息技术服务业':
            continue
        dic[ls[8]]=dic.get(ls[8],0)+1
    elif len(ls)==10:
        if ls[5]!='科学研究和技术服务业' and ls[5]!='信息传输、软件和信息技术服务业':
            continue
        dic[ls[7]]=dic.get(ls[7],0)+1
    '''try:
        dic[ls[8]]=dic.get(ls[8],0)+1
    except:
        print(ls,cnt)'''

print(dic)

fw.write('province,count\n')
for key in dic:
    y=str(key)+','+str(dic[key])+'\n'
    fw.write(y)

f.close()
fw.close()