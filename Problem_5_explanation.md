This creates a blockchain with three blocks made using a SHA-256 hash. 
When printed, each block (besides the first) displays the previous hash as well as the time (GMT). 
The time complexity for adding more blocks using the add_block() to the linked list is O(1).  
Each block needs to be stored with information for each item in the linked list, so the space complexity is O(N).