# -*- coding: utf-8 -*-
# @Time    : 2020/3/23 18:16
# @Author  : 唐家鑫
# @Email   : 1280445703@qq.com
# @File    : 快速排序.py
# @Software: PyCharm

l=[3,4,5,9,2,8,6,15,32,15,24,57]
''' 快速排序 的基本思想：通过一趟排序将待排记录分隔成独立的两部分，
其中一部分记录的关键字均比另一部分的关键字小，则可分别对这两部分记录继续进行排序，
以达到整个序列有序。
O(nlogn)
6.1 算法描述
对绝大多数顺序性较弱的随机数列而言，快速排序总是优于归并排序。
快速排序使用分治法来把一个串（list）分为两个子串（sub-lists）。
具体算法描述如下：
步骤1：从数列中挑出一个元素，称为 “基准”（pivot ）；
步骤2：重新排序数列，所有元素比基准值小的摆放在基准前面，所有元素比基准值大的摆在基准的后面（相同的数可以到任一边）。在这个分区退出之后，该基准就处于数列的中间位置。这个称为分区（partition）操作；
步骤3：递归地（recursive）把小于基准值元素的子数列和大于基准值元素的子数列排序。'''
i=0
def sort(l):
    for i in range(len(l)):
        for j in range(0, len(l) - 1):
            if l[j] > l[j + 1]:
                temp = l[j]
                l[j] = l[j + 1]
                l[j + 1] = temp
    return l
while i<len(l):
    n=i
    print(l[i])
    for j in range(i+1,len(l)):
        # 找出比基准小的数并把他移动到前面
        if l[j]<l[n]:
            temp=l[j]
            k=j
            while k!=i:
                l[k]=l[k-1]
                k=k-1
            l[i]=temp
            n=n+1
    if i!=n:
        l[i:n+1]=sort(l[i:n+1])
    # print(l[i:n+1])
    i=n+1

print(l)
