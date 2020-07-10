# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here

# 1. Read ciphertext.txt and find the frequency of each letter inside
# 2. Create decode table using found frequencies and given frequency table
# 3. Decode ciphertext.txt 

freq_table = {
    "A" : 0,
    "B" : 0,
    "C" : 0,
    "D" : 0,
    "E" : 0,
    "F" : 0,
    "G" : 0,
    "H" : 0,
    "I" : 0,
    "J" : 0,
    "K" : 0,
    "L" : 0,
    "M" : 0,
    "N" : 0,
    "O" : 0,
    "P" : 0,
    "Q" : 0,
    "R" : 0,
    "S" : 0,
    "T" : 0,
    "U" : 0,
    "V" : 0,
    "W" : 0,
    "X" : 0,
    "Y" : 0,
    "Z" : 0,
    # " " : 0,
    # '"' : 0,
    # "," : 0,
    # "." : 0,
    # "!" : 0,
    # "'" : 0,
    # "\n": 0,
    # ";" : 0,
    # ":" : 0,
    # "-" : 0,
    # "?" : 0,
    # "—" : 0,
    # "(" : 0,
    # ")" : 0,
    # "1" : 0
}

freq_eng = "ETAOHNRISDLWUGFBMYCPKVQJXZ"

decoder = {}

with open('ciphertext.txt','r') as f_open:
    data = f_open.read()

# data = "OUS.BAYAA"

print(freq_table.keys())

for c in data:
    if c in freq_table.keys():
        freq_table[c] = freq_table[c] + 1
        # print(c, freq_table[c])
    # else:
    #     print(c)

# print(data[5])

# c = "Z"

# freq_table[c] = freq_table[c] + 1
# freq_table[c] = 666

print(freq_table)

sorted_table = freq_table.copy()

sorted_table = {k: v for k, v in sorted(sorted_table.items(), key=lambda item: item[1], reverse=True)}

print(sorted_table)

for c, e in zip(sorted_table.keys(), freq_eng):
    # print(c, e)
    decoder[c] = e

print("Decoder is ", decoder)

english = ""

for c in data:
    if c in freq_table.keys():
        english += decoder[c]
    else:
        english += c

print(english)