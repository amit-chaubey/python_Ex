text = "apple banana orange apple orange apple"

words = text.split()

freq = {}

for word in words:
    if word in freq:
        freq[word] += 1 
    else:
        freq[word] = 1

print(freq)

###Q2

def fibonacci(n):
    if n <=0:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))

###Q3

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print(is_prime(11))

###Q4

import time

def log_time(func):
    def wrapper():
        start_time = time.time()
        result = func()
        end_time = time.time()
        print(f"Time taken: {end_time -start_time}")
        return result
    return wrapper

@log_time
def slow_function():
    time.sleep(2)
    print("Function executed")

slow_function()
