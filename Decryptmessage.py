import collections
import re

# Part 1
# ehkmortu --> hetomukr ,
# I use Counter function to count the letters are more common in real message.txt
encrypted = "ehkmortu"
decrypted = "hetomukr"

with open("message.txt") as file:
    data = file.readlines()  # To read The lines
    s = str(data)  # casting the data with str
    regex = re.compile('[^a-zA-Z]')
    a = regex.sub(" ", s)
    # print(collections.Counter(s))  # Count every thing repeated in this text


# Part 2
def text(my_str):
    b = zip(encrypted + encrypted.lower(),
            decrypted + decrypted.lower())  # iterator of tuples where the first item in each passed iterator is paired together
    my_dict = dict(b)  # casting all iterations to dictionary we can see that as print(my_dict)
    return "".join(my_dict.get(ch, ch) for ch in my_str)  # Join all items in a tuple into a string


print(text(a))


# Part 3
# I'm not sure if I do this part very well !
def update():
    with open("results.txt", "w") as f:  # new txt file
        f.write("Original text file:\n")
        f.write(a)
        f.write("\n")
        f.write("The encryption for the above text is:\n")
        f.write(text(a))  # cl the function in part 2 and write the encryption text message to our new file.


update()


# Part 4

def file_lengthy(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1


print("Number of lines in my new file:", file_lengthy("results.txt"))


def longest_word(fname):
    with open(fname) as f:
        words = f.read().split()
        max_len = len(max(words, key=len))
        for word in words:
            regex = re.compile('[^a-zA-Z]')
            a = regex.sub("", str(word))
            if len(word) == max_len:
                longest_word = word
                return f"The long word in new file is: {longest_word} --->  {text(a)}"


print(longest_word("results.txt"))

if __name__ == "__main__":  # maybe better than to use this main in another python file with using importing !
    with open("message.txt", "a") as m:
        m.write("\n")
        m.write("eventually eventually eventually eventually ")
        m.write("\n")
        m.write("*   *\n*   *\n * * \n  *\n * *\n*   *\n*   *")  # we also can use a loops for row and column ,this too short.
