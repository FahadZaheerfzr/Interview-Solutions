def solution(arr):
    arr.sort()
    front, back = len(arr) - 1, 0
    result = 999999999
    while front >= back:
        temp_sum = arr[front] + arr[back]
        result = min(result, abs(temp_sum))
        if temp_sum > 0:
            front -= 1
        elif temp_sum < 0:
            back += 1
    return result