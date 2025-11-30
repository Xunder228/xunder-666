# Функція бульбашкового сортування
def bubble_sort(arr):
    arr = arr.copy()   # щоб не змінювати вхідний список
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


# Функція сортування вибором
def selection_sort(arr):
    arr = arr.copy()
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


# Функція сортування вставкою
def insertion_sort(arr):
    arr = arr.copy()
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


# Тестування (необов’язково, але корисно залишити)
if __name__ == "__main__":
    data = [9, 5, 1, 4, 3]

    print("Bubble sort:", bubble_sort(data))
    print("Selection sort:", selection_sort(data))
    print("Insertion sort:", insertion_sort(data))
