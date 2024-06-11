#!/usr/bin/env python
# Foundations of Python Network Programming - Chapter 8 - squares.py
# Using memcached to cache expensive results.

import memcache  # Import the memcache module to interact with Memcached
import random    # Import the random module to generate random numbers
import time      # Import the time module to add delays
import timeit    # Import the timeit module to measure execution time

# Initialize a Memcached client connecting to the local Memcached server on port 11211
mc = memcache.Client(['127.0.0.1:11211'])

def compute_square(n):
    """
    Compute the square of the number n, using a cache to store results.
    """
    # Try to get the value from the cache
    value = mc.get('sq:%d' % n)
    
    # If the value is not in the cache, compute it
    if value is None:
        time.sleep(0.001)  # Simulate an expensive operation by sleeping for 1 millisecond
        value = n * n       # Compute the square of n
        
        # Store the computed value in the cache with the key 'sq:n'
        mc.set('sq:%d' % n, value)
    
    return value  # Return the square of n (from cache or newly computed)

def make_request():
    """
    Make a request to compute the square of a random integer between 0 and 5000.
    """
    compute_square(random.randint(0, 5000))

# Print the heading for timing results
print('Ten successive runs:')

# Perform the timing measurement 10 times
for i in range(1, 11):
    # Measure the time it takes to call make_request 2000 times
    execution_time = timeit.timeit(make_request, number=2000)
    # Print the execution time rounded to two decimal places
    print('%.2fs' % execution_time, end=' ')
print()  # Print a newline after all the timing results
