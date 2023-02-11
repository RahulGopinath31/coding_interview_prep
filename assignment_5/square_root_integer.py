## find the integer part of sqaure root of a non-negative number

## naive method
def square_root(number):
    if number < 0:
        return False
   
    ## it is known that square root of a number lies  between 0 and n//2 value
    i = 0
    while True:
        if i * i <= number:
            i = i + 1
        else:
            return i-1


# optimized method : using binary search
## used the logic that 0 < sqrt(n) < n/2, sqare root of a number at most equals to half of the original number
def square_root_bi_search(number):
    if number == 0:
        return 0

    if number < 4:
        return 1

    left = 0
    right = number // 2
    sqrt_value = 0

    while(left < right):
        mid = left + (right - left)//2

        if mid * mid == number:
            return mid

        elif mid * mid < number : 
            left =  mid + 1
            sqrt_value = mid


        else:
            right = mid - 1

    return sqrt_value
    

##driver code
number = 9999999999999999
print(square_root(number))