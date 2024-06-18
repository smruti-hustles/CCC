def leader_sum(arr):
    n = len(arr)
    if n == 0:
        return 0
    
    max_from_right = arr[-1]
    leader_sum = max_from_right
    
    for i in range(n-2, -1, -1):
        if arr[i] > max_from_right:
            max_from_right = arr[i]
            leader_sum += arr[i]
    
    return leader_sum

# Example usage
arr = [16, 17, 4, 3, 5, 2]
result = leader_sum(arr)
print(f"Sum of leader elements: {result}")  # Output: Sum of leader elements: 24
