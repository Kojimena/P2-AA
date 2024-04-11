import time
import matplotlib.pyplot as plt
from dynamic import *
import numpy as np

test_entries = [list(range(1, n + 2)) for n in range(2, 32)] 
 
counter = 1
for entry in test_entries:
    print(f"Entry {counter}: {entry}")
    counter += 1


def time_algorithm(entries):
    times = []
    for entry in entries:
        start_time = time.time()
        MatrixChainOrder(entry, len(entry))
        print("Minimum number of multiplications is",MatrixChainOrder(entry, len(entry)))
        end_time = time.time()
        times.append(end_time - start_time)
    return times

if __name__ == '__main__':
    times = time_algorithm(test_entries)

    plt.figure(figsize=(10, 6))
    plt.plot([len(entry) for entry in test_entries], times, marker='o')
    plt.title('Execution Time of Matrix Chain Multiplication with Memoization')
    plt.xlabel('Number of Matrices')
    plt.ylabel('Execution Time (seconds)')
    plt.grid(True)
    plt.xticks(np.arange(2, 33, 2))  
    plt.tight_layout()
    plt.show()
