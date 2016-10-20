def add_types(file_name):
    """
    Add types to data files
    :param file_name: path
    :return: text file
    """
    list_of_list_lines = parse_file(file_name)
    for line_list in list_of_list_lines:
        num_types = line_list[1]

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

