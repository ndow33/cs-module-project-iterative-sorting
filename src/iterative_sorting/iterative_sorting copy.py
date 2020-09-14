# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):


    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # find the length of the array
    n = len(arr)
    # for each element in the length of array...
    for i in range(n-1):
        # traverse through the list
        for j in range(n-i-1):
            # and compare the current value to the next value
            if arr[j] > arr[j+1]:
                # if the next value is greater than the current value
                # switch the two values
                arr[j], arr[j+1] = arr[j+1], arr[j]
        
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
