def binarySearch(a, left, right,num):
    if left > right:
        return -1

    mid = (left+right)//2
    if a[mid] == num:
        return mid

    if num < a[mid]:
        return binarySearch(a, left, mid-1, num)

    else:
        return binarySearch(a, mid+1, right, num)

    

a= [1,2,3,4,5,6,7,8,9,10,12,14,17,18,20,22,24,25,26,27,29,30]
print(binarySearch(a,0, len(a), 10))
