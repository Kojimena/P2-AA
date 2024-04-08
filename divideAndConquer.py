# Python code to implement the matrix chain multiplication using recursion
import sys

# Matrix A[i] has dimension p[i-1] x p[i]
def MatrixChainOrder(p, i, j): # for i = 1..n

    # Base case: if there's only one matrix in the chain, multiplication count is 0.    
    if i == j:
        return 0

    # Initialize the minimum count to maximum value
    minValue = sys.maxsize

    """
    Place parenthesis at different places between first and last matrix, 
    recursively calculate count of multiplications for each parenthesis placement 
    and return the minimum count.
    """
    for k in range(i, j):

        """
     Calculate the count of multiplications for the current partitioning of matrices,
        where k represents the split point. Recursively calculate the counts for the
        left and right partitions and multiply the dimensions of the matrices involved
        in the current split to account for the current multiplication.
        """
        count = (MatrixChainOrder(p, i, k) + MatrixChainOrder(p, k + 1, j) + p[i-1] * p[k] * p[j])

        # Update the minimum count if the calculated count is smaller
        if count < minValue:
            minValue = count

    # Return minimum count
    return minValue

# Main function
def divideAndConquerSolution(arr):
    N = len(arr)
    
    # Function call
    print("Minimum number of multiplications is", MatrixChainOrder(arr, 1, N-1))

# Example of usage
arr = [1, 2, 3, 4, 5]
divideAndConquerSolution(arr)
