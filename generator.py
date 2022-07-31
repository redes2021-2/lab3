import random
import sys
import names

# generate random matches of names separated by spaces
# Joao Pedro
# Pedro Joao
# ...
# output it to a file called "word_count.txt"
# end generating when file reaches 100 gb


with open("word_count_data.txt", "w") as f:
    for i in range(int(input("How many names? "))):
        name1 = names.get_first_name()
        name2 = names.get_first_name()
        f.write(name1 + " " + name2 + "\n")
        sys.stdout.write("\r{}".format(i))
        sys.stdout.flush()
    print("\n")
    print("Done!")
    f.close()
    sys.exit(0)
