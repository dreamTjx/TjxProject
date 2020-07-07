# -*- coding: utf-8 -*-
# @Time    : 2020/3/22 20:54
# @Author  : 唐家鑫
# @Email   : 1280445703@qq.com
# @File    : 希尔排序.py
# @Software: PyCharm

l=[3,4,5,9,2,8,15,32,15,24,57]
'''4、希尔排序（Shell Sort）
1959年Shell发明，第一个突破O(n2)的排序算法，是简单插入排序的改进版。
它与插入排序的不同之处在于，它会优先比较距离较远的元素。希尔排序又叫缩小增量排序。
O(nlogn)
4.1 算法描述
先将整个待排序的记录序列分割成为若干子序列分别进行直接插入排序，具体算法描述：

选择一个增量序列t1，t2，…，tk，其中ti>tj，tk=1；
按增量序列个数k，对序列进行k 趟排序；
每趟排序，根据对应的增量ti，将待排序列分割成若干长度为m 的子序列，
分别对各子表进行直接插入排序。
仅增量因子为1 时，整个序列作为一个表来处理，表长度即为整个序列的长度。'''
sp=2
# 设置每组两个数据

arr=[3,4,5,9,2,8,15,32,15,24,57]
gap=1
while(gap < len(arr)/3):
    gap = gap*3+1
    # print(gap)
while gap > 0:
    for i in range(gap,len(arr)):
        # print(i)
        temp = arr[i]
        j = i-gap
        # print(i,j)
        while j >=0 and arr[j] > temp:
            arr[j+gap]=arr[j]
            j-=gap
        arr[j+gap] = temp
    gap = gap//3
print(arr)
