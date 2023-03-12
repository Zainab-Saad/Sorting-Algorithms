import numpy as np, time, matplotlib.pyplot as plt
def selection_sort(array): 
    # outer loop runs n-2 times if n is length of array
    for j in range(0, len(array)-1):
        smallest = j
        # inner loop runs n-1-(j+1) times if n is length of array
        for i in range(j+1, len(array)):
            if array[i] < array[smallest]:
                smallest = i
        # exchange array[j] and array[smallest]
        # do the swapping only if smallest is changed
        if smallest != j:
            temp = array[j]
            array[j] = array[smallest]
            array[smallest] = temp    
    return array

if __name__ == '__main__':
    x, y = [], []
    for i in range(1, 10000, 400):
        x.append(i)
        unsorted_array = np.random.randint(1, 101, i)
        print('Iteration #', i, "Unsorted Array", unsorted_array)
        start = time.perf_counter()
        sorted_array = selection_sort(unsorted_array)
        end = time.perf_counter()
        print('Iteration #', i, "Sorted Array", sorted_array)
        y.append((end-start)*10**6)
    plt.style.use('dark_background')
    plt.plot(x, y)
    plt.xlabel('size of array')
    plt.ylabel('time in micro second')
    plt.title('Selection Sort')
    plt.show()