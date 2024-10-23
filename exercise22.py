def print_permutation(s,takenSoFar):
    if(len(s)==0 or s == ''):
        print(takenSoFar)
        return
    
    ourChar = s[0]
    smallInput = s[1:]

    for i in range(0,len(takenSoFar)+1):
        print_permutation(smallInput, takenSoFar[0:i]+ ourChar + takenSoFar[i:])
    return    


print_permutation('abc','')

