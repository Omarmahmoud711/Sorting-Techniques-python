import time
import random

def quick_sort(arr):
    length = len(arr)
    quick_sort_recursion(arr, 0, length-1)


def quick_sort_recursion(arr, low, high):
    if low < high:
        pivloc = partition(arr, low, high)
        quick_sort_recursion(arr, low, pivloc-1)
        quick_sort_recursion(arr, pivloc+1, high)


def partition(arr, low, high):
    piv_val = arr[high]
    i = low
    for j in range(low, high):
        if arr[j] <= piv_val:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[high] = arr[high], arr[i]
    return i
#-----------------------------------------------------------------------------------------------------------------------------------
def mergeSort(myList):
    if len(myList) > 1:
        mid = len(myList) // 2
        left = myList[:mid]
        right = myList[mid:]

        mergeSort(left)
        mergeSort(right)
        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                myList[k] = left[i]
                i += 1
            else:
                myList[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            myList[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            myList[k] = right[j]
            j += 1
            k += 1


#-----------------------------------------------------------------------------------------------------------------------------------
def insertion_sort(a):
    length=len(a)
    for i in range(1,length):
        key = a[i]
        j = i-1
        while j>=0 and a[j]>key:
            a[j+1]=a[j]
            j-=1
        a[j+1]=key
#-----------------------------------------------------------------------------------------------------------------------------------
def selection_sort(arr):
    for i in range(0,len(arr)-1):
        cur_min_idx=i
        for j in range (i+1,len(arr)):
            if arr[j]<arr[cur_min_idx]:
                cur_min_idx=j
        arr[i],arr[cur_min_idx]=arr[cur_min_idx],arr[i]


#-----------------------------------------------------------------------------------------------------------------------------------
def heapify(arr,i,upper):
    while(True):
        l,r=i*2+1,i*2+2
        if max(l,r)<upper:
            if arr[i]>=max(arr[l],arr[r]): break
            elif arr[l]>arr[r]:
                arr[i],arr[l]=arr[l],arr[i]
                i=l
            else:
                arr[i],arr[r]=arr[r],arr[i]
                i=r
        elif l<upper:
            if arr[l]>arr[i]:
                arr[i], arr[l] = arr[l], arr[i]
                i = l
            else:break
        elif r<upper:
            if arr[r] > arr[i]:
                arr[i], arr[r] = arr[r], arr[i]
                i = r
        else:break

def build_max_heap(arr):
    for j in range((len(arr)-2)//2,-1,-1):
        heapify(arr,j,len(arr))

def heapsort(arr):
    build_max_heap(arr)
    for end in range (len(arr)-1,0,-1):
        arr[0],arr[end]=arr[end],arr[0]
        heapify(arr,0,end)


#-----------------------------------------------------------------------------------------------------------------------------------

def hybrid(Arr,thres):
    size = len(Arr)
    if size <= thres:
        return selection_sort(Arr)
    else:
        left = 0
        right = len(Arr)
        mid = (left + right) // 2
        hybrid(Arr[:mid], thres)
        hybrid(Arr[mid:], thres)
        mergeSort(Arr)

#-----------------------------------------------------------------------------------------------------------------------------------
length=int(input("please enter the len of array U want "))
alist = [random.randint(0,50000) for i in range (length)]
print("What type of sorting do U want ? ")
print("1.Quick sort")
print("2.Merge sort")
print("3.Insertion sort")
print("4.Selection sort")
print("5.Heap sort")
print("6.Hybrid Merge and Selection")
a1=int(input())
if a1 ==1:
    start=time.time()
    quick_sort(alist)
    end=time.time()
    print(alist)
    print("it took ",(end-start)*(10^6),"milli Seconds")
    print("\n would you like to find the kth Smallest element ? 1-yes 2-no")
    op = int(input())
    if(op==1):
       print("Enter the value of k")
       k=int(input())
       print("the value of the " , k ,"th Smallest element is", alist[k-1])

if a1 ==2:
    start=time.time()
    mergeSort(alist)
    end=time.time()
    print(alist)
    print("it took ",(end-start)*(10^6),"milli Seconds")
if a1 ==3:
    start=time.time()
    insertion_sort(alist)
    end=time.time()
    print(alist)
    print("it took ",(end-start)*(10^6),"milli Seconds")
if a1 == 4:
        start = time.time()
        selection_sort(alist)
        end = time.time()
        print(alist)
        print("it took ", (end - start) * (10 ^ 6), "milli Seconds")
if a1 ==5:
    start=time.time()
    heapsort(alist)
    end=time.time()
    print(alist)
    print("it took ",(end-start)*(10^6),"milli Seconds")
if a1 ==6:
    threshold = int(input("please enter the THRESHOLD "))
    start=time.time()
    hybrid(alist,threshold)
    end=time.time()
    print(alist)
    print("it took ",(end-start)*(10^6),"milli Seconds")