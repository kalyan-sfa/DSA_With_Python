#Traversal
arr = [10, 20, 30, 40, 50] #list created
for i in arr:
    print(i)

#List methods
print(f'Original list: {arr}')

arr.append(40) #append method
print(f'List after append: {arr}')
count = arr.count(40)
print(f'Count of 40 in list: {count}')

#insert method
ins = arr.insert(2, 25) #insert method
print(f'List after insert: {arr}')

#remove method
remove = arr.remove(20)
print(f'List after remove: {arr}')

#pop method
pop = arr.pop(3) #pop method
print(f'List after pop: {arr}')

#reverse method
reverse = arr.reverse()
print(f'List after reverse: {arr}')

#index method
index = arr.index(30) #index method
print(f'Index of 30 in list: {index}')

#sort method
sort = arr.sort()
print(f'List after sort: {arr}')

#copy method
copy = arr.copy() #copy method
print(f'Copied list: {copy}')

#clear mwthod
clear = arr.clear()
print(f'List after clear: {arr}')

#Searching (Linear search)
array = [10, 20, 30, 40, 50]
key = 40

for i in range(len(array)): #len = 4 from 0 to 4
    if array[i] == key:
        print(f'Element {key} found at index {i}.')
        break

#2D Array
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for i in range(len(matrix)): #len = 3 from 0 to 2, i = 0
    row_sum = 0

    for j in range(len(matrix[i])): #len = 3 from 0 to 2, j = 0
        row_sum += matrix[i][j] # 0 += 1 = 1

        print("Row", i + 1, "Sum = ", row_sum)

#Binary Search
print("Binary search example:")
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid

        elif arr[mid] < target:
            low = mid + 1

        else:
            high = mid - 1

    return -1


arr = [10, 20, 30, 40, 50, 60, 70]

target = 50

result = binary_search(arr, target)

if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found")
