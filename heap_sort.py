import math, time, numpy as np, matplotlib.pyplot as plt

def max_heapify(array, index, length):
    left = (2 * index) + 1
    right = (2 * index) + 2
    if left <= length and array[left] > array[index]:
        largest = left
    else:
        largest = index
    if right <= length and array[right] > array[largest]:
        largest = right
    if largest != index:
        array[index], array[largest] = array[largest], array[index]
        max_heapify(array, largest, length)
    
def build_max_heap(array):
    for i in reversed(range(0, math.floor(len(array)/2))):

        max_heapify(array, i, len(array)-1)
    return array
        
def heap_sort(array):
    array = build_max_heap(array)
    for i in reversed(range(1, len(array))):
        # exchange array[0] and array[i]
        array[i], array[0] = array[0], array[i]
        max_heapify(array, 0, i-1)
    return array

if __name__ == '__main__':
    x, y = [], []
    for i in range(1, 10000, 400):
        x.append(i)
        unsorted_array = np.random.randint(1, 101, i)
        print('Iteration #', i, "Unsorted Array", unsorted_array)
        start = time.perf_counter()
        sorted_array = heap_sort(unsorted_array)
        end = time.perf_counter()
        print('Iteration #', i, "Sorted Array", sorted_array)
        y.append((end-start)*10**6)
    plt.style.use('dark_background')
    plt.plot(x, y)
    plt.xlabel('size of array')
    plt.ylabel('time in micro second')
    plt.title('Heap Sort')
    plt.show()