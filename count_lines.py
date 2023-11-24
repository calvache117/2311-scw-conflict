import sys
"""
This script counts the lines in standard input 
Input: text from the system
Output: Number of lines (I guess)
Author: Calvache, Miguel
"""
print("hello you")

count = 0
for line in sys.stdin:
	count +=1

print(count, 'lines in standard input')
