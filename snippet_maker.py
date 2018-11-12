import re 
import json
from collections import OrderedDict


def remove_new_line_marker(line):
    return re.sub(r"[\s\n]$", "", line)


def add_tab_symbol(line):
    for spaces in range(32, 3, -4):
        pattern = re.compile(r"^[\s]{%s}" %spaces)
        if re.match(pattern, line):
            return re.sub(pattern, "\t" * int(spaces / 4), line)
    return line


def build_json_file(prefix: str, description: str):
    """ 
    Builts a json file out of a txt files. 
    Used for transforming python scripts into their json representation.
    """
    body = []
    with open("python_snippet.txt", "r") as f:
        file = f.readlines()
    for line in file:
        line = remove_new_line_marker(line)
        line = add_tab_symbol(line) 
        body.append(line)
    with open("python_snippet.json", "w") as f:
        f.write(json.dumps(
            OrderedDict({"prefix": prefix, "description": description, "body": body}),
            indent=4, separators=(',', ': ')
            ))


if __name__ == "__main__":
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument("-p", "--prefix", default="pytorch:prefix", type=str, help="Adds a prefix for the snippet")
    parser.add_argument("-d", "--description", default="Short description", type=str, help="Adds a description to the snippet")
    args = parser.parse_args()
    build_json_file(args.prefix, args.description)
