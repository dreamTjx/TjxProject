# -*- coding: utf-8 -*-
# @Time    : 2020/3/22 22:50
# @Author  : 唐家鑫
# @Email   : 1280445703@qq.com
# @File    : 归并排序.py
# @Software: PyCharm

l=[3,4,5,9,2,8,15,32,15,24,57]
'''5、归并排序（Merge Sort）
归并排序是建立在归并操作上的一种有效的排序算法。
该算法是采用分治法（Divide and Conquer）的一个非常典型的应用。
将已有序的子序列合并，得到完全有序的序列；
即先使每个子序列有序，再使子序列段间有序。
若将两个有序表合并成一个有序表，称为2-路归并。 
O(nlogn)
5.1 算法描述
把长度为n的输入序列分成两个长度为n/2的子序列；
对这两个子序列分别采用归并排序；
将两个排序好的子序列合并成一个最终的排序序列。'''
l1=[]
l2=[]
i=2
def merge(left,right):
    '''
    合并并排序列表
    :param left: 左边的列表
    :param right: 右边的列表
    :return: 把两个合并并排序过后的列表
    '''
    result = []
    print(left,right)
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    while left:
        result.append(left.pop(0))
    while right:
        result.append(right.pop(0))
    print(result)
    return result
def cut(l):

    n=len(l)//2
    if len(l)>1:
        # 如果列表元素不是一个，就继续把元组划分
        # print(l[:n],l[n+1:])
        return merge(cut(l[:n]),cut(l[n:]))
    else:
        # 列表元素只有一个时候，，返回其本身
        # print(l)
        return l
print(cut(l))
