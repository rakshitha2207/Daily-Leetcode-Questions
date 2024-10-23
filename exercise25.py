# # Return all codes

# def get_char(value):
#     if(value <= 0 or value > 26):
#         return ''
#     return chr(97+value-1)


# def return_all_codes(input):

#     if(input==''):
#         return ['']
    
#     if(len(input)==1):
#         singleChar = get_char(int(input))
#         return [singleChar]
    
#     singleDigit = int(input[0:1])
#     doubleDigit = int(input[0:2])
#     mainAns = []

#     answerWithoutFirstDigit = return_all_codes(input[1:])

#     for eachAns in answerWithoutFirstDigit:
#         mainAns.append(get_char(singleDigit)+eachAns)

#     if(doubleDigit>=10 and doubleDigit<=26):
#         answerWithoutFirstDigit = return_all_codes(input[1:])
#         for eachAns in answerWithoutFirstDigit:
#             mainAns.append(get_char(doubleDigit)+eachAns)

#     return mainAns        


# ans = return_all_codes('1123')
# print(ans)



def get_char(value):
    if(value <= 0 or value > 26):
        return ''
    return chr(97 + value - 1)

def print_all_codes(input, output_so_far=''):
    if input == '':
        print(output_so_far)
        return
    
    # Process single digit
    singleDigit = int(input[0:1])
    print_all_codes(input[1:], output_so_far + get_char(singleDigit))

    # Process double digits (if valid)
    if len(input) >= 2:
        doubleDigit = int(input[0:2])
        if 10 <= doubleDigit <= 26:
            print_all_codes(input[2:], output_so_far + get_char(doubleDigit))

# Example usage
print_all_codes('1123')
