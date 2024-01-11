'''
You are given list of numbers, obtained by rotating a sorted list an unknown number of times.
Write a function to determine the minimum number of times the original sorted list was rotated to obtain the given list.
Your function should have the worst-case complexity of O(log N), where N is the length of the list.
You can assume that all the numbers in the list are unique.
Example: The list [5, 6, 9, 0, 2, 3, 4] was obtained by rotating the sorted list [0, 2, 3, 4, 5, 6, 9] 3 times.
We define "rotating a list" as removing the last element of the list and adding it before the first element. E.g. rotating the list [3, 2, 4, 1] produces [1, 3, 2, 4].
"Sorted list" refers to a list where the elements are arranged in the increasing order e.g. [1, 3, 5, 7].
'''

tests = []

# query occurs in the middle
tests.append({
    'input': {
        'list': [5, 6, 9, 0, 2, 3, 4],

    },
    'output': 3
})

tests.append({
    'input': {
        'list': [15, 18, 2, 3, 6, 12] ,

    },
    'output': 2
})

tests.append({
    'input': {
        'list': [19, 25, 29, 3, 5, 6, 7, 9, 11, 14] ,

    },
    'output': 3
})

def count_rotations(list):
    n=len(list)
    start = 0
    end = n-1
    while start <= end:
        mid = (start + end) // 2
        if list[mid]<list[mid-1] and list[mid]<=list[mid+1]:
            return mid
        elif list[mid]<list[0]:
            end = mid - 1
        else:
            start = mid + 1
    return -1

# Test
for test in tests:
    print("Output:",count_rotations(**test['input']))
    print ("Is correct:",count_rotations(**test['input']) == test['output'])