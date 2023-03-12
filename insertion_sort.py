import numpy as np, time, matplotlib.pyplot as plt

def insertion_sort(array):
    # outer loop runs n-1 times if n is length of array start outer loop from 1 instead of 0 
    # because consider first element of array as sorted part of array
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        # compare ith element with all elements till the start of array or until the first smaller element is encountered
        while(j >= 0 and array[j] > key):
            array[j+1] = array[j]
            j -= 1
        array[j+1] = key
    return array
if __name__ == '__main__':
    x, y = [], []
    for i in range(1, 10000, 400):
        x.append(i)
        unsorted_array = np.random.randint(1, 101, i)
        print('Iteration #', i, "Unsorted Array", unsorted_array)
        start = time.perf_counter()
        sorted_array = insertion_sort(unsorted_array)
        end = time.perf_counter()
        print('Iteration #', i, "Sorted Array", sorted_array)
        y.append((end-start)*10**6)
    plt.style.use('dark_background')
    plt.plot(x, y)
    plt.xlabel('size of array')
    plt.ylabel('time in micro second')
    plt.title('Insertion Sort')
    plt.show()