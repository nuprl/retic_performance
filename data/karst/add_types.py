from benchmark_tools.Runner import count_types


def get_lengths():
    directories = sorted(glob.glob('%s/*' % benchmark))
    all_files = [glob.glob('%s/*' % d) for d in directories]
    lengths = [len(files) for files in all_files]
    return lengths

def add_types(file_name):
    """
    Add types to data files
    :param file_name: path
    :return: text file
    """
    list_of_list_lines = parse_file(file_name)
    for line_list in list_of_list_lines:
        config = line_list[0]
        nums = config.split("-")
        num_types = count_types(nums, 0)

    new_file = open("%s_2" % file_name, "w")
    for l in list_of_list_lines:
        new_file.write(' '.join(l) + "\n")

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


add_types('Espionage.txt')

