def decimal_to_binary(n):
    res = ''
    while n > 0:
        res = str(n % 2) + res
        n = n // 2
    return res

def toggle_bits(binary_str):
    toggled = ''
    for bit in binary_str:
        if bit == '1':
            toggled += '0'
        else:
            toggled += '1'
    return toggled

def binary_to_decimal(binary_str):
    power = 0
    decimal = 0
    for i in range(len(binary_str) - 1, -1, -1):
        bit = int(binary_str[i])
        decimal += bit * (2 ** power)
        power += 1
    return decimal

# Main
n = 10
binary = decimal_to_binary(n)              # '1010'
toggled = toggle_bits(binary)              # '0101'
result = binary_to_decimal(toggled)        # 5

print("Original Decimal:", n)
print("Binary:", binary)
print("Toggled Binary:", toggled)
print("Decimal after toggle:", result)
