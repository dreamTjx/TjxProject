# -*- coding: utf-8 -*-
# @Time    : 2020/3/23 22:34
# @Author  : 唐家鑫
# @Email   : 1280445703@qq.com
# @File    : 基数排序.py
# @Software: PyCharm

l=[3,4,5,9,2,8,15,32,15,24,89,45,65,25,48,17,39,57]
'''10、基数排序（Radix Sort）
    基数排序也是非比较的排序算法，对每一位进行排序，从最低位开始排序，复杂度为O(kn),
    为数组长度，k为数组中的数的最大的位数；

    基数排序是按照低位先排序，然后收集；
    再按照高位排序，然后再收集；
    依次类推，直到最高位。
    有时候有些属性是有优先级顺序的，先按低优先级排序，再按高优先级排序。
    最后的次序就是高优先级高的在前，高优先级相同的低优先级高的在前。
    基数排序基于分别排序，分别收集，所以是稳定的。
O(kn)
10.1 算法描述
步骤1：取得数组中的最大数，并取得位数；
步骤2：arr为原始数组，从最低位开始取每个位组成radix数组；
步骤3：对radix进行计数排序（利用计数排序适用于小范围数的特点）；'''
'''
1. 基数排序 vs 计数排序 vs 桶排序
基数排序有两种方法：

这三种排序算法都利用了桶的概念，但对桶的使用方法上有明显差异：

基数排序：根据键值的每位数字来分配桶；
计数排序：每个桶只存储单一键值；
桶排序：每个桶存储一定范围的数值
'''
max=l[0]
# 找出最大值和最小值
for i in range(1,len(l)):
    # print(l[i],min,max)

    if l[i]>max:
        max=l[i]
# 获取最大值的位数
n=len(list(str(max)))
# 创建0-9的序列数组
barrel=[[]]*10
def sort(l):
    for i in range(len(l)):
        for j in range(0, len(l) - 1):
            if l[j] > l[j + 1]:
                temp = l[j]
                l[j] = l[j + 1]
                l[j + 1] = temp
    return l
i=0
while i!=n:
    barrel = [[] for i in range(10)]
    for j in range(len(l)):
        # 按相同位置数字放在相应的桶内
        # print(l[j],l[j]%(10**(i+1))//(10**i))
        # l[j]%(10**(i+1))//(10**i)取各位数的方法，
        # 先用除去取余比当前位更高的再整除当前位
        # 如35除10余5,5再除以当前位1得个位为5
        barrel[l[j]%(10**(i+1))//(10**i)].append(l[j])
        # print(barrel[l[j]%(10**(i+1))//(10**i)])
    j = 0
    for h in range(len(barrel)):
        # 桶内排序并赋值给原列表
        if barrel[h]:
            # print(j,len(lCount[i])+j,sort(lCount[i]))
            lTemp = sort(barrel[h])
            # 返回排序后的部分列表
            m = 0
            # 将列表赋值给原列表部分
            for k in range(j, len(barrel[h]) + j):
                # print(k)
                l[k] = lTemp[m]
                m = m + 1

            j = len(lTemp) + j
    # print(l)
    i=i+1
    # print(i,n)
print(l)
