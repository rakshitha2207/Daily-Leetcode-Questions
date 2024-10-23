# keys = {'1':'','2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno',
#         '7':'pqrs','8':'tuv','9':'wxyz'}

# def return_all_words(input):
#     if(input==''):
#         return ['']
    
#     ans = []

#     smallInput = input[1:]
#     smallInputWords = return_all_words(smallInput)

#     keysLetter = keys[input[0]]

#     for myChar in keysLetter:
#         for word in smallInputWords:
#             ans.append(myChar+word)

#     return ans  



# ans = return_all_words("23")
# print(ans)



keys = {1: '', 2: 'abc', 3: 'def', 4: 'ghi', 5: 'jkl', 6: 'mno',
        7: 'pqrs', 8: 'tuv', 9: 'wxyz'}

def return_all_words(input):
    # Base case: when the input is 0, return an empty string
    if input == 0:
        return ['']
    
    ans = []
    
    # Extract the last digit and find corresponding letters
    last_digit = input % 10
    small_input = input // 10
    
    small_input_words = return_all_words(small_input)

    # Get the corresponding characters for the last digit
    keys_letter = keys[last_digit]

    # Form words by combining characters of the last digit with the words from the smaller input
    for char in keys_letter:
        for word in small_input_words:
            ans.append(word + char)

    return ans

# Example with integer input
ans = return_all_words(23)
print(ans)

        