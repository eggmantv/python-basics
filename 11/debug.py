import os

def write_file(file):
    with open(file, mode='wt', encoding="utf-8") as f:
        f.write("apple\n")
        f.write("pineapple\n")
        f.write("grape")
        f.writelines(["banana\n", "pear\n", "orange"])

def read_file(file):
    f = open(file, 'rt')
    try:
        for line in f:

            # import pdb
            # pdb.set_trace()

            word = line.strip()
            print(word)
    finally:
        f.close()


if __name__ == '__main__':
    file = os.path.join(os.path.dirname(__file__), 'words.txt')
    write_file(file)
    read_file(file)
