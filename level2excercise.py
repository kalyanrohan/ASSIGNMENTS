#LEVEL 2
"""
1.Using range(1,101), make a list containing only prime numbers.
"""
prime=[x for x in range(2,101) if x%2!=0 and x%3!=0 and x%5!=0 and x%7!=0]
print(prime)
"""
2.Initialize a 2D list of 3*3 matrix. E.g.-
1	2	3
4	5	6
7	8	9

Check if the matrix is symmetric or not.
"""

"""
3. Sorting refers to arranging data in a particular format. Sort a list of integers in ascending order ( without using built-in sorted function ). One of the algorithm is selection sort. Use below explanation of selection sort to do this.
INITIAL LIST :
2	3	1	45	15
First iteration : Compare every element after first element with first element and if it is larger then swap. In first iteration, 2 is larger than 1. So, swap it.
1	3	2	45	15
Second iteration : Compare every element after second element with second element and if it is larger then swap. In second iteration, 3 is larger than 2. So, swap it.
1	2	3	45	15
Third iteration : Nothing will swap as 3 is smaller than every element after it.
1	2	3	45	15
Fourth iteration : Compare every element after fourth element with fourth element and if it is larger then swap. In fourth iteration, 45 is larger than 15. So, swap it.
1	2	3	15	45
"""

