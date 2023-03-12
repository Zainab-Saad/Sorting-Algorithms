import numpy as np, time, matplotlib.pyplot as plt
def bubble_sort(array):
    for j in range(0, len(array)-1):
        swap = 0
        for i in range(0, len(array)-j-1):
            if array[i] > array[i+1]:
                temp = array[i]
                array[i] = array[i+1]
                array[i+1] = temp
                swap += 1 
        if not swap:
            break
    return array

if __name__ == '__main__':
    x, y = [], []
    for i in range(1, 10000, 400):
        x.append(i)
        unsorted_array = np.random.randint(1, 101, i)
        print('Iteration #', i, "Unsorted Array", unsorted_array)
        start = time.perf_counter()
        sorted_array = bubble_sort(unsorted_array)
        end = time.perf_counter()
        print('Iteration #', i, "Sorted Array", sorted_array)
        y.append((end-start)*10**6)
    plt.style.use('dark_background')
    plt.plot(x, y)
    plt.xlabel('size of array')
    plt.ylabel('time in micro second')
    plt.title('Bubble Sort')
    plt.show()