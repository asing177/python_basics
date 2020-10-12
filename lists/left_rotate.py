arr = [1,2,3,4,5,6]
k = 2

def left_rotate(arr, d):
    for i in range(d):
        left_rotate_one(arr,len(arr))

def left_rotate_one(arr,n):
    temp = arr[-1]
    print(arr)
    for i in range(n):
        print(arr)
        arr[i-1] = arr[i]



def print_arr(arr):
    for i in range(len(arr)):
        print("%d" % arr[i], end="")

left_rotate(arr,k)
print_arr(arr)