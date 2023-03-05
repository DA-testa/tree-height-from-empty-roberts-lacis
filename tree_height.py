# python3

import sys
import threading
import numpy as np


def compute_height(elements, parents):
    apmeklets = np.zeros([elements], dtype=np.int32)
    max_height_arr = np.zeros([elements], dtype=np.int32)

    for i in range(elements):
        if apmeklets[i]==0:
            node = i
            reizes = 0
            while node != -1:
               apmeklets[node] = 1 
               reizes = reizes + 1
               max_height_arr[i] = reizes
               node = parents[node]
    
    return max(max_height_arr)


def main():
    tekstaievade = input()
    if tekstaievade.__contains__("I"):
        elements = int(input())
        parents = np.array(list((map(int, input().strip().split()))))[:elements]
        height = compute_height(elements, parents)
        print(height)
        
    elif tekstaievade.__contains__("F"):
        nos = input()
        if "a" not in nos:
            fails = "test/" + nos
            with open(fails,"r") as f:
                elements = int(f.readline())
                parents = np.array(list((map(int, f.readline().strip().split()))))[:elements]
                height = compute_height(elements, parents)
                print(height)
   
sys.setrecursionlimit(10**7) 
threading.stack_size(2**27)   
threading.Thread(target=main).start()
# main()
# print(numpy.array([1,2,3]))