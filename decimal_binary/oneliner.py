from math import log2


def decimal_to_binary(n):
    k = (1 << int(log2(n))+1) -1
    ans = n ^ k
    return ans




n = 10
ans = decimal_to_binary(n)
print(ans)