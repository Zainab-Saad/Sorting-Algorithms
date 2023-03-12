import math, numpy as np, time, matplotlib.pyplot as plt

# function to merge the subarrays
def merge(array, left, mid, right):
    # get the length for the two subarrays
    len1 = mid-left+1
    len2 = right-mid
    # declare and initialize the two arrays to None
    first_subarray = [None]*(len1+1)
    second_subarray = [None]*(len2+1)
    # give values to the two subarrays from the original array
    for i in range(1, len1+1):
        first_subarray[i-1] = array[left+i-1]
    for i in range(1, len2+1):
        second_subarray[i-1] = array[mid+i]
    # initialize the last index as infinity 
    first_subarray[len1] = math.inf
    second_subarray[len2] = math.inf
    
    # initialize two variables to point to index of first and second subarray
    i, j = 0, 0
    for k in range(left, right+1):
        if first_subarray[i] <= second_subarray[j]:
            array[k] = first_subarray[i]
            i += 1
        else:
            array[k] = second_subarray[j]
            j += 1
    return array

def merge_sort(array, left, right):
    if left < right:
        mid = math.floor((left+right)/2)
        merge_sort(array, left, mid)
        merge_sort(array, mid+1, right)
        merge(array, left, mid, right)
if __name__ == '__main__':
    x, y = [], []
    for i in range(1, 10000, 400):
        x.append(i)
        unsorted_array = np.random.randint(1, 101, i)
        print('Iteration #', i, "Unsorted Array", unsorted_array)
        start = time.perf_counter()
        merge_sort(unsorted_array, 0, len(unsorted_array)-1)
        end = time.perf_counter()
        print('Iteration #', i, "Sorted Array", unsorted_array)
        y.append((end-start)*10**6)
    plt.style.use('dark_background')
    plt.plot(x, y)
    plt.xlabel('size of array')
    plt.ylabel('time in micro second')
    plt.title('Merge Sort')
    plt.show()