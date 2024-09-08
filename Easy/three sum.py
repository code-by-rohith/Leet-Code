import time
def three_sum(arr, k):
    n = len(arr)
    result = set()

    for i in range(n):
        seen = {}
        current_sum = k - arr[i]

        for j in range(i + 1, n):
            complement = current_sum - arr[j]
            if complement in seen:
                triplet = tuple(sorted([arr[i], arr[j], complement]))
                result.add(triplet)
            seen[arr[j]] = j

    return list(result)




