# merging two sorted lists in O(n)

def spl_sort(l1, l2):
	l3 = []
	i = 0;
	j = 0;
	n1 = len(l1)
	n2 = len(l2)
	while(i<n1 and j<n2):
		if l1[i] < l2[j]:
			l3.append(l1[i])
			i += 1
		elif l1[i] == l2[j]:
			l3.append(l1[i])
			l3.append(l2[j])
			i += 1
			j += 1
		else:
			l3.append(l2[j])
			j += 1
	l3 += l1[i:]
	l3 += l2[j:]

	return l3

l1 = [1,3,5,7,9,10,11,12]
l2 = [2,4,6,6,7,9]

print spl_sort(l1, l2)

def quick_sort(arr, low, high):
	if low < high:
		pivot = partition(arr, low, high)

		quick_sort(arr, low, pivot-1)
		quick_sort(arr, pivot+1, high)
	else:
		print "Sorted!"
		return arr

def swap(arr, i, j):
	temp = arr[i]
	arr[i] = arr[j]
	arr[j] = temp


def partition(arr, low, high):
	i = (low-1) # index of smaller elements
	pivot = arr[high] # always pick rightmost element

	j = low
	for j in range(low, high):
		if arr[j] <= pivot:
			i += 1
			# swap arr[i] and arr[j]
			swap(arr, i, j)
	
	# put the pivot in the right place
	swap(arr, i+1, high)
	return (i+1)

def merge_sort(arr, low, high):
    if low >= high:
        return

    mid = (low + high)/2
    print "merge_sort:", low, mid, high
    merge_sort(arr, low, mid)
    merge_sort(arr, mid+1, high)

    merge(arr, low, mid, high)

def merge(arr, low, mid, high):
	# same as spl_sort
    new_arr = []
    i = low
    j = mid+1
    while(i<=mid and j<=high):
    	# if elements are equal, add any one
    	# the next one will go in in the next iteration
        if arr[i] <= arr[j]:
            new_arr.append(arr[i])
            i += 1
        else:
            new_arr.append(arr[j])
            j += 1
    # push whatever else remains
    new_arr += arr[i:mid+1]
    new_arr += arr[j:high+1]
    
    # copy it back into original array
    arr[low:(high+1)] = new_arr
