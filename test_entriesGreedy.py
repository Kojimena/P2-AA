import time
import matplotlib.pyplot as plt
import numpy as np
from greedy import *

def time_algorithm(entries):
    times = []
    for entry in entries:
        start_time = time.time()
        result = Novel_MCM(entry)
        print("Minimum number of multiplications is:", result)
        end_time = time.time()
        times.append(end_time - start_time)
    return times

if __name__ == '__main__':
    test_entries = [list(range(1, n + 2)) for n in range(2, 32)] 

    counter = 1
    for entry in test_entries:
        print(f"Entry {counter}: {entry}")
        counter += 1
    
    # Timing the matrix chain multiplication for each entry
    times = time_algorithm(test_entries)

    # Plotting
    plt.figure(figsize=(10, 6))
    plt.plot([len(entry) for entry in test_entries], times, marker='o')
    plt.title('Execution Time of Matrix Chain Multiplication with Greedy')
    plt.xlabel('Number of Matrices')
    plt.ylabel('Execution Time (seconds)')
    plt.grid(True)
    plt.xticks(np.arange(2, 33, 2))  
    plt.tight_layout()
    plt.show()