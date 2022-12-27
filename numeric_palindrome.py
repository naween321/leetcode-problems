def is_palindrome(x):
    if x < 0:
        return False
    summ = 0
    num = x
    while x != 0:
        c = x % 10
        x = x // 10
        summ = summ * 10 + c
    return summ == num


print(is_palindrome(121))
