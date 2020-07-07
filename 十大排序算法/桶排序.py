# -*- coding: utf-8 -*-
# @Time    : 2020/3/23 22:07
# @Author  : 唐家鑫
# @Email   : 1280445703@qq.com
# @File    : 桶排序.py
# @Software: PyCharm

l=[3,4,5,9,2,8,15,32,17,25,15,24,22]
'''桶排序（Bucket Sort）
    桶排序 是计数排序的升级版。
    它利用了函数的映射关系，高效与否的关键就在于这个映射函数的确定。

    桶排序 (Bucket sort)的工作的原理：
假设输入数据服从均匀分布，将数据分到有限数量的桶里，每个桶再分别排序
（有可能再使用别的排序算法或是以递归方式继续使用桶排序进行排
O(n+k)
9.1 算法描述
步骤1：人为设置一个BucketSize，作为每个桶所能放置多少个不同数值
（例如当BucketSize==5时，该桶可以存放｛1,2,3,4,5｝这几种数字，但是容量不限，即可以存放100个3）；
步骤2：遍历输入数据，并且把数据一个一个放到对应的桶里去；
步骤3：对每个不是空的桶进行排序，可以使用其它排序方法，也可以递归使用桶排序；
步骤4：从不是空的桶里把排好序的数据拼接起来。 

注意，如果递归使用桶排序为各个桶排序，则当桶数量为1时要手动减小BucketSize增加下一循环桶的数量，
否则会陷入死循环，导致内存溢出。'''
max=l[0]
# 找出最大值和最小值
for i in range(1,len(l)):
    # print(l[i],min,max)

    if l[i]>max:
        max=l[i]
# 创建有偏移量的列表
# 设置5个桶,并求出每个区间的大小
n=max//5+1
lCount=[[] for i in range(5)]
# for i in range(len(lCount)):
#     lCount[i].append([])
for i in range(len(l)):
    # print(l[i]//n)
    lCount[l[i]//n].append(l[i])
def sort(l):
    for i in range(len(l)):
        for j in range(0, len(l) - 1):
            if l[j] > l[j + 1]:
                temp = l[j]
                l[j] = l[j + 1]
                l[j + 1] = temp
    return l
j=0
for i in range(len(lCount)):
    # 桶内排序并赋值给原列表
    if lCount[i]:
        # print(j,len(lCount[i])+j,sort(lCount[i]))
        lTemp= sort(lCount[i])
        # 返回排序后的部分列表
        m = 0
        # 将列表赋值给原列表部分
        for k in range(j,len(lCount[i])+j):
            # print(k)
            l[k]=lTemp[m]
            m=m+1
        # 不能直接使用下面的语句对猎豹的部分进行赋值，运行证明这样原列表不会改变
        # l[j:len(lCount[i])+j]=sort(lCount[i])
        j=len(lTemp)+j
        # print(len(lCount[i]))

print(l)