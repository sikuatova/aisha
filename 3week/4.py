n=2
def is_prime(num, n=2):
  if n >= num:  
      return True
  if num % n == 0:
      return False
  return is_prime(num, n+1)

def filter_prime(list1):
  list2 = []
  for i in list1:
    if is_prime(i):
      list2.append(i)

  print(list2)
  
filter_prime([1,2,3,4,5,6,7,8,9])
