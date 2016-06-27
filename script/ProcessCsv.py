from ProcessText import *


def main(file, dir, pos):
    """
    Reads  lines from file & prints to output file
    :param file: file path
    :return:
    """
    with open("output.txt", "w") as output:
        with open(file, "r") as f:
            for line in f:
                if has_typed(line, dir, pos):
                    print(line.strip(), file=output)


def has_typed(line, dir, i):
    """
    Returns True if function in pos i is typed
    :param line: String
    :return: Boolean
    """
    config = line.split()[0]
    num_list = get_nums(config)
    file_names = get_file_names(dir)
    res = convert_all_num(num_list, file_names)
    return res[i] == "0"


if __name__ == "__main__":
  main(sys.argv[1], sys.argv[2], int(sys.argv[3]))
