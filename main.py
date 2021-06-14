#written by Lili Bagramyan
def prime_checker(number):
  prime=True
  for i in range(2,number):
    if number%i==0:
      prime=False
  if prime:
    return (print("Prime number!"))
  else:
    return (print("NOT a prime number!"))

numToCheck = int(input("I will check for you if number is prime or not. Please enter the number: "))
prime_checker(number=numToCheck)
