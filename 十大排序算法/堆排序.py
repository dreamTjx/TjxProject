# -*- coding: utf-8 -*-
# @Time    : 2020/3/23 19:38
# @Author  : 唐家鑫
# @Email   : 1280445703@qq.com
# @File    : 堆排序.py
# @Software: PyCharm

l=[3,4,5,9,2,8,15,32,15,24,57]
'''堆排序（Heapsort） 是指利用堆这种数据结构所设计的一种排序算法。
堆积是一个近似完全二叉树的结构，并同时满足堆积的性质：
即子结点的键值或索引总是小于（或者大于）它的父节点。
O(nlogn)
7.1 算法描述
步骤1：将初始待排序关键字序列(R1,R2….Rn)构建成大顶堆，此堆为初始的无序区；
步骤2：将堆顶元素R[1]与最后一个元素R[n]交换，
此时得到新的无序区(R1,R2,……Rn-1)和新的有序区(Rn),且满足R[1,2…n-1]<=R[n]；
步骤3：由于交换后新的堆顶R[1]可能违反堆的性质，
因此需要对当前无序区(R1,R2,……Rn-1)调整为新堆，然后再次将R[1]与无序区最后一个元素交换，
得到新的无序区(R1,R2….Rn-2)和新的有序区(Rn-1,Rn)。
不断重复此过程直到有序区的元素个数为n-1，则整个排序过程完成。'''
'''
挺麻烦的，我觉得不是太实用
'''
def buildMaxHeap(arr):
    '''
    创建大顶推
    :param arr:
    :return:
    '''
    import math
    for i in range(math.floor(len(arr)/2),-1,-1):
        heapify(arr,i)

def heapify(arr, i):
    left = 2*i+1
    right = 2*i+2
    largest = i
    if left < arrLen and arr[left] > arr[largest]:
        largest = left
    if right < arrLen and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        swap(arr, i, largest)
        heapify(arr, largest)

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def heapSort(arr):
    '''
    堆排序
    :param arr:
    :return:
    '''
    global arrLen
    arrLen = len(arr)
    buildMaxHeap(arr)
    for i in range(len(arr)-1,0,-1):
        swap(arr,0,i)
        arrLen -=1
        heapify(arr, 0)
    return arr
print(heapSort(l))