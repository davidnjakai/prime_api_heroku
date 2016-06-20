# generate primes
def primenos(n):
	primelist=[2,3]
	starter = 4
	while True:
		for i in range(2,(starter//2)+1):
			if starter % i == 0:
				break
		else:		
			primelist.append(starter)
		starter+=1
		if len(primelist) == n:
			break
	return primelist

# class PrimeChecker():
#   def __init__(self, number):
#     self.number = number
    
#   def calc_prime(self,num):
#     primelist = [2, 3]
#     starter = 4
#     while primelist[len(primelist) - 1] <= num:
#       for num in primelist:
#         if starter % num == 0:
#           starter += 1
#           break
#       else:
#         primelist.append(starter)
#         starter += 1
#     if primelist[len(primelist) - 1] == num:
#       return True
#     else:
#       return False
        
  
#   def is_prime(self):
#     if self.number >= 2 and self.number < 4:
#       return True
#     else:
#       return self.calc_prime(self.number)
