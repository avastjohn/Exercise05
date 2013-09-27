from sys import argv

script, file_name = argv
# open the file
file_to_count = open(file_name)
# read the file
file_text = file_to_count.read().lower()

# counts instances of the given letter and prints count to the screen
def count_letter(letter_ord, file_text):
    letter_count = 0
    for i in file_text:
        if ord(i) == letter_ord:
            letter_count += 1
    print letter_count


# for every letter, call the count_letter function
def letter_loop(file_text):
    for i in range(97, 123):
        count_letter(i, file_text)

# start the process
letter_loop(file_text)
# close file when finished counting
file_to_count.close()