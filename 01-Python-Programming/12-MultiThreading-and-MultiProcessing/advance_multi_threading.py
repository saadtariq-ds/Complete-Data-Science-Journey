### Multi Threading With Thread Pool Executor

from concurrent.futures import ThreadPoolExecutor
import time

def print_numbers(number):
    time.sleep(1)
    return f"number: {number}"

numbers = [1, 2, 3, 4, 5]

t = time.time()
with ThreadPoolExecutor(max_workers=3) as executor:
    results=executor.map(print_numbers, numbers)

for result in results:
    print(result)

finished_time = time.time() - t
print(finished_time)