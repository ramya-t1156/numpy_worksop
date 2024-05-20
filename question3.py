#write a program to find the factorial of a nummber
def fact(n):
  if n==1 || num==0:
    return 1
  else:
    return n*fact(n-1)
  n = int(input())
  if(fact(n)):
    print(f"{n} is Palindrome")
  else:
    print(f"{n} is not a Palindrome")
  
