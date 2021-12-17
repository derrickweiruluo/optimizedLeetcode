'''
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).
Example 1:

Input: x = 2.00000, n = 10
Output: 1024.00000
Example 2:

Input: x = 2.10000, n = 3
Output: 9.26100
Example 3:

Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
'''


# x positive
def pow(x, n):
    if n == 0:
        return 1
    if n == 1:
        return x
    if n < 0:
        return pow(1/x, -n)
    
    half = pow(x, n // 2)   # 999//2 -> 499, -999//2  -500

    if n % 2 == 1:
        return half * half * x
    else:
        return half * half

print(pow(5, -2))
print(pow(5, 2))

'''
n= 10 -> 5 ->2 -> 1
n = -5, -> 5, -> 2, ->1
log(N)
half_1 * half_1 -> half_2 * half_2 * x
'''