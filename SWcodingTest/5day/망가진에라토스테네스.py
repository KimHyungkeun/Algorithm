import sys

n = int(sys.stdin.readline())

def prime (num) :
	i = 2
	while i*i <= num+1 :
		if num % i == 0 :
			return 0
		i += 1
	return 1

def solution () :
	if n == 1: 
		print(0)
	
	i = 2
	while i*i <= n+1 :
		if n % i == 0 :
			if prime(i) and prime((n // i)) :
				print(1)
				return

			else :
				print(0)
				return
		i += 1
	
	print(1)
	return

solution()