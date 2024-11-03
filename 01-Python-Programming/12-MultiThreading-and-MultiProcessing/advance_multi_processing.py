### Multiprocessing with ProcessPoolExecutor

from concurrent.futures import ProcessPoolExecutor
import time

def square_numbers(number):
    time.sleep(1)
    return f"number: {number**2}"

numbers = [1, 2, 3, 4, 5]


if __name__ == "__main__":
    t = time.time()
    
    with ProcessPoolExecutor(max_workers=3) as executor:
        results=executor.map(square_numbers, numbers)
    
    for result in results:
        print(result)

    finished_time = time.time() - t
    print(finished_time)