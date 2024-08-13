def chunk_array(arr, size):
    chunked_array = []
    for i in range(0, len(arr), size):
        chunked_array.append(arr[i:i+size])
    return chunked_array

arr2 = [1, 9, 6, 3, 2]
size2 = 3
print(chunk_array(arr2, size2))


