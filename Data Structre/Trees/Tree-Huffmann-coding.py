
"""class Node:
    def __init__(self, freq,data):
        self.freq= freq
        self.data=data
        self.left = None
        self.right = None
"""        

# Enter your code here. Read input from STDIN. Print output to STDOUT
def decodeHuff(root, s):
    #Enter Your Code Here
    decode=[]
    cur= root
    def decode_char(A):
        if A.left is None and A.right is None:
            decode.append(A.data)
            return root
        else:
            return A

    for i in s:
        if i=='0':
            cur= decode_char(cur.left)
        if i=='1':
            cur= decode_char(cur.right)
    
    print(''.join(decode))







ip = input()
freq = {}#maps each character to its frequency

cntr = 0

for ch in ip:
    if(freq.get(ch) == None):
        freq[ch] = 1
    else:
        freq[ch]+=1

root = huffman_hidden()#contains root of huffman tree

code_hidden = {}#contains code for each object

dfs_hidden(root, "")

if len(code_hidden) == 1:#if there is only one character in the i/p
    for key in code_hidden:
        code_hidden[key] = "0"

toBeDecoded = ""

for ch in ip:
   toBeDecoded += code_hidden[ch]

decodeHuff(root, toBeDecoded)
