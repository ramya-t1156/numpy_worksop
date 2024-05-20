#write a program to find the sum of digits of a given number'
def sumDig(n):
  sum = 0
  while(n!=0):
    sum+=num%10
    n//=10
  return sum
n = int(input())
result = sumDig(n)
print(result)
