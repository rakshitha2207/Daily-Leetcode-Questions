def return_subsequences(s):
    if(s==''):
        ans = ['']
        return ans
    
    smallAnswer = return_subsequences(s[1:])
    myChar = s[0]
    ans = []
    ans.extend(smallAnswer)

    for eachPermutation in smallAnswer:
        ans.append(myChar+eachPermutation)
    return ans


s = "abc"
l = return_subsequences(s)
print(l)