import matplotlib.pyplot as plt
import numpy as np

# Selection Sort
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        yield arr

# Heap Sort
def heapify(arr, n, root):
    largest = root
    left = 2 * root + 1
    right = 2 * root + 2

    if left < n and arr[root] < arr[left]:
        largest = left
    if right < n and arr[largest] < arr[right]:
        largest = right
    if largest != root:
        arr[root], arr[largest] = arr[largest], arr[root]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        yield arr
        heapify(arr, i, 0)

# Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                yield arr

# Quick Sort
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        yield arr
        yield from quick_sort(arr, low, pi - 1)
        yield from quick_sort(arr, pi + 1, high)

# Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        yield arr

# Plotting function
def visualize_sorting(sorting_function, arr, title):
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.set_title(title)
    bars = ax.bar(range(len(arr)), arr, align="edge")
    ax.set_xlim(0, len(arr))
    ax.set_ylim(0, int(1.1 * max(arr)))
    for step in sorting_function(arr):
        for bar, val in zip(bars, step):
            bar.set_height(val)
        plt.pause(0.001)

    
    
    plt.show()

# Initial array to be sorted
arr = np.random.randint(1, 100, 70)

# Visualize each sorting algorithm
visualize_sorting(selection_sort, arr.copy(), "Selection Sort")
visualize_sorting(heap_sort, arr.copy(), "Heap Sort")
visualize_sorting(bubble_sort, arr.copy(), "Bubble Sort")
visualize_sorting(lambda a: quick_sort(a, 0, len(a) - 1), arr.copy(), "Quick Sort")
visualize_sorting(insertion_sort, arr.copy(), "Insertion Sort")