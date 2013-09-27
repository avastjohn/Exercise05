from sys import argv

script, file_name = argv
# open the file
file_to_count = open(file_name)

# initialize count list
counts = [0] * 26 

# read one line at a time
for line in file_to_count:
    # make lowercase, increment count for each letter
    for i in line:
        i = i.lower()
        if ord(i) >= 97 and ord(i) < 123:
            counts[ord(i) - 97] += 1

# prints count of each letter alphabetically
for i in counts:
    print i 
