# python3

import sys
import threading
import numpy


def compute_height(n, parents):
    searched = numpy.zeros(n)
    max = 0

    for i in range(n):
        if searched[i] == 0:
            a = i
            count = 0
            while a != -1:
                count += 1
                searched[a] = 1
                a = parents[a]
            if max < count:
                max = count
    return max


def main():
    try:
        type = input()
        if type.__contains__("I"):
            n = int(input())
            parents = numpy.array(list((map(int, input().strip().split()))))
            print(compute_height(n,parents))
        else:
            file = "test/" + input()
            if "a" in file:
                return
            with open(file,"r") as fr:
                n = int(fr.readline())
                parents = numpy.array(list((map(int, fr.readline().strip().split()))))
                print(compute_height(n,parents))
    except EOFError as e:
        pass
    # implement input form keyboard and from files
    
    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    
    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
main()
# print(numpy.array([1,2,3]))
