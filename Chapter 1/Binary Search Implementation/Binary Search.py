def binarySearch (list, item):
    low = 0
    high = len (list)-1
    
    while low <= high:
        mid = (low + high)//2
        guess = list [mid]     # guess has the value of the middle element
        if guess ==item:
            return mid
        if item < guess:
            high = mid -1
        else:
            low = mid +1
    return None

my_list= []
for i in range (1,100):
    my_list.append(i)
print (binarySearch(my_list, 500))                