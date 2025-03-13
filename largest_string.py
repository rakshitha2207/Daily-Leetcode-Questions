def largest_string(str):
    max_len = 0
    words = str.split()
    for word in words:
        length = len(word)
        if length > max_len: 
            max_len = length
            max_word = word
    return max_len, max_word        
    


str = "Hello Worlds"
ans = largest_string(str)
print(ans)