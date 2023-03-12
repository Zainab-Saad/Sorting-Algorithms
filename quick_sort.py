import numpy as np, time, matplotlib.pyplot as plt
# partition puts pivot at the correct position and returns the index of the pivot
# once pivot is decided, array is split over this pivot
def partition(array, left, right):
    # pick right-most element as pivot
    pivot = array[right]
    i = left - 1
    for j in range(left, right):
        if array[j] <= pivot:
            i += 1
            if i != j:
                temp = array[i]
                array[i] = array[j]
                array[j] = temp
    if i+1 != right:
        temp = array[i+1]
        array[i+1] = array[right]
        array[right] = temp
    return i+1

def quick_sort(array, left, right):
    if left < right:
        pivot = partition(array, left, right)
        quick_sort(array, left, pivot-1)
        quick_sort(array, pivot+1, right)
        
if __name__ == '__main__':
    x, y = [], []
    for i in range(1, 10000, 400):
        x.append(i)
        unsorted_array = np.random.randint(1, 101, i)
        print('Iteration #', i, "Unsorted Array", unsorted_array)
        start = time.perf_counter()
        quick_sort(unsorted_array, 0, len(unsorted_array)-1)
        end = time.perf_counter()
        print('Iteration #', i, "Sorted Array", unsorted_array)
        y.append((end-start)*10**6)
    plt.style.use('dark_background')    
    plt.plot(x, y)
    plt.xlabel('size of input array')
    plt.ylabel('time (microsecond)')
    plt.title('Quick Sort')
    plt.show()