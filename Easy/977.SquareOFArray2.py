def main(arr):
    res=[]
    left=0
    right=len(arr)-1
    while left <=right:
        if arr[left]**2 > arr[right]**2:
            res.append(arr[left]**2)
            left+=1
        else:
            res.append(arr[right]**2)
            right -=1
    return res[::-1]
  

arr = [-3, -2, 0, 1, 2, 3, 4, 5]
print(main(arr))












