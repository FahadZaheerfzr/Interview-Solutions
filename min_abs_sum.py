def solution(numbers):
    '''Returns the minimum absolute sum of any two numbers in the list.'''

    # Sort the list in ascending order
    sorted_list = sorted(numbers)

    # Initialize the variables
    front, back = len(sorted_list) - 1, 0
    result = 999999999

    # Loop until the front and back meet
    while front >= back:
        # Calculate the sum of the two numbers
        temp_sum = sorted_list[front] + sorted_list[back]
        # If the sum is less than the result, update the result
        result = min(result, abs(temp_sum))

        # If the sum is less than 0, move the back pointer forward
        # If the sum is greater than 0, move the front pointer backward
        if temp_sum > 0:
            front -= 1
        elif temp_sum < 0:
            back += 1
    
    # Return the result
    return result


# Test cases
if __name__ == "__main__":
    print(solution([1, 4, -3])) # 1
    print(solution([-8, 4, 5, -10, 3])) # 3
    print(solution([2, 2, 2, 4, 5])) # 2
    