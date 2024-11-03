#### Multithreading
## When to use: 
# 1. Tasks that are I/O Bound, means spend more time waiting for I/O operations
# 2. Concurrent execution: When you want to improve the throughput of your application by performing multiple operations concurrently.

import threading
import time

def print_numbers():
    for i in range(5):
        time.sleep(2)
        print(f"number: {i}")

def print_letters():
    for letter in 'abcde':
        time.sleep(2)
        print(f"Letter: {letter}")

# t = time.time()
# print_numbers()
# print_letters()
# finished_time = time.time() - t
# print(finished_time)


## Creating Threads
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

t = time.time()

# Staring the threads
thread1.start()
thread2.start()

# Waiting for the threads to complete
thread1.join()
thread2.join()


finished_time = time.time() - t
print(finished_time)