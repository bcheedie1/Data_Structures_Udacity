# Write your code here :-)
import sys
import heapq
from collections import defaultdict

class Node:
    def __init__(self, character, frequency):
        self.character = character
        self.frequency = frequency
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.frequency < other.frequency

def build_huffman_tree(frequencies):
    priority_queue = [Node(char, freq) for char, freq in frequencies.items()]
    heapq.heapify(priority_queue)

    while len(priority_queue) > 1:
        left_child = heapq.heappop(priority_queue)
        right_child = heapq.heappop(priority_queue)

        merged_node = Node(None, left_child.frequency + right_child.frequency)
        merged_node.left = left_child
        merged_node.right = right_child

        heapq.heappush(priority_queue, merged_node)

    return priority_queue[0]

def build_encoding_table(root_node, encoding="", encoding_table={}):
    if not root_node:
        return

    if root_node.character:
        encoding_table[root_node.character] = encoding
        return

    build_encoding_table(root_node.left, encoding + "0", encoding_table)
    build_encoding_table(root_node.right, encoding + "1", encoding_table)

def huffman_encoding(data):
    frequencies = defaultdict(int)
    for char in data:
        frequencies[char] += 1

    huffman_tree = build_huffman_tree(frequencies)
    encoding_table = {}
    build_encoding_table(huffman_tree, encoding="", encoding_table=encoding_table)

    encoded_data = ""
    for char in data:
        encoded_data += encoding_table[char]

    return encoded_data, huffman_tree

def huffman_decoding(encoded_data, root_node):
    decoded_data = ""
    current_node = root_node

    for bit in encoded_data:
        if bit == "0":
            current_node = current_node.left
        else:
            current_node = current_node.right

        if current_node.character:
            decoded_data += current_node.character
            current_node = root_node  
    return decoded_data

if __name__ == "__main__":

    a_great_sentence = "The bird is the word"

    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))


    a_better_sentence = "AAAAAAABBBCCCCCCCDDEEEEEE"

    print("The size of the data is: {}\n".format(sys.getsizeof(a_better_sentence)))
    print("The content of the data is: {}\n".format(a_better_sentence))

    encoded_data, tree = huffman_encoding(a_better_sentence)

    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))


    a_good_sentence = "The 7 quick brown foxes jump over 400,000,129 lazy dogs."

    print("The size of the data is: {}\n".format(sys.getsizeof(a_good_sentence)))
    print("The content of the data is: {}\n".format(a_good_sentence))

    encoded_data, tree = huffman_encoding(a_good_sentence)

    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))

