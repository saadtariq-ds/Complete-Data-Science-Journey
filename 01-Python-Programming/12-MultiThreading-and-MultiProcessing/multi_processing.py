## Allows to create processes that run in parallel.

## When to use
# 1. CPU-Bound Tasks
# 2. Parallel Execution - Multiple cores of the CPU

import multiprocessing
import time

def square_numbers():
    for i in range(5):
        time.sleep(1)
        print(f"Square: {i**2}")

def cube_numbers():
    for i in range(5):
        time.sleep(1)
        print(f"Cube: {i**3}")


if __name__ == "__main__":
    t = time.time()

    ## Create 2 processes
    process1 = multiprocessing.Process(target=square_numbers)
    process2 = multiprocessing.Process(target=cube_numbers)

    ## Start the process
    process1.start()
    process2.start()

    ## Wait for the process to complete
    process1.join()
    process2.join()

    finished_time = time.time() - t
    print(finished_time)