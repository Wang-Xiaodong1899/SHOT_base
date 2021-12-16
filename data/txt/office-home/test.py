import torch
# pred = open('labeled_source_images_Clipart_Product_1_25_pseudo.txt','r').readlines()
# gt = open('labeled_source_images_Product.txt','r').readlines()
# length = len(pred)
# cnt=0.
# for i in range(length):
#     if pred[i]==gt[i]:
#         cnt=cnt +1
# print('Acc:',cnt/length)


# a = torch.tensor([10.,20.])
# print('{%d,%d}'%(a[0],a[1]))
# print(a[0],a[1])
# temp = open('../../../predcit_tmp.txt').readlines()
# cnt=0.
# for i in temp:
#     a,b = i.strip().split(',')
#     if a==b:
#         cnt+=1
# print(cnt/len(temp))
# pred = open('labeled_source_images_Art_Clipart_2_25_tmp_pseudo.txt','r').readlines()
# length = len(pred)
# cnt=0.
# cluster={}
# for cla in range(65):
#     cluster[cla]=[]

# for line in pred:
#     path,p,gt = line.split(' ')
#     p,gt = int(p),int(gt)
#     cluster[p].append(gt)
# for cla in range(65):
#     cluster[cla]=set(cluster[cla])
# # print(cluster)
# y=[]
# for cla in range(65):
#     print(cla,len(cluster[cla]),end='\t')
#     y.append(len(cluster[cla]))

# print('Acc:',cnt/length)

# import matplotlib.pyplot as plt
# import numpy as np
# plt.bar(range(65),y)
# print(y)
# plt.xlabel('class')
# plt.ylabel('nums')
# plt.title('Shuffle')
# # plt.savefig('2.png',dpi=100)
# # plt.show()
# x=torch.tensor([0.,0.,0.,0.])
# print(x.norm(p=2,dim=0))
import random
random.seed(71)
f = open('labeled_source_images_Real.txt', 'r').readlines()
cluster={}
for i in range(65):
    cluster[i] = []
for li in f:
    cl = li.strip().split(' ')[-1]
    cluster[int(cl)].append(li)

f = open('NoOrder_labeled_source_images_Real.txt', 'w')
clss = random.sample(range(65),65)
print(clss)
for cl in clss:
    for li in cluster[cl]:
        f.write(li)
f.close()
