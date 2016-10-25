from script.ProcessText import *
from math import log2

def add_types(file_name, dir_path):
    """
    Add types to data files
    :param file_name: path
    :return: text file
    """
    list_of_list_lines = parse_file(file_name)
    file_names = get_file_names(dir_path)
    max_configs = get_max_configs_all_files(file_names)
    for line_list in list_of_list_lines:
        config = line_list[0]
        nums_str = config.split("-")
        nums = [int(n) for n in nums_str]
        print(nums)
        num_types = count_types(nums, max_configs)
        line_list[1] = str(num_types)

    new_file = open("%s_2" % file_name, "a")
    for l in list_of_list_lines:
        new_file.write('  '.join(l) + "\n")

def parse_file(file_name):
    """
    parse file and return a list of lines parsed
    :param file_name: path
    :return: list of lines
    """
    res = []
    with open(file_name) as f:
        lines = f.readlines()

    for line in lines:
        res.append(line.split())

    return res


def count_types(nums, lengths):
    """
    Number of typed functions across all the files
    :param nums: List of string
    :param lengths: lengths[i] is upper bound for nums[i]
    :return: Int, representing number of annotated functions in the file
    """
    total = 0
    for num, length in zip(nums, lengths):
        b = bin(int(num))[2:]
        l = int(log2(length))
        c = ("0" * (l - len(b))) + b
        total += sum([1 for bit in c if bit == '0'])

    return total

def get_name(fname):
    return fname.rsplit("/", 1)[-1].rsplit(".", 1)[0]

add_types('Espionage.txt', '/Users/zeinamigeed/Documents/fall2016/software_dev/retic_performance/Espionage')

