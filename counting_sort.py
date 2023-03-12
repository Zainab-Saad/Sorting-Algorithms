import numpy as np, time, matplotlib.pyplot as plt
# pass the unsorted array as argument initialize new array inside the function and return it
# determine the max of the parameter unsorted array in function
def counting_sort(array):
    new_array = [0]*(len(array))
    max_element = max(array)
    temp_array = [0]*(max_element+1)
    # loop to record the number of times each element in unsorted array appears into the temp_array
    for j in range(0, len(array)):
        temp_array[array[j]] += 1
    # sum the count of the elements from first index to end in the temporary array
    for j in range(1, max_element+1):
        temp_array[j] += temp_array[j-1]
    # according to the summed count in temporary array put elements from unsorted array to new array
    for j in reversed(range(0, len(array))):
        new_array[temp_array[array[j]]-1] = array[j]
        temp_array[array[j]] -= 1
    return new_array
if __name__ == '__main__':
    x, y = [], []
    for i in range(1, 5):
        x.append(10**i)
        unsorted_array = np.random.randint(1, 101, 10**i)
        print('At iteration # ', i, 'Unsorted: ', unsorted_array)
        start = time.perf_counter()
        sorted_array = counting_sort(unsorted_array)
        end = time.perf_counter()
        print('At iteration # ', i, 'Sorted: ', sorted_array)
        y.append((end-start)*10**6)
    plt.style.use('dark_background')
    plt.plot(x, y)
    plt.xlabel('size of array')
    plt.ylabel('time in micro second')
    plt.title('Counting Sort')
    plt.show()