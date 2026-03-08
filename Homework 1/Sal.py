def can_transport(weights, K, capacity):
    n = len(weights)
    used = [False] * n
    i = 0
    trips = 0
    while i < n:
        if used[i]:
            i += 1
            continue
        trips += 1
        if trips > K:
            return False
        total = weights[i]
        used[i] = True
        j = i + 1
        while j < n:
            if not used[j] and total + weights[j] <= capacity:
                total += weights[j]
                used[j] = True
            j += 1
        i += 1
    return True
def minimal_capacity(N, K, A):
    A.sort(reverse = True)
    low = max(A)
    high = sum(A)
    result = high
    while low <= high:
        mid = (low + high) // 2
        if can_transport(A, K, mid):
            result = mid
            high = mid - 1
        else:
            low = mid + 1
    return result
N, K = map(int, input("Enter the count of goats and courses:").split())
A = list(map(int, input(f"Enter {N} weights:").split()))
print("The minimal capacity is:", minimal_capacity(N, K, A))