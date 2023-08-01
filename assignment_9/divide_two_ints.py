# Divide Two Integers (Facebook)
# 4. Given two integers, dividend and divisor, divide the two integers without using
# multiplication, division, and mod operator.

def Divide(num1, num2):

    ## determine the sign 
    sign = (1 if (num1 < 0 ^ num2 < 0) else -1)

    quotient = 0
    acc_val = 0

    dividend = abs(num1)
    divisor = abs(num2)

    for i in range(31, -1, -1):
        if (acc_val + (divisor << i) <= dividend):
            acc_val += divisor << i
            quotient |= 1 << i

    return quotient

# Driver code
dividend = 7
divisor = 2

print(Divide(dividend, divisor))