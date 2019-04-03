num, nth = input("Enter the two numbers:").split()
def findDigit(num, nth): print(-1) if int(nth) < 0 else print(0) if int(nth) > len(num) else  print (num[len(num) - int(nth)])
findDigit(num, nth)