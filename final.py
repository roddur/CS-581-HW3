import pandas as pd

al=[]
m1=[]
m2=[]

data=pd.read_csv("FastTree_JC.csv", header=None, sep=' ')

data_all=data.iloc[:,2:].mean(axis=0)
al.append((data_all.iloc[3]/(data_all.iloc[0]-3),data_all.iloc[4]/(data_all.iloc[0]-3), data_all.iloc[5]))

data_m1=data.loc[data.iloc[:,0]=='1000M1'].iloc[:,2:].mean(axis=0)
m1.append((data_m1.iloc[3]/(data_m1.iloc[0]-3),data_m1.iloc[4]/(data_m1.iloc[0]-3), data_m1.iloc[5]))
data_m2=data.loc[data.iloc[:,0]=='1000M4'].iloc[:,2:].mean(axis=0)
m2.append((data_m2.iloc[3]/(data_m2.iloc[0]-3),data_m2.iloc[4]/(data_m2.iloc[0]-3), data_m2.iloc[5]))

data=pd.read_csv("FastTree_GTR.csv", header=None, sep=' ')

data_all=data.iloc[:,2:].mean(axis=0)
al.append((data_all.iloc[3]/(data_all.iloc[0]-3),data_all.iloc[4]/(data_all.iloc[0]-3), data_all.iloc[5]))

data_m1=data.loc[data.iloc[:,0]=='1000M1'].iloc[:,2:].mean(axis=0)
m1.append((data_m1.iloc[3]/(data_m1.iloc[0]-3),data_m1.iloc[4]/(data_m1.iloc[0]-3), data_m1.iloc[5]))
data_m2=data.loc[data.iloc[:,0]=='1000M4'].iloc[:,2:].mean(axis=0)
m2.append((data_m2.iloc[3]/(data_m2.iloc[0]-3),data_m2.iloc[4]/(data_m2.iloc[0]-3), data_m2.iloc[5]))

data=pd.read_csv("NJ_JC.csv", header=None, sep=' ')

data_all=data.iloc[:,2:].mean(axis=0)
al.append((data_all.iloc[3]/(data_all.iloc[0]-3),data_all.iloc[4]/(data_all.iloc[0]-3), data_all.iloc[5]))

data_m1=data.loc[data.iloc[:,0]=='1000M1'].iloc[:,2:].mean(axis=0)
m1.append((data_m1.iloc[3]/(data_m1.iloc[0]-3),data_m1.iloc[4]/(data_m1.iloc[0]-3), data_m1.iloc[5]))
data_m2=data.loc[data.iloc[:,0]=='1000M4'].iloc[:,2:].mean(axis=0)
m2.append((data_m2.iloc[3]/(data_m2.iloc[0]-3),data_m2.iloc[4]/(data_m2.iloc[0]-3), data_m2.iloc[5]))

data=pd.read_csv("NJ_L.csv", header=None, sep=' ')

data_all=data.iloc[:,2:].mean(axis=0)
al.append((data_all.iloc[3]/(data_all.iloc[0]-3),data_all.iloc[4]/(data_all.iloc[0]-3), data_all.iloc[5]))

data_m1=data.loc[data.iloc[:,0]=='1000M1'].iloc[:,2:].mean(axis=0)
m1.append((data_m1.iloc[3]/(data_m1.iloc[0]-3),data_m1.iloc[4]/(data_m1.iloc[0]-3), data_m1.iloc[5]))
data_m2=data.loc[data.iloc[:,0]=='1000M4'].iloc[:,2:].mean(axis=0)
m2.append((data_m2.iloc[3]/(data_m2.iloc[0]-3),data_m2.iloc[4]/(data_m2.iloc[0]-3), data_m2.iloc[5]))


for i in range(4):
    print(al[i])
    print(m1[i])
    print(m2[i])



'''
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')
N = 4


fp = [i[0] for i in al]
fn = [i[1] for i in al]

ind = np.arange(N) 
width = 0.35
plt.bar(ind, fp, width, label='FP')
plt.bar(ind + width, fn, width,
    label='FN')

plt.ylabel('Scores')
plt.title('Average FN/FP rate for both datasets')

plt.xticks(ind + width / 2, ('FastTree(JC69)', 'FastTree(GTR)', 'NJ(JC distance)', 'NJ(Logdet)'))
plt.legend(loc='best')
plt.savefig('al.png')
plt.close()

fp = [i[0] for i in m1]
fn = [i[1] for i in m1]

ind = np.arange(N) 
width = 0.35
plt.bar(ind, fp, width, label='FP')
plt.bar(ind + width, fn, width,
    label='FN')

plt.ylabel('Scores')
plt.title('Average FN/FP rate for 1000M1 dataset')

plt.xticks(ind + width / 2, ('FastTree(JC69)', 'FastTree(GTR)', 'NJ(JC distance)', 'NJ(Logdet)'))
plt.legend(loc='best')
plt.savefig('m1.png')


fp = [i[0] for i in m2]
fn = [i[1] for i in m2]

ind = np.arange(N) 
width = 0.35
plt.bar(ind, fp, width, label='FP')
plt.bar(ind + width, fn, width,
    label='FN')

plt.ylabel('Scores')
plt.title('Average FN/FP rate for 1000M4 dataset')

plt.xticks(ind + width / 2, ('FastTree(JC69)', 'FastTree(GTR)', 'NJ(JC distance)', 'NJ(Logdet)'))
plt.legend(loc='best')
plt.savefig('m2.png')
'''