def divisible(num):
    for num in range(1, num+1):
        divisors = []
        for i in range(1, num+1):
            if num % i == 0:
                divisors.append(str(i))
        print(f"{num} is divisible by {', '.join(divisors)}")        
        


num = int(input("Enter a number: "))
divisible(num)

