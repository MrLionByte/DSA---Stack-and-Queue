arr = [1,2,3,4,5,6,7,8]
unsorted_arr = [2,1,3,4,2,1,3,4,5,3,4,6,5,4,6]

# bubble Sort
print('         >Bubble Sort<       ')
bubble_arr = unsorted_arr.copy()
print('Unsorted' ,bubble_arr)

size = len(bubble_arr)
for i in range(size):
    swap = False
    for j in range(size-i-1):
        if bubble_arr[j] > bubble_arr[j+1]:
            bubble_arr[j] , bubble_arr[j+1] = bubble_arr[j+1] , bubble_arr[j]
            swap = True
    if not swap:
        break

print('Sorted' , bubble_arr)


# Insertion Sort
print('         >Insertion Sort<       ')
insertion_arr = unsorted_arr.copy()
print('Unsorted' ,insertion_arr)

size = len(insertion_arr)
for i in range(i, size):
    index = i
    current_value = insertion_arr[i]
    for j in range(i-1, -1, -1):
        if insertion_arr[j] > current_value:
            insertion_arr[j+1] = insertion_arr[j]
            index = j
        else:
            break
    insertion_arr[index] = current_value
print('Insertion Sorted', insertion_arr)

# Selection Sort
print('         >Selection Sort<       ')
selection_arr = unsorted_arr.copy()
print('Unsorted' ,selection_arr)
for i in range(size):
    min_index = i
    for j in range(i+1, size):
        if selection_arr[j] < selection_arr[min_index]:
            min_index = j
    selection_arr[i], selection_arr[min_index] = selection_arr[min_index], selection_arr[i]

print('Sorted', selection_arr)
