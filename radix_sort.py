import numpy as np, time, math, matplotlib.pyplot as plt
def radix_sort(array):
    maximum = max(array)
    divisor = 1
    # run the loop the number of digits in the maximum number times
    while maximum / divisor >= 1:
        # use counting sort to sort the single digites in each pass initialize array of 10 size that will hold 0
        temp_array, output = [0] * 10, [0] * len(array)
        # loop through the array and fill the temp_array with the count of the digits to be sorted in this pass
        for i in range(0, len(array)):
            # get the digit to be sorted
            digit = math.floor(array[i] / divisor) % 10
            temp_array[digit] += 1
        # take the cummulative sum of all the elements in the temp_array
        for i in range(1, 10):
            temp_array[i] += temp_array[i-1]
        
        # copy the elements in sorted order from original unsorted array to the output array from the temp_array
        for i in reversed(range(0, len(array))):
            # get the digit to be sorted
            digit = math.floor(array[i] / divisor) % 10
            output[temp_array[digit]-1] = array[i]
            temp_array[digit] -= 1
        # copy the elements from output array to original array
        for i in range(0, len(array)):
            array[i] = output[i]
        # set the value of looping variable
        divisor *= 10
    return array
if __name__ == '__main__':
    x, y = [], []
    for i in range(1, 5):
        x.append(10**i)
        unsorted_array = np.random.randint(1, 101, 10**i)
        print('At iteration # ', i, 'Unsorted: ', unsorted_array)
        start = time.perf_counter()
        sorted_array = radix_sort(unsorted_array)
        end = time.perf_counter()
        print('At iteration # ', i, 'Sorted: ', sorted_array)
        y.append((end-start)*10**6)
    plt.style.use('dark_background')
    plt.plot(x, y)
    plt.xlabel('size of array')
    plt.ylabel('time in micro second')
    plt.title('Radix Sort')
    plt.show()
    