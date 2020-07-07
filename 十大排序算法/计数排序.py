# -*- coding: utf-8 -*-
# @Time    : 2020/3/23 21:26
# @Author  : 唐家鑫
# @Email   : 1280445703@qq.com
# @File    : 计数排序.py
# @Software: PyCharm
l=[3,4,5,9,2,8,15,32,15,24,2,12,14,6,6,20]
'''8、计数排序（Counting Sort）
    计数排序 的核心在于将输入的数据值转化为键存储在额外开辟的数组空间中。 
    作为一种线性时间复杂度的排序，计数排序要求输入的数据必须是有确定范围的整数。

    计数排序(Counting sort) 是一种稳定的排序算法。
    计数排序使用一个额外的数组C，其中第i个元素是待排序数组A中值等于i的元素的个数。
    然后根据数组C来将A中的元素排到正确的位置。它只能对整数进行排序。
O(n+k)
8.1 算法描述
步骤1：找出待排序的数组中最大和最小的元素；
步骤2：统计数组中每个值为i的元素出现的次数，存入数组C的第i项；
步骤3：对所有的计数累加（从C中的第一个元素开始，每一项和前一项相加）；
步骤4：反向填充目标数组：将每个元素i放在新数组的第C(i)项，每放一个元素就将C(i)减去1。'''
'''
比较适合数据比较集中，数据重复比较多的情况
'''

min=l[0]
max=l[0]
# 找出最大值和最小值
for i in range(1,len(l)):
    # print(l[i],min,max)
    if l[i]<min:
        min=l[i]
    if l[i]>max:
        max=l[i]
# 创建有偏移量的列表
lCount=[0]*(max-min+1)

# 将列表元素分别计数
for i in range(len(l)):
    if lCount[l[i]-min]!=0:
        lCount[l[i]-min]=lCount[l[i]-min]+1
    else:
        lCount[l[i]-min] =   1
j=0
for i in range(len(lCount)):
    while lCount[i]!=0:
        l[j] = i + min
        j=j+1
        # 计数减一
        lCount[i]=lCount[i]-1
print(l)

