# def mergesort(arr):
#     if len(arr) > 1:
#         mid = len(arr)//2
#         sa1 = arr[:mid]
#         sa2 = arr[mid:]

#         mergesort(sa1)
#         mergesort(sa2)

#         i = j = k = 0

#         while i < len(sa1) and j < len(sa2):
#             if sa1[i] < sa2[j]:
#                 arr[k] = sa1[i]
#                 i += 1
#             else:
#                 arr[k] = sa2[j]
#                 j += 1
#             k += 1
#         while i < len(sa1):
#             arr[k] = sa1[i]
#             i += 1
#             k += 1
# arr = [3,1,10,8,4,2]
# mergesort(arr)
# print(arr)

'''Quick sort'''

def partition(arr,low,high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i+1
            (arr[i], arr[j]) = (arr[j],arr[i])
        (arr[i+1], arr[high]) = (arr[high], arr[i+1])
        return i+1
def quicksort(arr,low,high):
    if low < high:
        pi = partition(arr,low,high)
        quicksort(arr,low,pi-1)
        quicksort(arr,pi+1,high)
arr = [67,89,19,90,28,78]
quicksort(arr,0,len(arr)-1)

print(f'Sorted array: {arr}')