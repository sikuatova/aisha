
def filter_primes(num_list):
    l = list(filter(lambda x :  all(x % i !=0 for i in range(2,int(x/2)+1)),num_list))
    return l


  
print(filter_primes([1,2,3,4,5,6,7,8,9,10,11,13,12]))