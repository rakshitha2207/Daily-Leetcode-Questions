def single_digit(num):
    sum = 0
    while num > 0:
        temp = num % 10
        sum = sum + temp
        num = num // 10   
    if num == 0:
        sum = str(sum)
        new_sum = 0
        for i in range (0,len(sum)):
            new_sum += int(sum[i])
        return new_sum


num = 12345
ans = single_digit(num)
print(ans)