def decimal_to_binary(decimal):
    binary = bin(decimal)[2:]
    print(binary)
    toggled = ''.join(['1' if bit=='0'  else '0' for bit in binary])
    print(toggled)
    decimal = int(toggled, 2)
    return decimal


decimal = 10
ans = decimal_to_binary(decimal)
print(ans)
