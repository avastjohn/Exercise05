from sys import argv

script, file_name = argv
# open the file
file_to_count = open(file_name)
# read the file
file_text = file_to_count.read().lower()


def count_letter_a():
    a_count = 0
    for i in file_text:
        if ord(i) == 97:
            a_count += 1
    return a_count

print count_letter_a()
