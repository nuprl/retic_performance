"""
  Usage:
    python ProcessText.py DATA-FILE BENCHMARK-DIRECTORY
  Convert DATA-FILE into comma-separated-value (csv) format for use in R.
  Uses the code in BENCHMARK-DIRECTORY to infer function names from the
   configuration id's in DATA-FILE.
"""

import ast
import glob
import sys

def get_file_names(dir_path):
    """
    :param dir_path: Path of directory containing file names
    :return: list of file paths
    """
    return sorted(glob.glob(dir_path+"/typed/*.py"))
    #hardcoded = ["main.py", "player.py", "dealer.py"] # Take5 2016-04-20
    #hardcoded = ["main", "Other", "Population", "Utilities", "Automata"] # FSM 2016-05-13
    #hardcoded = ["dealer", "player", "main"]
    #return ["%s/typed/%s.py" % (dir_path, argh) for argh in hardcoded]


def read_from_file(txt_file, dir_path):
    """
    Process text file and write results to an output file
    :param txt_file: text file containing configs
    :param dir_path: Directory path to read files from
    :return: None
    """
    with open(txt_file, "r") as lines:
        with open("%s.csv" % txt_file.rsplit("/", 1)[1], "w") as output:

            file_names = get_file_names(dir_path)

            function_names = ",".join([",".join(get_function_names_for_file(file)) for file in file_names])
            header = "time, %s" % function_names
            print(header, file=output)

            for line in lines:
                [nums_str, num_types_str, times_str] = line.split("   ")
                num_list = get_nums(nums_str)
                times_list = get_times(times_str)
                res = convert_all_num(num_list, file_names)
                for t in times_list:
                    print("%s,%s" % (t, ",".join(res)), file=output)

def get_times(times):
    val = ast.literal_eval(times)
    if not isinstance(val, list):
      #print("WARNING: only 1 time in data row. Did you average the data? That's not good.")
      return [val]
    else:
      return val

def get_nums(a_line):
    """
    Gets
    :param a_line: Line from text file
    :return: [int, ...]
    """
    s = a_line.strip()
    return s.split("-")


def convert_all_num(int_list, files):
    """
    Converts all numbers in this list to their appropriate binary formats
    and returns a list of tuples representing typed/untyped functions
    correspond to the numbers in the text files.
    :param int_list: List of int
    :param files: file paths
    :return: [1/0, ...]

    """
    max_list = get_max_configs_all_files(files)
    res = []
    for i in range(len(int_list)):
        number = int_list[i]
        max_number = max_list[i]
        bits = determine_config(number, max_number)

        for b in bits:
            #look for each function in config.
            res.append(b)

    return res


def get_function_names_for_file(file):
    """
    Gets all function names in this file
    :param file: a file
    :return: [String, ...]
    """
    # print("getting ffnction names for file %s" % file)
    with open(file) as f:
        file_name = file.rsplit("/", 1)[-1].split(".", 1)[0]
        tree = ast.parse(f.read())
        names = []
        unvisited = [x for x in tree.body]
        while unvisited:
            exp = unvisited.pop()
            if isinstance(exp, ast.FunctionDef):
                names.append("%s.%s" % (file_name, exp.name))
            elif isinstance(exp, ast.ClassDef):
                unvisited.extend([x for x in exp.body])

        return names

def determine_config(num, max_number):
    """
    Given the number of configuration, and the maximum number this configuration could have
    returns a list of 0 or 1 based on whether the function is typed.
    :param num int
    :param max_number: maximum number for this configuration
    :return: [0 or 1, ...]
    """
    return convert_num_to_binary(num, max_number)

def get_num_of_configs(python_file):
    """
    Gets the max number of configurations for a given file
    :param python_file: python file path
    :return: int
    """
    return len(get_function_names_for_file(python_file))

def get_max_configs_all_files(files):
    """
    Gets the maximum number of configurations for
    all files in the list
    :param files: list of python files paths
    :return: [Int, ...]
    """
    max_configs = []
    for file in files:
        max_configs.append(get_num_of_configs(file))

    return max_configs


def convert_num_to_binary(number, max_number):
    """
    Converts this number to the appropriate binary format
    :param number: int
    :param max_number: int
    :return: Binary number
    """
    #Need to convert this string based on max_number
    config = bin(int(number))[2:]
    x =  config.zfill(max_number)
    return x

if __name__ == "__main__":
  read_from_file(sys.argv[1], sys.argv[2])
