# python3

import sys
import threading
import numpy


def compute_height(n, parents):
    max_height = 0
    levels = []
    i=-1
    while(i<eval(n)):
        level = []
        for elem in parents:
            if eval(elem) == i:
                level.add(elem)
        if len(level) > 0:
            levels.add(level)
        i=i+1
    return len(levels)


def main():
    type = input()
    if type == "I":
        n = input()
        parentstr = input()
    else:
        filename = input()
        file = "test/"+filename
        if "a" in file:
            return
        with open(file, "r") as filereader:
            lines = filereader.readlines()
            n = lines[0]
            parentstr = lines[1]
    parents = parentstr.split()
    print(compute_height(parents))

    # implement input form keyboard and from files
    
    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    
    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result
    pass

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
main()
# print(numpy.array([1,2,3]))