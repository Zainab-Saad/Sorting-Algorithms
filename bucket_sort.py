import time, numpy as np, matplotlib.pyplot as plt, math
from insertion_sort import insertion_sort
def bucket_sort(array):
    # initialize a list of empty lists that will contain the buckets 
    # using list comprehension for creating a 2d list of empty lists
    buckets = [[] for _ in range(len(array))]
    for i in range(0, len(array)):
        # append the elements in array in the right bucket 
        buckets[(math.floor(len(array) * array[i]))-1].append(array[i])
    # now the buckets are made
    # sort the elements in individual buckets using insertion sort
    for i in range(0, len(array)):
        buckets[i] = insertion_sort(buckets[i])
    # concatenate all the buckets into one bucket
    # this will be our final sorted array
    sorted_array = []
    for i in range(0, len(array)):
        for j in range(0, len(buckets[i])):
            sorted_array.append(buckets[i][j])
    return sorted_array

if __name__ == '__main__':
    x, y = [], []
    for i in range(1, 10000, 400):
        x.append(i)
        unsorted_array = np.random.random_sample(i).round(2)
        print('Iteration #', i, "Unsorted Array", unsorted_array)
        start = time.perf_counter()
        sorted_array = bucket_sort(unsorted_array)
        end = time.perf_counter()
        print('Iteration #', i, "Sorted Array", sorted_array)
        y.append((end-start)*10**6)
    plt.style.use('dark_background')    
    plt.plot(x, y)
    plt.xlabel('size of array')
    plt.ylabel('time in micro second')
    plt.title('Bucket Sort')
    plt.show()