# Pow(x,n) (Facebook)
# 3. Implement pow(x,n) which calculates x raised to the power n (i.e. x^n)
# For example: x = 2.00000, n = -2
# Output: 0.25000
# Explanation: 2^-2 =½^2 = ¼ = 0.25

## method to find the power:
def power(x, n):

    if n == -1:
        return (1/x)
    
    if n == 1:
        return (x)

    mid = n // 2
    leftPower = power(x, mid)
    rightPower = power(x, n - mid)

    return leftPower*rightPower


## driver code
# x, n = 2, -5
# x, n = 4, -4
x, n = 43, -6
# x, n = 3, -5
result = power(x, n)
print(result)