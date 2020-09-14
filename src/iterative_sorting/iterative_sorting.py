# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(len(arr)):
        cur_index = i
        smallest_index = cur_index

        # loop through the remaining indices
        # that come after the current index
        for j in range(cur_index+1, len(arr)):
            # compare the object at index j
            # to the current smallest object
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        # get the value at the current index
        cur_obj = arr[cur_index]
        # get the smallest value
        smallest = arr[smallest_index]
        # set the current index to the smallest value
        arr[cur_index] = smallest
        # set the index with the smallest value 
        # to the current index's value
        arr[smallest_index] = cur_obj

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # loop through the array
    for value in range(len(arr)):
        # create an index value that starts at the beginning 
        # every iteration
        index = 0
        # create a second index value
        # that starts at the second value every iteration
        index1 = 1
        # loop through again        
        for value in range(len(arr)-1):
            # if the current value is greater than the next value
            if arr[index] > arr[index1]:
                # switch the values
                small = arr[index1]
                big = arr[index]
                arr[index] = small
                arr[index1] = big
            index +=1
            index1 +=1

    return arr

'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    # Your code here


    return arr
