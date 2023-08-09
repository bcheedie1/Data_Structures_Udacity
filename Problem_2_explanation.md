The function traverses the given directory recursively and therefore is O(N) for time complexity as it is dependent on the size of the directory. 
This is similar for space complexity; due to its recursive nature it will also be O(N). 
The space is limited by the number of files in the directory, which in this case will be N = 16. 
For this size of directory, this level of recursion is sufficient. A DFS could be used for a much larger directory.