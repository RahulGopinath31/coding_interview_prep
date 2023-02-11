## Given a positive integer num, write a program that returns True if num is a perfect
# square else return False. Do not use built-in functions like sqrt. Also, talk about the time 
# complexity of your code.
## Test Cases:
# Input: 16
# Output: True
# Input: 14
# Output: False

def is_perfect_square(num):
    if num == 0 or num == 1:
        return True

    left = 0
    right = num//2
    while(left <= right):
        mid = left + (right - left) // 2

        if mid * mid == num:
            return True

        elif mid * mid > num:
            right = mid - 1

        else:
            left = mid + 1

    return False

#driver code:
num = 7
print(is_perfect_square(num))