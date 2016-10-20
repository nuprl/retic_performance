from benchmark_tools.Runner import count_types
from script.ProcessText import *

def add_types(file_name, dir_path):
    """
    Add types to data files
    :param file_name: path
    :return: text file
    """
    list_of_list_lines = parse_file(file_name)
    for line_list in list_of_list_lines:
        file_names = get_file_names(dir_path)
        max_configs = get_max_configs_all_files(file_names)
        config = line_list[0]
        nums = config.split("-")
        print(nums)
        num_types = count_types(nums, max_configs)
        line_list[1] = num_types

    new_file = open("%s_2" % file_name, "w")
    for l in list_of_list_lines:
        new_file.write(' '.join((str (l))) + "\n")

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


add_types('Espionage.txt', '/../../Espionage')

