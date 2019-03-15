def write_in_file(file, word):
    file = open(file, "a")
    file.write(word+"\n")


def get_file(file):
    file = open(file, "r")
    return file
