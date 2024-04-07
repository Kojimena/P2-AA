# Python program using memoization 
import sys
dp = [[-1 for i in range(100)] for j in range(100)] # Matrix to store the result of subproblems


# Function for matrix chain multiplication 
def matrixChainMemoised(p, i, j):
	"""
	p[]: An array containing the dimensions of the matrices
	i: starting index
	j: ending index
	"""
	if(i == j):
		return 0
	
	if(dp[i][j] != -1): # Check if the value is already calculated
		return dp[i][j]
	
	dp[i][j] = sys.maxsize # Initialize the value to infinity
	
	for k in range(i,j): # Loop to find the minimum cost of multiplication of matrices
		dp[i][j] = min(dp[i][j], matrixChainMemoised(p, i, k) + matrixChainMemoised(p, k + 1, j)+ p[i - 1] * p[k] * p[j])
	
	return dp[i][j]

def MatrixChainOrder(p,n):
	"""
	p[]: An array containing the dimensions of the matrices
	n: Size of the array p[]
	"""
	i = 1
	j = n - 1
	return matrixChainMemoised(p, i, j)