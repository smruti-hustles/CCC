#reversing the array/list 
l=list(map(int,input().split()))
ans=l[::-1]
print(ans)
'''
input
10 20 3 4 78
output
[78, 4, 3, 20, 10]
'''
#reverse the list without distrbing the even numbers
def reverse_odds(arr):
    # Extract odd numbers and their positions
    odds = [num for num in arr if num % 2 != 0]
    odd_positions = [i for i, num in enumerate(arr) if num % 2 != 0]
    
    # Reverse the list of odd numbers
    reversed_odds = odds[::-1]
    
    # Create a copy of the original array to modify
    result = arr[:]
    
    # Place the reversed odd numbers back into their original positions
    for pos, num in zip(odd_positions, reversed_odds):
        result[pos] = num
    
    return result

# Example usage
arr = [1, 2, 3, 4, 5, 6, 7, 8]
reversed_arr = reverse_odds(arr)
print(reversed_arr)  # Output: [7, 2, 5, 4, 3, 6, 1, 8]

