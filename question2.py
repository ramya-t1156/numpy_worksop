# find if the given number is a palindrome or not?
def isPalindrome(n):
  ans = n
  rev = 0
  while(n!=0):
    rev = rev*10+n%10
    n//=10
  return n==rev
n = int(input())
if(isPalindrome(n)):
  print(f"{n} is Palindrome")
else:
  print(f"{n} is not a Palindrome")
  
